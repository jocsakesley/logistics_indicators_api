from threading import Thread, RLock
import time
from werkzeug.datastructures import FileStorage
from queue import Queue
from sqlalchemy.exc import IntegrityError

from src.infra.config.logger import logger
from src.repositories.abstract_repository import AbstractRepository

class FileHandler:
    def __init__(self, file: FileStorage, queue: Queue, repository: AbstractRepository):
        self.file = file
        self.queue = queue
        self.repository = repository
        self.lock = RLock()
        self.__start_threads()
        self.__file_process_in_thread()

    def __file_process(self):
        for line in self.file.stream.read().decode('utf-8').split('\n'):
            self.queue.put(line)

    def __file_process_in_thread(self):
        process = Thread(target=self.__file_process)
        process.start()
        process.join()
    def __listen_queue(self):
        while True:
            with self.lock:
                chunks = []
                lines = []
                for _ in range(min(1000, self.queue.qsize())):
                    line = self.queue.get_nowait()
                    lines.append(line)
                    register = line.split(";")
                    if register[0].isnumeric():
                        customer_service = self.repository.model().load_by_file(*register)
                        chunks.append(customer_service)
                try:
                    self.repository.add_all(chunks)
                except IntegrityError:
                    continue     
                except Exception:
                    with self.lock:
                        [self.queue.put(line) for line in lines]
                    continue
            if self.queue.empty():
                time.sleep(0.1)
                end = time.time() - self.start
                if self.queue.empty():
                    time.sleep(10)
                    end = time.time() - self.start
                    if self.queue.empty():
                        end = time.time() - self.start
                        logger.info(f"Arquivo processado, encerrando Threads. Tempo passado desde o inicio: {end:.4f} segundos")

                        self.__remove_file()
                        break
    def __remove_file(self):
        try:
            self.file.close()
        except Exception as e:
            raise e

    def __start_threads(self):
        self.start = time.time()
        for _ in range(100):
            thread = Thread(target=self.__listen_queue, daemon=True)
            thread.start()
        


            
        