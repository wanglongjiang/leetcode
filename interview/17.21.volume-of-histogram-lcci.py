'''
面试题 17.21. 直方图的水量
给定一个直方图(也称柱状图)，假设有人从上面源源不断地倒水，最后直方图能存多少水量?直方图的宽度为 1。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的直方图，在这种情况下，可以接 6 个单位的水（蓝色部分表示水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
'''
from typing import List
'''
思路1：双指针
    开始left,right指向2端，
    每次向内移动值较小的指针，如果移动的下一个值小于该值，是洼地，需要累计，如果大于该值没有容积，更新指针
    时间复杂度：O(n)，整个数组遍历1次
    空间复杂度：O(1)

思路2：单调栈
遍历输入，当前元素索引为i
    如果比栈底小，入栈。
    如果不小于栈底，当前元素i与栈底元素会形成洼地，可以容纳雨水，需要将洼地的容积累计起来
        累积方式为：出栈直至栈为空
        每个出栈的元素height[j]，其容积为(栈底的元素高度)*height[j]
        最后将当前元素i入栈
    遍历结束后，如果栈中还有元素（全部小于栈底），依次出栈，
        如果第j个出栈的值>第j-1个出栈的值，会形成洼地，容积需要累计h-height[j]
        否则将h进行更新
时间复杂度：O(n)，整个数组遍历1次，每个元素出入栈1次，O(2n)
空间复杂度：O(n)

与下面题目相同：
- 42.[接雨水](hard/42-trapping-rain-water.py)

'''


class Solution:
    # 思路2，单调栈
    def trap2(self, height: List[int]) -> int:
        n = len(height)
        stack = []
        v = 0
        for i in range(n):
            while stack and height[stack[0]] <= height[i]:
                j = stack.pop()
                if stack:
                    v += height[stack[0]] - height[j]
            stack.append(i)
        if stack:  # 剩余栈不为空，因栈底元素最大，需要合计栈顶与栈顶下面的元素形成的洼地
            h = height[stack.pop()]
        while stack:
            j = stack.pop()
            if h > height[j]:  #
                v += h - height[j]
            else:
                h = height[j]
        return v

    # 思路1，双指针
    def trap(self, height: List[int]) -> int:
        total = 0
        left, right = 0, len(height) - 1
        while right > left:
            h = min(height[left], height[right])
            while height[left] < height[right]:
                if h > height[left + 1]:
                    total += h - height[left + 1]
                else:
                    h = height[left + 1]
                left += 1
            h = min(height[left], height[right])
            while height[left] >= height[right] and left < right:
                if h > height[right - 1]:
                    total += h - height[right - 1]
                else:
                    h = height[right - 1]
                right -= 1
        return total
