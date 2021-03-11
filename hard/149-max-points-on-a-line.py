'''
直线上最多的点数
给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。
'''
from typing import List
'''
思路：暴力查找。
    2个点确认一个直线，要判断第3个点在不在这条直线上，可以用斜率公式k=(y1-y2)/(x1-x2) == (y1-y3)/(x1-x3)来对比
    因x1-x2有可能为0，所以可以将公式进行变形，只计算乘法变成判断：(y1-y2)*(x1-x3) == (y1-y3)*(x1-x2)
    暴力查找需要3重循环，将所有3个点的组合找出，判断是否在同一直线上
    时间复杂度：O(n^3)
    空间复杂度：O(1)
'''


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        maxCnt = min(2, n)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                lineCnt = 2
                for k in range(j + 1, n):
                    if (points[i][1] - points[j][1]) * (points[i][0] - points[k][0]) == (points[i][1] - points[k][1]) * (points[i][0] - points[j][0]):
                        lineCnt += 1
                maxCnt = max(maxCnt, lineCnt)
        return maxCnt


s = Solution()
print(s.maxPoints([[1, 1], [2, 2], [3, 3]]))
print(s.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
print(s.maxPoints([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]))
