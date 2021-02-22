'''
全排列 II

给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
'''
from typing import List
'''
解题思路：回溯搜索，插入结果集之前进行重复判定。
重复判定使用set进行排重
'''


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        unionSet = set()
        nums.sort()

        def perm(index):
            if index == len(nums):
                key = ''.join(map(str, nums))
                if key not in unionSet:
                    unionSet.add(key)
                    result.append(nums[:])
                return
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                perm(index + 1)
                nums[index], nums[i] = nums[i], nums[index]

        perm(0)
        return result


s = Solution()
print(s.permuteUnique([3, 3, 1, 2, 3, 2, 3, 1]))
print(s.permuteUnique([0, 1, 0, 0, 9]))
print(s.permuteUnique([1, 2, 3]))
print(s.permuteUnique([1, 1, 2]))
