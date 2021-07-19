'''
剑指 Offer 65. 不用加减乘除做加法
写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。

 

示例:

输入: a = 1, b = 1
输出: 2
 

提示：

a, b 均可能是负数或 0
结果不会溢出 32 位整数
'''
'''
思路：位运算
andOp = a&b是所有同时为1的位运算结果，如果相加需要进位，结果为向左移位(a&b)<<1
xorOp = a^b是任意1个有1的位运算结果。
递归执行上面运算，直至2者之一为0，返回另外一个数即可

时间复杂度：O(1)
空间复杂度：O(1)
'''


class Solution:
    def add(self, a: int, b: int) -> int:
        andOp, xorOp = (a & b) << 1, a ^ b
        while andOp:
            a, b = andOp, xorOp
            andOp, xorOp = (a & b) << 1, a ^ b
        return xorOp


s = Solution()
print(s.add(3, 4))
print(s.add(3, 99))
print(s.add(5, 8))
print(s.add(-1, -2))
