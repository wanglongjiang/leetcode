'''
面试题 05.06. 整数转换
整数转换。编写一个函数，确定需要改变几个位才能将整数A转成整数B。

示例1:

 输入：A = 29 （或者0b11101）, B = 15（或者0b01111）
 输出：2
示例2:

 输入：A = 1，B = 2
 输出：2
提示:

A，B范围在[-2147483648, 2147483647]之间
'''
'''
思路：位运算
2个数或运算后，1的个数就是相异的位数

时间复杂度：O(1)
空间复杂度：O(1)
'''


class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        xor = A ^ B
        count = 0
        while xor:
            xor &= xor - 1
            count += 1
        return count


s = Solution()
print(s.convertInteger(1, 2))
