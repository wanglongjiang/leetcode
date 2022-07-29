'''
593. 有效的正方形
给定二维空间中四点的坐标，返回四点是否可以构造一个正方形。

一个点的坐标（x，y）由一个有两个整数的整数数组表示。

示例:

输入: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
输出: True


注意:

所有输入整数都在 [-10000，10000] 范围内。
一个有效的正方形有四个等长的正长和四个等角（90度角）。
输入点没有顺序。
'''
from typing import List
'''
思路：几何 数学
4个点构成的4条边长度相同，然后2个点构成的对角线长度相同
任意2个点构成的线段长度为$\\sqrt{(p1[0]-p2[0])^2+(p1[1]-p2[1])^2}$，为了方便计算，不再开平方

时间复杂度：O(1)
空间复杂度：O(1)
'''


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if len(set([tuple(p1), tuple(p2), tuple(p3), tuple(p4)])) < 4:  # 有重合的点，返回false
            return False

        def dis(p1, p2):
            return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

        edges = [dis(p1, p2), dis(p1, p3), dis(p1, p4), dis(p3, p2), dis(p3, p4), dis(p2, p4)]  # 计算4个边和2个对角线长度
        edges.sort()  # 排序，如果是正方形，前4条边长度相同，后面2个是对角线，长度相同
        return edges[0] == edges[1] == edges[2] == edges[3] and edges[4] == edges[5]


s = Solution()
print(s.validSquare(p1=[0, 0], p2=[1, 1], p3=[1, 0], p4=[0, 1]))
