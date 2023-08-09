from collections import Counter
from typing import List
'''
[TOC]

# 思路
滑动窗口

# 解题方法
创建一个滑动窗口，使其包含所有的整数
窗口右边的下标与窗口左边所有下标都可以构成完全子数组

# 复杂度
- 时间复杂度: 
> $O(n)$ 

- 空间复杂度: 
> $O(n)$
'''


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        numSize = len({val for val in nums})
        size = len(nums)
        winNums = Counter()
        i, j = 0, 0
        ans = 0
        while i < size:
            while len(winNums) <= numSize and i < size:
                winNums[nums[i]] += 1
                i += 1
                if len(winNums) == numSize:
                    break
            while j < i and winNums[nums[j]] > 1:
                winNums[nums[j]] -= 1
                j += 1
            ans += j + 1
        return ans


s = Solution()
assert s.countCompleteSubarrays([1, 3, 1, 2, 2]) == 4
assert s.countCompleteSubarrays([5, 5, 5, 5]) == 10
