'''
跳跃游戏
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。
'''
from typing import List
'''
思路：贪心算法

可以设置1个步长，每前进一步减一，然后与当前元素比较，如果大于当前元素，将步长更新为当前元素，否则不更新
如果步长为0，则无法到达终点
'''


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        step = 1
        for num in nums:
            if step == 0:
                return False
            step -= 1
            if step < num:
                step = num
        return True


s = Solution()
print(s.canJump([0]))
print(s.canJump([2, 3, 1, 1, 4]))
print(s.canJump([3, 2, 1, 0, 4]))
