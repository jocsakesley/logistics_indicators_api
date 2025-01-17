from threading import Thread, RLock
import time
import logging
import csv
from werkzeug.datastructures import FileStorage
from queue import Queue, Empty

from src.models.base_model import BaseModel
from src.models.customer_service_model import CustomerServiceModel
from src.repositories.abstract_repository import AbstractRepository

class FileHandler:
    def __init__(self, file: FileStorage, queue: Queue, repository: AbstractRepository, model: BaseModel):
        self.file = file
        self.queue = queue
        self.repository = repository
        self.model = model
        self.lock = RLock()
        self.start_threads()
        self.file_process_in_thread()

    def file_process(self):
        for line in self.file.stream.read().decode('utf-8').split('\n'):
            self.queue.put(line)

    def file_process_in_thread(self):
        process = Thread(target=self.file_process)
        process.start()
        process.join()
    def listen_queue(self):
        while True:
            try:
                with self.lock:
                    chunks = []
                    lines = []
                    for i in range(min(1000, self.queue.qsize())):
                        line = self.queue.get_nowait()
                        lines.append(line)
                        register = line.split(";")
                        if register[0].isnumeric():
                            customer_service = self.model().load_by_file(*register)
                            chunks.append(customer_service)
                    try:
                        self.repository.add_all(chunks)
                    except Exception:
                        with self.lock:
                            [self.queue.put(line) for line in lines]
            except Empty:
                time.sleep(0.1)
                if self.queue.empty():
                    empty_start = time.time()
                    while self.queue.empty() and (time.time() - empty_start) < 10:
                        time.sleep(0.1)
                    if self.queue.empty():
                        break
                continue

    def start_threads(self):
        for i in range(100):
            thread = Thread(target=self.listen_queue, daemon=True)
            thread.start()
        


            
        