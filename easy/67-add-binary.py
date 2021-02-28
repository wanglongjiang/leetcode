'''
二进制求和
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。
'''
'''
思路：
从右往左遍历2个字符串，做加法，进位
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        longStr, shortStr = None, None
        if len(a) > len(b):
            longStr = list(a[i] for i in range(len(a)))
            shortStr = b
        else:
            longStr = list(b[i] for i in range(len(b)))
            shortStr = a
        n = len(longStr)
        m = len(shortStr)
        carry = 0
        for i in range(n):
            if i < m:
                carry += int(shortStr[m - i - 1])
            if carry == 0 and i >= m:
                break
            carry += int(longStr[n - i - 1])
            carry, remainder = divmod(carry, 2)
            longStr[n - i - 1] = str(remainder)
        if carry > 0:
            return '1' + ''.join(longStr)
        else:
            return ''.join(longStr)


s = Solution()
print(s.addBinary("11111", "1"))
print(s.addBinary("11", "1"))
print(s.addBinary("1010", "1011"))
