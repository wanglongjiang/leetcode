from collections import Counter
from typing import List
'''
[TOC]

# 思路
滑动窗口、有序集合

# 解题方法
遍历数组，用滑动窗口查找每个不间断子数组，子数组每向右扩大一个元素，形成的子数组数+m（m为当前子数组大小）
需要用哈希表保存滑动窗口中的元素，以确保在扩展、收缩滑动窗口时能取得最大值最小值。因为差最大为2，所以哈希表中最多有3个元素，max和min可以认为是O(1)

# 复杂度
- 时间复杂度: 
> $O(n)$ 

- 空间复杂度: 
> $O(1)$
'''


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        subli = Counter()
        ans = 0
        j, i, n = 0, 0, len(nums)
        while i < n:
            if not subli or (abs(nums[i] - max(subli)) <= 2 and abs(nums[i] - min(subli)) <= 2):  # 加上最新的元素，还是不间断子数组，扩展滑动窗口
                subli[nums[i]] += 1
                ans += i - j + 1
                i += 1
            else:  # 加上最新的元素，不是不间断子数组，缩小滑动窗口
                subli[nums[j]] -= 1
                if subli[nums[j]] == 0:
                    del subli[nums[j]]
                j += 1
        return ans


s = Solution()
assert s.continuousSubarrays([5, 4, 2, 4]) == 8
assert s.continuousSubarrays([1, 2, 3]) == 6
