'''
盛最多水的容器
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
'''
from typing import List


class Solution:
    '''
    思路：双指针法，初始从左右边界开始算，之后每次都移动数值较小的指针。
    原因：因x<=y，y不论向x靠近多少，最大值都是x*weight
    '''
    def maxArea(self, height: List[int]) -> int:
        mx = 0
        left, right = 0, len(height) - 1
        while left < right:
            mx = max(mx, min(height[left], height[right]) * (right - left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return mx


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49)
print(s.maxArea([1, 1]) == 1)
print(s.maxArea([4, 3, 2, 1, 4]) == 16)
print(s.maxArea([1, 2, 1]) == 2)
