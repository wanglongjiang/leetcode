'''
唯一元素的和

给你一个整数数组 nums 。数组中唯一元素是那些只出现 恰好一次 的元素。

请你返回 nums 中唯一元素的 和 。
'''
from typing import List
from collections import Counter
'''
思路：哈希
用哈希表对元素进行计数，然后累计只出现一次的元素

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        total = 0
        for num, count in Counter(nums).items():
            if count == 1:
                total += num
        return total
