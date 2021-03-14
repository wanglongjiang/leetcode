'''
快乐数
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：

对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果 可以变为  1，那么这个数就是快乐数。
如果 n 是快乐数就返回 true ；不是，则返回 false 。
'''
'''
没啥思路，按照题目的算法写出来，如果循环1000次还未变成0，就认为不是快乐数。。。
'''


class Solution:
    def isHappy(self, n: int) -> bool:
        def f(n):
            s = 0
            while n > 0:
                m = n % 10
                m *= m
                s += m
                n //= 10
            return s

        for i in range(1000):
            if n == 1:
                return True
            n = f(n)
        return False


s = Solution()
print(s.isHappy(19))
print(s.isHappy(19))
print(s.isHappy(2))
