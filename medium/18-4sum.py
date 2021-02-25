'''
四数之和
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

'''
from typing import List
'''
解题思路：双指针法
设置4个指针，逐步向内搜索可能的解
时间复杂度：O(n^3)
空间复杂度：O(1)
'''


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        for left in range(n - 3):
            if left > 0 and nums[left] == nums[left - 1]:
                continue
            for right in range(n - 1, left + 2, -1):
                if right < n - 1 and nums[right] == nums[right + 1]:
                    continue
                t = target - (nums[left] + nums[right])
                midRight = right - 1
                for midLeft in range(left + 1, midRight):
                    if midLeft > left + 1 and nums[midLeft] == nums[midLeft - 1]:
                        continue
                    while midLeft < midRight and nums[midLeft] + nums[midRight] > t:
                        midRight -= 1
                    if midLeft == midRight:
                        break
                    if nums[midLeft] + nums[midRight] == t:
                        ans.append([nums[left], nums[midLeft], nums[midRight], nums[right]])
        return ans


s = Solution()
print(s.fourSum([0, 0, 0, 0], 1))
print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
