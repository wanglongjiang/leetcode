'''
丑数
给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。

丑数 就是只包含质因数 2、3 和/或 5 的正整数。
'''
'''
思路：将数字除以2、3、5，如果最后能除尽则为丑数
'''


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        # 将2约去
        while n & 1 == 0:
            n >>= 1
        # 将3约去
        while n % 3 == 0:
            n //= 3
        # 将5约去
        while n % 5 == 0:
            n //= 5
        return n == 1


s = Solution()
print(s.isUgly(9))
print(s.isUgly(6))
print(s.isUgly(8))
print(s.isUgly(14))
print(s.isUgly(1))
