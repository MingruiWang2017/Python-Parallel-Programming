# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2021/3/10 14:09
@ desc: Box类拥有add（）与remove（）方法，
    并提供了对execute（）方法的访问。
    这样我们就可以执行添加或者删除条目的动作。
    对execute（）方法的访问是通过RLock（）来管理
"""
import threading
import time


class Box(object):
    # 设置可重入锁，他可以在一个线程中多次被获取，但是获取后必须被释放
    lock = threading.RLock()

    def __init__(self):
        self.total_items = 0

    def execute(self, n):
        Box.lock.acquire()
        self.total_items += n
        Box.lock.release()

    def add(self):
        Box.lock.acquire()
        self.execute(1)  # 调用execute方法，再次获取lock（重入）
        Box.lock.release()

    def remove(self):
        Box.lock.acquire()
        self.execute(-1)  # 调用execute方法，再次获取lock（重入）
        Box.lock.release()


# 将两个方法在单独的线程中运行n次
def adder(box, items):
    while items > 0:
        print("adding 1 item in the box")
        box.add()
        time.sleep(1)
        items -= 1


def remover(box, items):
    while items > 0:
        print("removing 1 item in the box")
        box.remove()
        time.sleep(1)
        items -= 1


# 主程序构建一些线程，并确保可以正常工作
if __name__ == "__main__":
    items = 5
    print("putting %d items in the box " % items)
    box = Box()
    t1 = threading.Thread(target=adder, args=(box, items))
    t2 = threading.Thread(target=remover, args=(box, items))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("%d items still remain in the box" % box.total_items)
