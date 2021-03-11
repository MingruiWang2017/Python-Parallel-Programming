# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/10 15:57
@ desc: 使用时间在线程间进行通知，以生产者消费者模型为例
"""
from threading import Thread, Event
import time

items = []
event = Event()


class Consumer(Thread):
    def __init__(self, items, event: Event):
        Thread.__init__(self)
        self.items = items
        self.event = event

    def run(self):
        while True:
            time.sleep(1)
            self.event.wait()  # 设置等待，当标志被set()为True时，继续执行，clear()为False时，则继续等待
            item = self.items.pop()
            print("\033[34;1mConsumer notify: %d popped from list by %s\033[0m" % (item, self.name))


class Producer(Thread):
    def __init__(self, items, event: Event):
        Thread.__init__(self)
        self.items = items
        self.event = event

    def run(self):
        global item
        for i in range(15):
            time.sleep(1)
            item = i
            self.items.append(item)
            print("\033[35;1mProducer notify: item No.%d appended to list by %s\033[0m" % (item, self.name))

            print("\033[35;1mProducer notify: event set by %s\033[0m" % self.name)
            self.event.set()  # 通知wait()的消费者继续执行

            print("\033[35;1mProducer notify: event cleared by %s \033[0m" % self.name)
            self.event.clear()  # 通知消费者继续wait


if __name__ == '__main__':
    t1 = Producer(items, event)
    t2 = Consumer(items, event)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
