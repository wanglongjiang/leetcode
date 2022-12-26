'''
280. 摆动排序
给你一个无序的数组 nums, 将该数字 原地 重排后使得 nums[0] <= nums[1] >= nums[2] <= nums[3]...。

示例:

输入: nums = [3,5,2,1,6,4]
输出: 一个可能的解答是 [3,5,1,6,2,4]
'''
from typing import List
'''
思路：一次遍历
遍历nums，
如果i是偶数下标，需要使nums[i]<=nums[i+1]，如果不满足，交换2个元素。这种交换会不会破坏与nums[i-1]的关系呢，不会，因为nums[i+1]更小，交换后同样满足nums[i-1]>nums[i]。
同理，如果i是奇数下标，需要时nums[i]>=nums[i+1]，如果不满足，交换2个元素。

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        for i in range(len(nums) - 1):
            if (i & 1 == 0 and nums[i] > nums[i + 1]) or (i & 1 and nums[i] < nums[i + 1]):
                nums[i], nums[i + 1], nums[i + 1], nums[i]
