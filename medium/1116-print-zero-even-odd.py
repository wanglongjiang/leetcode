'''
打印零与奇偶数
假设有这么一个类：

class ZeroEvenOdd {
  public ZeroEvenOdd(int n) { ... }      // 构造函数
  public void zero(printNumber) { ... }  // 仅打印出 0
  public void even(printNumber) { ... }  // 仅打印出 偶数
  public void odd(printNumber) { ... }   // 仅打印出 奇数
}
相同的一个 ZeroEvenOdd 类实例将会传递给三个不同的线程：

线程 A 将调用 zero()，它只输出 0 。
线程 B 将调用 even()，它只输出偶数。
线程 C 将调用 odd()，它只输出奇数。
每个线程都有一个 printNumber 方法来输出一个整数。请修改给出的代码以输出整数序列 010203040506... ，其中序列的长度必须为 2n。

 

示例 1：

输入：n = 2
输出："0102"
说明：三条线程异步执行，其中一个调用 zero()，另一个线程调用 even()，最后一个线程调用odd()。正确的输出为 "0102"。
示例 2：

输入：n = 5
输出："0102030405"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/print-zero-even-odd
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import threading
'''
思路：多线程
使用锁进行同步。
当执行printNumber之前上锁，执行完成后释放锁

'''


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.lock0 = threading.Lock()
        self.lock2 = threading.Lock()
        self.lock1 = threading.Lock()
        self.lock2.acquire()
        self.lock1.acquire()

    def zero(self, printNumber=print) -> None:
        for i in range(1, self.n + 1):
            self.lock0.acquire()
            printNumber(0)
            if i % 2:
                self.lock1.release()
            else:
                self.lock2.release()

    def even(self, printNumber=print) -> None:
        for i in range(1, self.n + 1):
            if i % 2 == 0:
                self.lock2.acquire()
                printNumber(i)
                self.lock0.release()

    def odd(self, printNumber=print) -> None:
        for i in range(1, self.n + 1):
            if i % 2:
                self.lock1.acquire()
                printNumber(i)
                self.lock0.release()


s = ZeroEvenOdd(200)
t1 = threading.Thread(target=s.zero)
t2 = threading.Thread(target=s.even)
t3 = threading.Thread(target=s.odd)
t1.start()
t2.start()
t3.start()
