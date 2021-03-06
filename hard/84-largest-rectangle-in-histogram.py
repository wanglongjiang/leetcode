'''
柱状图中最大的矩形
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。
'''
from typing import List
'''
思路1，暴力法。2重循环，针对每个元素heights[i]，向前遍历每个元素heights[j]，矩形面积为area = (j-i+1)*min(heights[i]..heights[j])
    时间复杂度为：O(n*n)，超出时间限制
思路2，单调栈。
    迭代heights，对于heights[i]，
        如果比上个元素大，入栈(i,heights[i])。
        否则出栈，直至遇到第1个值小于heights[i]的停止，
            计算出栈的最大矩形面积，第1个出栈的值最大，所以最大矩形面积area= (第1个出栈的索引-最后一个出栈的索引)*最后一个出栈的height
            将当前值与最后一个出索引的索引值入栈，(lastPopIndex,heights[i])
        时间复杂度：迭代heights1次，每个元素最多入栈、出栈1次，所以为：O(n)
        空间复杂度：O(n)，最多所有元素入栈
'''


class Solution:
    # 思路2
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        vstack = []
        istack = []
        for i in range(n):
            if vstack and vstack[-1] > heights[i]:
                endIndex = i
                while vstack and vstack[-1] > heights[i]:
                    height = vstack.pop()
                    beginIndex = istack.pop()
                    maxArea = max(maxArea, (endIndex - beginIndex) * height)
                vstack.append(heights[i])
                istack.append(beginIndex)
            else:
                vstack.append(heights[i])
                istack.append(i)
        if vstack:
            endIndex = n
            while vstack:
                height = vstack.pop()
                beginIndex = istack.pop()
                maxArea = max(maxArea, (endIndex - beginIndex) * height)
        return maxArea

    # 思路1
    def largestRectangleArea1(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        for i in range(n):
            height = heights[i]
            for j in range(i, n):
                height = min(height, heights[j])
                maxArea = max(maxArea, height * (j - i + 1))
        return maxArea


s = Solution()
print(s.largestRectangleArea([5, 4, 1, 2]))
print(s.largestRectangleArea([0, 9]))
print(s.largestRectangleArea([1]))
print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
print(s.largestRectangleArea([2, 1, 5, 6, 2, 3, 1, 1, 1, 1, 1, 1, 1]))
