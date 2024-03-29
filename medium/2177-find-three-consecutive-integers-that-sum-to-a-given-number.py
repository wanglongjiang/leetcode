'''
2177. 找到和为给定整数的三个连续整数
给你一个整数 num ，请你返回三个连续的整数，它们的 和 为 num 。如果 num 无法被表示成三个连续整数的和，请你返回一个 空 数组。

 

示例 1：

输入：num = 33
输出：[10,11,12]
解释：33 可以表示为 10 + 11 + 12 = 33 。
10, 11, 12 是 3 个连续整数，所以返回 [10, 11, 12] 。
示例 2：

输入：num = 4
输出：[]
解释：没有办法将 4 表示成 3 个连续整数的和。
 

提示：

0 <= num <= 1015
'''
from typing import List
'''
思路：简单数学
如果能被3整除，则可以表示为3个连续整数

时间复杂度：O(1)
空间复杂度：O(1)
'''


class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        d, r = divmod(num, 3)
        if r == 0:
            return [d - 1, d, d + 1]
        return []
