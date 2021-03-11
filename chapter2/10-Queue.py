# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/11 9:10
@ desc: 使用队列在线程间共享数据
"""
from threading import Thread, Event
from queue import Queue
import time


class Producer(Thread):
    def __init__(self, queue: Queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(20):
            item = i
            self.queue.put(item)
            print("\033[34;1mProducer notify: item %d appended to queue by %s\033[0m"
                  % (item, self.name))
            if self.queue.full():
                print("\033[34;1mProducer notify: queue is Full：%d !!!\033[0m"
                      % self.queue.qsize())
            time.sleep(0.5)


class Consumer(Thread):
    def __init__(self, queue: Queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            print("\033[35;1mConsumer notify: %d popped from queue by %s\033[0m"
                  % (item, self.name))
            time.sleep(3)
            self.queue.task_done()  # 告诉队列此次get()任务完成了


if __name__ == '__main__':
    queue = Queue(5)  # 设置队列长度为5，如果<=0, 则表示队列长度无限
    t1 = Producer(queue)
    t2 = Consumer(queue)
    t3 = Consumer(queue)
    t4 = Consumer(queue)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
