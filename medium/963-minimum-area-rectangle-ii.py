'''
963. 最小面积矩形 II
中等
65
相关企业
给定在 xy 平面上的一组点，确定由这些点组成的任何矩形的最小面积，其中矩形的边不一定平行于 x 轴和 y 轴。

如果没有任何矩形，就返回 0。

 

示例 1：



输入：[[1,2],[2,1],[1,0],[0,1]]
输出：2.00000
解释：最小面积的矩形出现在 [1,2],[2,1],[1,0],[0,1] 处，面积为 2。
示例 2：



输入：[[0,1],[2,1],[1,1],[1,0],[2,0]]
输出：1.00000
解释：最小面积的矩形出现在 [1,0],[1,1],[2,1],[2,0] 处，面积为 1。
示例 3：



输入：[[0,3],[1,2],[3,1],[1,3],[2,1]]
输出：0
解释：没法从这些点中组成任何矩形。
示例 4：



输入：[[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
输出：2.00000
解释：最小面积的矩形出现在 [2,1],[2,3],[3,3],[3,1] 处，面积为 2。
 

提示：

1 <= points.length <= 50
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
所有的点都是不同的。
与真实值误差不超过 10^-5 的答案将视为正确结果。
'''
from math import inf
from typing import List
'''
[TOC]

# 思路
哈希表 几何

# 解题方法
首先，将所有的点加入哈希表；

然后，用一个三重循环，先检测3个点是否构成一个直角，然后在哈希表中检测是否存在第4个点，如果是，计算该矩形面积


# 复杂度
- 时间复杂度: 
> $O(n^3)$ 

- 空间复杂度: 
> $O(n)$
'''


class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        allpoint = set((x, y) for x, y in points)
        ans = inf

        # 求斜率
        def slope(p1, p2):
            if p1[0] == p2[0]:
                return 0
            return (p1[1] - p2[1]) / (p1[0] - p2[0])

        # 求直角三角角形补全成为矩形的面积，如果不是直角三角形，返回0
        def rect(p1, p2, p3):
            p1p2 = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2  # 计算p1、p2形成的边的长度平方
            p1p3 = (p1[0] - p3[0])**2 + (p1[1] - p3[1])**2  # 计算p1、p3形成的边的长度平方
            p2p3 = (p2[0] - p3[0])**2 + (p2[1] - p3[1])**2  # 计算p2、p3形成的边的长度平方
            area = 0
            x, y = 0, 0  # 该点为矩形第4个点
            if p1p2 + p1p3 == p2p3:  # 根据勾股定理，2条直边的平方和等于斜边平方和，以p1为直角顶点
                area = p1p2**0.5 * p1p3**0.5
                x, y = p2[0] + p3[0] - p1[0], p2[1] + p3[1] - p1[1]
            elif p1p2 + p2p3 == p1p3:  # 以p2为直角顶点
                area = p1p2**0.5 * p2p3**0.5
                x, y = p1[0] + p3[0] - p1[0], p1[1] + p3[1] - p1[1]
            elif p1p3 + p2p3 == p1p2:  # 以p3为直角顶点
                area = p1p3**0.5 * p2p3**0.5
                x, y = p1[0] + p2[0] - p3[0], p1[1] + p2[1] - p3[1]
            if (x, y) not in allpoint or [x, y] == p1 or [x, y] == p2 or [x, y] == p3:
                return 0
            return area

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    if slope(points[i], points[j]) == slope(points[j], points[k]):  # 3点斜率相同，在一条直线上
                        break
                    area = rect(points[i], points[j], points[k])
                    if area > 0:
                        ans = min(ans, area)
        return ans if ans != inf else 0


s = Solution()
assert s.minAreaFreeRect([[3, 0], [0, 1], [1, 0], [3, 3], [2, 3], [0, 2], [2, 1]]) == 0
assert s.minAreaFreeRect([[3, 1], [1, 1], [0, 1], [2, 1], [3, 3], [3, 2], [0, 2], [2, 3]]) - 2 <= 10**-5
assert s.minAreaFreeRect([[1, 2], [2, 1], [1, 0], [0, 1]]) - 2 <= 10**-5
assert s.minAreaFreeRect([[0, 1], [2, 1], [1, 1], [1, 0], [2, 0]]) - 1 <= 10**-5
assert s.minAreaFreeRect([[0, 3], [1, 2], [3, 1], [1, 3], [2, 1]]) == 0
