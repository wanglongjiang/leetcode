'''
实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。
'''


class Solution:
    def myPow(self, x: float, n: int) -> float:
        neg = n >= 0
        n = abs(n)
        product = 1
        product2n = x
        while n > 0:
            if n & 1 == 1:
                product = product * product2n
            n >>= 1
            product2n *= product2n
        if neg:
            return product
        else:
            return 1 / product


s = Solution()
print(s.myPow(2.0, 10) == 1024.0)
print(s.myPow(2.1, 3) == 9.261)
print(s.myPow(2.0, -2) == 0.25)
