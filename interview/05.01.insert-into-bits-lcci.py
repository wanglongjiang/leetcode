'''
面试题 05.01. 插入
给定两个整型数字 N 与 M，以及表示比特位置的 i 与 j（i <= j，且从 0 位开始计算）。

编写一种方法，使 M 对应的二进制数字插入 N 对应的二进制数字的第 i ~ j 位区域，不足之处用 0 补齐。具体插入过程如图所示。
题目保证从 i 位到 j 位足以容纳 M， 例如： M = 10011，则 i～j 区域至少可容纳 5 位。

 

示例1:

 输入：N = 1024(10000000000), M = 19(10011), i = 2, j = 6
 输出：N = 1100(10001001100)
示例2:

 输入： N = 0, M = 31(11111), i = 0, j = 4
 输出：N = 31(11111)
'''
'''
思路：位运算
生成i~j位为0的掩码，将N对应的未清零，然后M左移i位，与N进行或操作

时间复杂度：O(1)
空间复杂度：O(1)
'''


class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        mask = 0
        for k in range(i, j + 1):
            mask |= 1 << k
        return N & (~mask) | (M << i)


s = Solution()
print(s.insertBits(N=1024, M=19, i=2, j=6))
print(s.insertBits(N=0, M=31, i=0, j=4))
