'''
跳跃游戏 II
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

'''
from typing import List
'''
思路：动态规划+滑动窗口
该题目具有最优子结构：
第0个跳跃次数jumpNum[0] = 0
第i个跳跃次数jumpNum[i] = min(jumpNum[j] 满足 j<i,nums[j]+j>= i)
求解min(jumpNum[j] 满足 j<i,nums[j]+j>= i)，
需要维护left指针，使nums[left]+left>=i，满足该条件的jumpNum[left]肯定小于jumNum[left+xxx]
    如果不满足该条件，需要使left指针右移，直至满足该条件
left指针初始值为0
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumpNums = [0] * n
        left = 0
        for i in range(1, n):
            while nums[left] + left < i:
                left += 1
            jumpNums[i] = jumpNums[left] + 1
        return jumpNums[n - 1]


s = Solution()
print(s.jump([3, 2, 1]))
print(s.jump([2, 3, 1, 1, 4]))
print(s.jump([0]))
