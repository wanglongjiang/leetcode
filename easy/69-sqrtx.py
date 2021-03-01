'''
 x 的平方根
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
'''
'''
解题思路：设置一个精度、和初始答案，通过将初始答案一直应用收敛函数得到接近平方根的数值
'''


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        guess = x / 2
        accuracy = 0.01
        div = x / guess
        while abs(div - guess) > accuracy:
            guess = (div + guess) / 2
            div = x / guess
        return int(guess)


s = Solution()
print(s.mySqrt(1))
print(s.mySqrt(2))
print(s.mySqrt(3))
print(s.mySqrt(4))
print(s.mySqrt(6))
print(s.mySqrt(7))
print(s.mySqrt(8))
print(s.mySqrt(9))
print(s.mySqrt(16))
print(s.mySqrt(49))
print(s.mySqrt(81))
print(s.mySqrt(10000000))
