'''
交替打印FooBar

我们提供一个类：

class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}
两个不同的线程将会共用一个 FooBar 实例。其中一个线程将会调用 foo() 方法，另一个线程将会调用 bar() 方法。

请设计修改程序，以确保 "foobar" 被输出 n 次。

 

示例 1:

输入: n = 1
输出: "foobar"
解释: 这里有两个线程被异步启动。其中一个调用 foo() 方法, 另一个调用 bar() 方法，"foobar" 将被输出一次。
示例 2:

输入: n = 2
输出: "foobarfoobar"
解释: "foobar" 将被输出两次。
'''
import threading
from threading import Condition
'''
思路：多线程
设置一个计数器，值为2*n，当数值大于0，为偶数时，打印foo，为奇数时打印bar
使用锁进行同步
'''


class FooBar:
    def __init__(self, n):
        self.n = n * 2
        self.lock = Condition()

    def foo(self, printFoo) -> None:
        if self.lock.acquire():
            while self.n > 0:
                if self.n % 2 == 0:
                    printFoo()
                    self.n -= 1
                self.lock.notify()
                if self.n > 0:
                    self.lock.wait()
                else:
                    self.lock.release()

    def bar(self, printBar) -> None:
        if self.lock.acquire():
            while self.n > 0:
                if self.n % 2 == 1:
                    printBar()
                    self.n -= 1
                self.lock.notify()
                if self.n > 1:
                    self.lock.wait()
                else:
                    self.lock.release()


f = FooBar(10)
t1 = threading.Thread(target=f.foo)
t2 = threading.Thread(target=f.bar)
t1.start()
t2.start()
