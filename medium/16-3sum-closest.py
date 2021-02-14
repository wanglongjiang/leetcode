'''
最接近的三数之和
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

'''

from typing import List


# 解题思路：暴力破解法
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = nums[0] + nums[1] + nums[2]
        diff = abs(closest - target)
        numsLen = len(nums)
        nums.sort()
        for left in range(numsLen - 2):
            if left > 0 and nums[left] == nums[left - 1]:
                continue
            need = target - nums[left]
            for mid in range(left + 1, numsLen - 1):
                if mid > left + 1 and nums[mid] == nums[mid - 1]:
                    continue
                for right in range(mid + 1, numsLen):
                    if right > mid + 1 and nums[right] == nums[right - 1]:
                        continue
                    if nums[mid] + nums[right] - need == 0:
                        return target
                    if abs(diff) > abs(nums[mid] + nums[right] - need):
                        closest = nums[left] + nums[mid] + nums[right]
                        diff = abs(closest - target)
        return closest


s = Solution()
print(s.threeSumClosest([1, 1, 1, 0], -100))
print(s.threeSumClosest([-1, 2, 1, -4], 1))
