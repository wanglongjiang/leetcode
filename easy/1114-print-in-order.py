'''
按序打印
我们提供了一个类：

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
三个不同的线程 A、B、C 将会共用一个 Foo 实例。

一个将会调用 first() 方法
一个将会调用 second() 方法
还有一个将会调用 third() 方法
请设计修改程序，以确保 second() 方法在 first() 方法之后被执行，third() 方法在 second() 方法之后被执行。

 

示例 1:

输入: [1,2,3]
输出: "firstsecondthird"
解释:
有三个线程会被异步启动。
输入 [1,2,3] 表示线程 A 将会调用 first() 方法，线程 B 将会调用 second() 方法，线程 C 将会调用 third() 方法。
正确的输出是 "firstsecondthird"。
示例 2:

输入: [1,3,2]
输出: "firstsecondthird"
解释:
输入 [1,3,2] 表示线程 A 将会调用 first() 方法，线程 B 将会调用 third() 方法，线程 C 将会调用 second() 方法。
正确的输出是 "firstsecondthird"。
 

提示：

尽管输入中的数字似乎暗示了顺序，但是我们并不保证线程在操作系统中的调度顺序。
你看到的输入格式主要是为了确保测试的全面性。
'''
from threading import RLock
'''
思路：使用锁
使用python中的Rlock，设置一个变量step，first如果要打印，step必须为1，second如果要打印，step必须为2，third如果要打印step必须为0

'''


class Foo:
    def __init__(self):
        self.step = 1
        self.lock = RLock()

    def first(self, printFirst) -> None:
        while self.lock.acquire():
            if self.step == 1:
                printFirst()
                self.step += 1
                self.lock.release()
                break
            self.lock.release()

    def second(self, printSecond) -> None:
        while self.lock.acquire():
            if self.step == 2:
                printSecond()
                self.step += 1
                self.lock.release()
                break
            self.lock.release()

    def third(self, printThird) -> None:
        while self.lock.acquire():
            if self.step == 3:
                printThird()
                self.lock.release()
                break
            self.lock.release()
