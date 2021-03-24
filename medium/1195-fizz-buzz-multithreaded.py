'''
交替打印字符串
请你实现一个有四个线程的多线程版  FizzBuzz， 同一个 FizzBuzz 实例会被如下四个线程使用：

线程A将调用 fizz() 来判断是否能被 3 整除，如果可以，则输出 fizz。
线程B将调用 buzz() 来判断是否能被 5 整除，如果可以，则输出 buzz。
线程C将调用 fizzbuzz() 来判断是否同时能被 3 和 5 整除，如果可以，则输出 fizzbuzz。
线程D将调用 number() 来实现输出既不能被 3 整除也不能被 5 整除的数字。
'''
'''
思路：使用锁进行同步。对python的多线程机制不熟。
'''


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.count = 1
        import threading
        self.threadLock = threading.Lock()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz) -> None:
        while True:
            self.threadLock.acquire()
            if self.count > self.n:
                self.threadLock.release()
                return
            if self.count <= self.n and self.count % 3 == 0 and self.count % 5 != 0:
                printFizz()
                self.count += 1
            self.threadLock.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz) -> None:
        while True:
            self.threadLock.acquire()
            if self.count > self.n:
                self.threadLock.release()
                return
            if self.count <= self.n and self.count % 5 == 0 and self.count % 3 != 0:
                printBuzz()
                self.count += 1
            self.threadLock.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz) -> None:
        while True:
            self.threadLock.acquire()
            if self.count > self.n:
                self.threadLock.release()
                return
            if self.count <= self.n and self.count % 15 == 0:
                printFizzBuzz()
                self.count += 1
            self.threadLock.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber) -> None:
        while True:
            self.threadLock.acquire()
            if self.count > self.n:
                self.threadLock.release()
                return
            if self.count % 3 != 0 and self.count % 5 != 0:
                printNumber(self.count)
                self.count += 1
            self.threadLock.release()
