'''
最小面积矩形

给定在 xy 平面上的一组点，确定由这些点组成的矩形的最小面积，其中矩形的边平行于 x 轴和 y 轴。

如果没有任何矩形，就返回 0。

 

示例 1：

输入：[[1,1],[1,3],[3,1],[3,3],[2,2]]
输出：4
示例 2：

输入：[[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
输出：2
 

提示：

1 <= points.length <= 500
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
所有的点都是不同的。
'''
from typing import List
'''
思路：哈希
1. 将所有坐标加入哈希表
2. 组合任意2个点尝试构成矩形，矩形面积如果小于最小矩形，在哈希表中查找另外2个点是否存在，如果存在，更新最小矩形面积

时间复杂度：O(n^2)
空间复杂度：O(n)
'''


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        hashset = set(map(lambda p: (p[0], p[1]), points))
        n = len(points)
        minArea = float('inf')
        for i in range(n - 1):
            for j in range(i + 1, n):
                p1, p2 = points[i], points[j]
                if p1[0] == p2[0] or p1[1] == p2[1]:
                    continue
                area = abs(p1[0] - p2[0]) * abs(p1[1] - p2[1])
                if area < minArea:
                    if p1[0] > p2[0]:  # 确保p1在左边
                        p1, p2 = p2, p1
                    if p1[1] > p2[1]:  # p1在p2的上面，需要补充leftbottom,righttop
                        leftbottom = (p1[0], p2[1])
                        if leftbottom not in hashset:
                            continue
                        righttop = (p2[0], p1[1])
                        if righttop in hashset:
                            minArea = area
                    else:  # p1在p2的下面，需要补充leftop,rightbottom
                        leftTop = (p1[0], p2[1])
                        if leftTop not in hashset:
                            continue
                        rightbottom = (p2[0], p1[1])
                        if rightbottom in hashset:
                            minArea = area
        return minArea if minArea != float('inf') else 0


s = Solution()
print(s.minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]))
print(s.minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]))
print(s.minAreaRect([[3, 2], [3, 1], [4, 4], [1, 1], [4, 3], [0, 3], [0, 2], [4, 0]]))
