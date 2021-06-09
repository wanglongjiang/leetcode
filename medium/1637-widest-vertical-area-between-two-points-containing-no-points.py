'''
两点之间不包含任何点的最宽垂直面积
给你 n 个二维平面上的点 points ，其中 points[i] = [xi, yi] ，请你返回两点之间内部不包含任何点的 最宽垂直面积 的宽度。

垂直面积 的定义是固定宽度，而 y 轴上无限延伸的一块区域（也就是高度为无穷大）。 最宽垂直面积 为宽度最大的一个垂直面积。

请注意，垂直区域 边上 的点 不在 区域内。

 

示例 1：

​
输入：points = [[8,7],[9,9],[7,4],[9,7]]
输出：1
解释：红色区域和蓝色区域都是最优区域。
示例 2：

输入：points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
输出：3
 

提示：

n == points.length
2 <= n <= 10^5
points[i].length == 2
0 <= xi, yi <= 10^9
'''
from typing import List
'''
思路:排序
问题实际上是求x轴上最大的间距,可以对points中x坐标进行排序

时间复杂度:O(nlogn)
空间复杂度:O(n)
'''


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xAxis = list(sorted(map(lambda p: p[0], points)))
        ans, pre = 0, xAxis[0]
        for i in range(1, len(xAxis)):
            ans = max(ans, xAxis[i] - pre)
            pre = xAxis[i]
        return ans


s = Solution()
print(s.maxWidthOfVerticalArea([[8, 7], [9, 9], [7, 4], [9, 7]]))
print(s.maxWidthOfVerticalArea([[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]))
