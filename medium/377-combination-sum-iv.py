'''
组合总和 Ⅳ
给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。

题目数据保证答案符合 32 位整数范围。

提示：
1 <= nums.length <= 200
1 <= nums[i] <= 1000
nums 中的所有元素 互不相同
1 <= target <= 1000
'''
from typing import List
'''
思路：回溯
1、数组排序
2、回溯函数每层依次减去一个数，如果大于0，继续回溯，如果=0，有合法的解，如果>0，结束当前回溯
'''


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        mem = {}

        def backtrack(target):
            if target in mem:
                return mem[target]
            ans = 0
            for i in range(n):
                if nums[i] < target:
                    ans += backtrack(target - nums[i])
                elif nums[i] == target:
                    ans += 1
                else:
                    break
            mem[target] = ans
            return ans

        return backtrack(target)


s = Solution()
print(s.combinationSum4(nums=[1, 2, 3], target=4))
print(s.combinationSum4(nums=[9], target=3))
