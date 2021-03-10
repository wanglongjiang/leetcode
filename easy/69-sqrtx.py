'''
 x 的平方根
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
'''
'''
解题思路1，暴力搜索，使用4则运算，从1开始搜索，直至i*i<=x and (i+1)*(i+1)>x 返回i
时间复杂度：O(求根n)
解题思路2，牛顿法，使用4则运算，每次求guess和x/guess的平均值来渐进
时间复杂度：O(log(n))
'''


class Solution:
    # 思路1
    def mySqrt1(self, x: int) -> int:
        a, b = 0, 0
        while b * b <= x:
            a = b
            b += 1
        return a

    # 思路2
    def mySqrt(self, x: int) -> int:
        guess = x
        while True:
            if guess * guess <= x:
                return guess
            guess = (x // guess + guess) >> 1


s = Solution()
print('sqrt1=%d' % s.mySqrt(1))
print(s.mySqrt(2))
print(s.mySqrt(3))
print(s.mySqrt(4))
print(s.mySqrt(6))
print(s.mySqrt(7))
print(s.mySqrt(8))
print('sqrt9=%d' % s.mySqrt(9))
print(s.mySqrt(16))
print(s.mySqrt(49))
print(s.mySqrt(81))
print(s.mySqrt(10000000))
