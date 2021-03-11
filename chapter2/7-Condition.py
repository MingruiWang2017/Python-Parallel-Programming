# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/10 15:10
@ desc: 类producer向缓冲区写入数据，直到缓冲区充满为止；
    只要缓冲区中有数据，类consumer就会从缓冲区接收数据（并将数据从缓冲区清除）。
    类producer会通知consumer缓冲区不为空，同时consumer会告诉producer缓冲区没有满。
"""
from threading import Thread, Condition
import time

items = []
condition = Condition()


class Consumer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def consume(self):
        global condition
        global items

        condition.acquire()
        if len(items) == 0:
            condition.wait()
            print("\033[34;1mConsumer notify: no item to consume\033[0m")
        items.pop()
        print("\033[34;1mConsumer notify: consumed 1 item\033[0m")
        print("\033[34;1mConsumer notify: items to consume are %d \033[0m" % len(items))

        condition.notify()
        condition.release()

    def run(self):
        for i in range(1, 20):
            time.sleep(3)
            self.consume()


class Producer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def produce(self):
        global condition
        global items

        condition.acquire()
        if len(items) == 10:
            condition.wait()
            print("\033[35;1mProducer notify: items producted are %d \033[0m" % len(items))
            print("\033[35;1mProducer notify: stop the production!!\033[0m")
        items.append(1)
        print("\033[35;1mProducer notify: total items producted %d \033[0m" % len(items))
        condition.notify()
        condition.release()

    def run(self):
        for i in range(1, 20):
            time.sleep(1)
            self.produce()


if __name__ == '__main__':
    producer = Producer()
    consumer = Consumer()
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
