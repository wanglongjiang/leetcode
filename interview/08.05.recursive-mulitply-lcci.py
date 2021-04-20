'''
面试题 08.05. 递归乘法

递归乘法。 写一个递归函数，不使用 * 运算符， 实现两个正整数的相乘。可以使用加号、减号、位移，但要吝啬一些。
'''
'''
思路：位运算
一个a与2的n次幂相乘可以认为是向左移位n，任意一个整数b可以分解为诺干2的幂的和，根据乘法结合律
a*b=a*(2^i+2^j+..)=a<<i+a<<j+a<<...
时间复杂度：O(logb)
空间复杂度：O(logb)，递归深度
'''


class Solution:
    def multiply(self, A: int, B: int) -> int:
        if A > B:  # 将B交换为较小的，减少递归深度
            A, B = B, A

        def mul(a, b):
            if b > 0:
                return a + mul(a << 1, b >> 1) if (b & 1) else mul(a << 1, b >> 1)
            else:
                return 0

        return mul(A, B)


s = Solution()
print(s.multiply(A=1, B=10))
print(s.multiply(A=3, B=4))
