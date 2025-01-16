from threading import Thread, RLock
import time
import logging
import csv
from werkzeug.datastructures import FileStorage
from queue import Queue, Empty

from src.models.customer_service_model import CustomerServiceModel
from src.repositories.abstract_repository import AbstractRepository

class FileHandler:
    def __init__(self, file: FileStorage, queue: Queue, repository: AbstractRepository):
        self.file = file
        self.queue = queue
        self.repository = repository
        self.lock = RLock()
        self.start_threads()
        self.file_process()

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
                    line = self.queue.get_nowait()
                    register = line.split(";")
                    if register[0].isnumeric():
                        customer_service = CustomerServiceModel().load_by_file(*register)
                        self.repository.add(customer_service)
            except Empty:
                time.sleep(1)
                continue

    def start_threads(self):
        for i in range(100):
            thread = Thread(target=self.listen_queue, daemon=True)
            thread.start()


            
        