'''
2的幂
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
'''
'''
思路：2的幂次方肯定二进制数里面只有1个1。判断这个数是否只有1个1就可以。
小技巧：n&(n-1)可以直接删除最右边的1
时间复杂度：O(1)

'''


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0


s = Solution()
print(s.isPowerOfTwo(1))
print(s.isPowerOfTwo(16))
print(s.isPowerOfTwo(218))
