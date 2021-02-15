'''
给定一个二进制数组， 计算其中最大连续1的个数。
'''
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        count = 0
        for num in nums:
            if num:
                count += 1
            else:
                maxCount = max(count, maxCount)
                count = 0
        return max(count, maxCount)


s = Solution()
print(s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
