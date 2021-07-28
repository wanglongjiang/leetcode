'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

你可以按任意顺序返回答案。
'''
from typing import List
'''
思路1，暴力循环
时间复杂度：O(n^2)
空间复杂度：O(1)

思路2，哈希
设哈希表ht用于保存nums中的元素。
遍历nums中的元素，
> 如果target-nums[i]在哈希表中，返回。
> 如果不在哈希表中，将nums[i]加入哈希表

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    # 思路2，哈希
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        for i in range(len(nums)):
            if target - nums[i] in ht:
                return [ht.get(target - nums[i]), i]
            ht[nums[i]] = i
        return []

    # 思路1，暴力循环
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] + nums[j] == target:
                    return [j, i]


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([3, 2, 4], 6))
print(s.twoSum([3, 3], 6))
print(s.twoSum([2, 5, 5, 11], 10))
