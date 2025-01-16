# import asyncio
# import aiofiles
# from werkzeug.datastructures import FileStorage
# from asyncio import Queue

# class AsyncFileHandler:
#     def __init__(self, file: FileStorage, queue: Queue):
#         self.file = file
#         self.queue = queue
#         self.lock = asyncio.Lock()

#     async def file_process(self):
#         async with aiofiles.open(self.file.stream.read().decode("utf-8"), mode='r') as f:
#             async for line in f:
#                 await self.queue.put(line.strip())

#     async def listen_queue(self):
#         while True:
#             async with self.lock:
#                 try:
#                     line = self.queue.get_nowait()
#                     print(line)
#                 except asyncio.QueueEmpty:
#                     await asyncio.sleep(1)

#     async def start_tasks(self):
#         tasks = []
#         for i in range(50):
#             task = asyncio.create_task(self.listen_queue())
#             tasks.append(task)
#         await self.file_process()
#         await asyncio.gather(*tasks)

# # Exemplo de uso
# # file = FileStorage(stream=open('path_to_your_file.csv', 'rb'))
# # queue = Queue()
# # handler = AsyncFileHandler(file, queue)
