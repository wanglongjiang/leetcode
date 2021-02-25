'''
接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

'''

from typing import List
'''
思路：双指针
2端指针，left、right从外向内找到>0的数，此时内部的高度为h=min(right,left),容积为vol = (right-left-1)*h
left、right指针继续向内移动，
    如果内部num<=h，将其从vol中减去
    如果num>h，指针停止移动，vol减去h
2个指针都停止移动后，vol合计到total里面，重新计算left、right内新的容积
'''


class Solution:
    def trap(self, height: List[int]) -> int:
        h = 0
        total, vol = 0, 0
        left, right = 0, len(height) - 1
        while right >= left:
            while height[left] <= h and left <= right:
                vol -= height[left]
                left += 1
            while height[right] <= h and left <= right:
                vol -= height[right]
                right -= 1
            if left <= right:
                innerVol = (right - left + 1) * h
                vol -= innerVol
            total += vol
            h = min(height[left], height[right])
            vol = (right - left - 1) * h
            right -= 1
            left += 1
        return total


s = Solution()
print(s.trap([1, 0, 5, 0, 5, 0, 1]))
print(s.trap([1, 0, 5, 2, 5, 2, 5, 0, 1]))
print(s.trap([4, 2, 0, 3, 2, 5]))
print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(s.trap([2, 0, 4, 0, 2]))
print(s.trap([2, 4, 2]))
print(s.trap([]))
print(s.trap([2, 3, 4, 5, 6, 3]))
