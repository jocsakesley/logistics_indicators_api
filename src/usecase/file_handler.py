from multiprocessing import Process
from threading import Thread
import time
import csv
from werkzeug.datastructures import FileStorage
from queue import Queue, Empty

class FileHandler:
    def __init__(self, file: FileStorage):
        self.file: FileStorage = file
        self.queue: Queue
        self.start_threads()
        self.file_process()
     
    def set_queue(self, queue: Queue):
        self.queue = queue

    def file_process(self):
        for line in self.file.stream.read().decode('utf-8').split('\n'):
            
            self.queue.put(csv_line)

    def listen_queue(self, name):
        while True:
            try:
                line = self.queue.get_nowait()
                print(name + "/" + line) 
            except Empty:
                time.sleep(1)
                continue

    def start_threads(self):
        for i in range(100):
            thread = Thread(target=self.listen_queue, args=(f"worker-{i}",), daemon=True)
            thread.start()


            
        