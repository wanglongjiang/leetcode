'''
唯一元素的和

给你一个整数数组 nums 。数组中唯一元素是那些只出现 恰好一次 的元素。

请你返回 nums 中唯一元素的 和 。
'''
from typing import List
'''
思路：用哈希表存储所有元素
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        allItem = set()
        total = 0
        for num in nums:
            if num not in allItem:
                allItem.add(num)
                total += num
        return num
