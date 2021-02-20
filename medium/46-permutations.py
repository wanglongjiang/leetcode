'''
全排列
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
'''

from typing import List
'''
解题思路：回溯搜索

'''


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def perm(index):
            if index == len(nums):
                result.append(nums[:])
                return
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                perm(index + 1)
                nums[index], nums[i] = nums[i], nums[index]

        perm(0)
        return result


s = Solution()
print(s.permute([1, 2, 3]))
