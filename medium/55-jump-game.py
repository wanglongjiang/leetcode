'''
跳跃游戏
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。
'''
from typing import List
'''
思路1，贪心算法

可以设置1个步长，每前进一步减一，然后与当前元素比较，如果大于当前元素，将步长更新为当前元素，否则不更新
如果步长为0，则无法到达终点
时间复杂度：O(n)
空间复杂度：O(1)

思路2，动态规划
设dp[i]为跳到第i个单元格剩余的步数，如果dp[i]为0，则无法到达终点
dp[i]=max(dp[i-1]-1,nums[i])
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    # 动态规划
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if nums[0] == 0 and n != 1:
            return False
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] - 1, nums[i])
            if i != n - 1 and dp[i] == 0:
                return False
        return True

    # 贪心算法
    def canJump1(self, nums: List[int]) -> bool:
        step = 1
        for num in nums:
            if step == 0:
                return False
            step -= 1
            if step < num:
                step = num
        return True


s = Solution()
print(s.canJump([0, 1]))
print(s.canJump([0]))
print(s.canJump([2, 3, 1, 1, 4]))
print(s.canJump([3, 2, 1, 0, 4]))
