'''
颠倒二进制位
颠倒给定的 32 位无符号整数的二进制位。
'''
'''
思路：输入依次右移32次，移出来的位，与左移的结果用或运算拼接到一起
'''


class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans <<= 1
            ans |= n & 0x1
            n >>= 1
        return ans


s = Solution()
print(s.reverseBits(43261596))
print(s.reverseBits(-3))
