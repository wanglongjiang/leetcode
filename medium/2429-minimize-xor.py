'''
2429. 最小 XOR
给你两个正整数 num1 和 num2 ，找出满足下述条件的整数 x ：

x 的置位数和 num2 相同，且
x XOR num1 的值 最小
注意 XOR 是按位异或运算。

返回整数 x 。题目保证，对于生成的测试用例， x 是 唯一确定 的。

整数的 置位数 是其二进制表示中 1 的数目。



示例 1：

输入：num1 = 3, num2 = 5
输出：3
解释：
num1 和 num2 的二进制表示分别是 0011 和 0101 。
整数 3 的置位数与 num2 相同，且 3 XOR 3 = 0 是最小的。
示例 2：

输入：num1 = 1, num2 = 12
输出：3
解释：
num1 和 num2 的二进制表示分别是 0001 和 1100 。
整数 3 的置位数与 num2 相同，且 3 XOR 1 = 2 是最小的。


提示：

1 <= num1, num2 <= 109
'''
'''
思路：位运算
首先统计2个数字中1的位数
如果num1的1与num2中一样多，返回num1，因为num1^num1==0，值最小
如果num1的1比num2中的多，需要消掉num1的低位的1，保证num1高位在异或时被置零
如果num1的1比num2中的少，需要将num2比num1多的1尽量保存在num1的低位的0

时间复杂度：O(logn)
空间复杂度：O(1)
'''


class Solution:

    def minimizeXor(self, num1: int, num2: int) -> int:
        bitcount1, bitcount2 = num1.bit_count(), num2.bit_count()
        if bitcount1 == bitcount2:
            return num1
        if bitcount1 > bitcount2:  # num1中的1比num2的多，需要将num1低位的1消掉
            for _ in range(bitcount1 - bitcount2):
                num1 &= num1 - 1
        else:  # num1中的1比num2的少，需要将num2比num1多的1补到num1的低位
            for _ in range(bitcount2 - bitcount1):
                num1 |= num1 + 1
        return num1


s = Solution()
assert s.minimizeXor(3, 5) == 3
