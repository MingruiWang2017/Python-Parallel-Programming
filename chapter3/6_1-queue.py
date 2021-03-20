# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/12 17:49
@ desc: 使用队列在进程间通信
"""
import multiprocessing
import time


class Producer(multiprocessing.Process):
    def __init__(self, queue: multiprocessing.Queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(10):
            item = i
            self.queue.put(item)
            print("\033[34;1m Process Producer: item %d appended to queue %s \033[0m"
                  % (item, self.name))
            time.sleep(1)
            print("The size of queue is %d" % self.queue.qsize())


class Consumer(multiprocessing.Process):
    def __init__(self, queue: multiprocessing.Queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if self.queue.empty():
                print("the queue is empty!!!")
                break
            else:
                time.sleep(1)
                item = self.queue.get()
                print("\033[35;1m Process Consumer: item %d popped by %s\033[0m"
                      % (item, self.name))
                time.sleep(1)


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process_producer = Producer(queue)
    process_consumer = Consumer(queue)
    process_producer.start()
    process_consumer.start()
    process_producer.join()
    process_consumer.join()
