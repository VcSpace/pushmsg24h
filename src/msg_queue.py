import time

from multiprocessing import Process, Queue, Pool, Lock

class msg_Queue(object):
    def __init__(self):
        self.queue = Queue()
        self.lock = Lock()
        for num in range(5):
            Process(target=self.worker(), args=()).start()

    def worker(self):
        self.lock.acquire()
        try:
            task = self.queue.get()
            if task is None:
                pass
            print(f"Processing task {task}")
            time.sleep(1)
            self.lock.release()
        except Exception as e:
            print(e)
            self.lock.release()
    def que_push(self):


def producer(queue, pool):
    # 向队列中添加任务
    for i in range(10):
        print(f"Putting task {i} in the queue")
        queue.put(i)
    # 通知所有工作进程结束
    for _ in range(pool._processes):
        queue.put(None)