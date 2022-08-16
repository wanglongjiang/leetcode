'''
360. 有序转化数组
给你一个已经 排好序 的整数数组 nums 和整数 a、b、c。对于数组中的每一个数 x，计算函数值 f(x) = ax2 + bx + c，请将函数值产生的数组返回。

要注意，返回的这个数组必须按照 升序排列，并且我们所期望的解法时间复杂度为 O(n)。

示例 1：

输入: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
输出: [3,9,15,33]
示例 2：

输入: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
输出: [-23,-5,1,7]
'''
from typing import List
'''
思路：数学 双指针
f(x)的函数曲线根据a、b的调性，有可能是山谷或者山峰形状，
根据前2个函数值判断是山谷或者山峰形状。
如果是山谷，找到最小值索引，然后设2个指针从谷底分别向数组2端移动，比较大小后输出到结果list
如果是山峰，设2个指针从2端向中间移动，比较大小后输出到结果list

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        n = len(nums)
        nums = list(map(lambda x: a * x * x + b * x + c, nums))
        if n == 1:
            return nums
        ans = []
        if nums[0] >= nums[1]:  # 山谷形状
            minIdx = 0
            while minIdx + 1 < n and nums[minIdx] > nums[minIdx + 1]:  # 找到最小值
                minIdx += 1
            left, right = minIdx, minIdx + 1
            while left >= 0 or right < n:  # 双指针从内向外移动
                if right == n or (left >= 0 and nums[left] <= nums[right]):
                    ans.append(nums[left])
                    left -= 1
                else:
                    ans.append(nums[right])
                    right += 1
        else:  # 山峰形状，双指针从外向内移动
            left, right = 0, n - 1
            while left <= right:
                if nums[left] <= nums[right]:
                    ans.append(nums[left])
                    left += 1
                else:
                    ans.append(nums[right])
                    right -= 1
        return ans


s = Solution()
print(s.sortTransformedArray(nums=[-4, -2, 2, 4], a=-1, b=3, c=5))
print(s.sortTransformedArray(nums=[-4, -2, 2, 4], a=1, b=3, c=5))
