'''
剑指 Offer 10- I. 斐波那契数列
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
提示：

0 <= n <= 100
'''
'''
思路：递归
按照定义写出递归函数
时间复杂度：O(fib(n))

思路：迭代
时间复杂度：O(n)
'''


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        fib, fib1, fib2 = 0, 0, 1
        for i in range(2, n + 1):
            fib = fib1 + fib2
            fib1, fib2 = fib2, fib
        return fib % 1000000007


s = Solution()
print(s.fib(2))
print(s.fib(5))
print(s.fib(37))
