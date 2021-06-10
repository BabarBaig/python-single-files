__author__ = 'Babar_000'

import array

def test1():
    q = my_queue(3)
    if not q.empty():
        print("test1 NOT OK")
        return
    if not q.enqueue(10):
        print("test1 NOT OK")
        return
    if not q.enqueue(11):
        print("test1 NOT OK")
        return
    if 10 != q.dequeue():
        print("test1 NOT OK")
        return
    if 11 != q.dequeue():
        print("test1 NOT OK")
        return
    if not q.empty():
        print("test1 NOT OK")
        return
    print("test1 OK")


def test2():
    q = my_queue(3)
    if q.dequeue():
        print("test2 NOT OK due to None")
        return
    if not q.enqueue(10):
        print("test2 NOT OK")
        return
    if not q.enqueue(11):
        print("test2 NOT OK")
        return
    if not q.enqueue(12):
        print("test2 NOT OK")
        return
    if not q.full():
        print("test2 NOT OK")
        return
    q.enqueue(13)
    if q.tail != 0:
        print("test2 NOT OK")
        return
    print("test2 OK")


def test3():
    q = my_queue(3)
    if not q.empty():
        print("test3 NOT OK")
        return
    if q.dequeue():
        print("test3 NOT OK")
        return
    if not q.enqueue(10):
        print("test3 NOT OK")
        return
    if not q.enqueue(11):
        print("test3 NOT OK")
        return
    if not q.enqueue(12):
        print("test3 NOT OK")
        return
    if 10 != q.dequeue():
        print("test3 NOT OK")
        return
    if 11 != q.dequeue():
        print("test3 NOT OK")
        return
    if 12 != q.dequeue():
        print("test3 NOT OK")
        return
    q.dequeue()
    if q.head != 0:
        print("test3 NOT OK")
        return
    print("test3 OK")


class my_queue:
    def __init__(self, size_max):  # Constructor
        assert size_max > 0
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i', range(size_max))  # integer que is 10x faster

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.max

    def enqueue(self, x):
        if self.size == self.max:
            return False  #Queue is full--can't add any more
        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        if self.tail == self.max:
            self.tail = 0
        return True

    def dequeue(self):
        if self.size == 0:
            return None
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:
            self.head = 0
        return x

    def check_rep(self):
        assert self.size >= 0 and self.size <= self.max
        if self.size == self.max:
            assert self.tail == 0
        return

# -- end --
