'''
剑指 Offer 17. 打印从1到最大的n位数

输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:

输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]
 

说明：

用返回一个整数列表来代替打印
n 为正整数
'''
from typing import List
'''
思路：先计算出最大的n位数，然后一个迭代输出1..最大n位数

时间复杂度：O(n)
空间复杂度：O(1)，除返回list,不需要使用额外空间
'''


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return list(range(1, 10**n))
