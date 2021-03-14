'''
位1的个数
编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。
'''
'''
思路：输入的整数右移32位，统计其1的个数
'''


class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        i = 0
        while n != 0 and i < 32:
            cnt += n & 1
            n >>= 1
            i += 1
        return cnt


s = Solution()
print(s.hammingWeight(3))
print(s.hammingWeight(1))
print(s.hammingWeight(0))
print(s.hammingWeight(7))
print(s.hammingWeight(-1))
