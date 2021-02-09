'''
给你一个 32 位的有符号整数 x ，返回 x 中每位上的数字反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−2^31,  2^31 − 1] ，就返回 0。

'''


class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        neg = False
        maxInt = (2**31 - 1) / 10
        if x < 0:
            neg = True
            x = -x
        while x != 0:
            r = x % 10
            x //= 10
            if result > maxInt or (result == maxInt and r > 7):
                return 0
            result = result * 10 + r
        return -result if neg else result


s = Solution()
print(s.reverse(123))
print(s.reverse(1230))
print(s.reverse(-4560))
print(s.reverse(0))
print(s.reverse(1534236469))
