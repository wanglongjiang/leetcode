'''
数字范围按位与
给你两个整数 left 和 right ，表示区间 [left, right] ，返回此区间内所有数字 按位与 的结果（包含 left 、right 端点）。
'''
'''
思路：暴力与会超时，2个数的差的最高位以下的位肯定会被清零（可以将差从0不停的进位到差，从最高位往下的1，都会被清除）
可以将差的最高位至低位置成0，其他位为1，与left、right与
'''


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        diff = right - left
        mask = 0
        while diff != 0:
            mask <<= 1
            mask |= 1
            diff >>= 1
        mask = ~mask
        return left & right & mask


s = Solution()
print(s.rangeBitwiseAnd(left=5, right=7))
print(s.rangeBitwiseAnd(left=0, right=0))
print(s.rangeBitwiseAnd(left=1, right=2147483647))
