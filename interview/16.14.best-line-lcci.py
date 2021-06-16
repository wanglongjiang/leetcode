'''
面试题 16.14. 最佳直线

给定一个二维平面及平面上的 N 个点列表Points，其中第i个点的坐标为Points[i]=[Xi,Yi]。请找出一条直线，其通过的点的数目最多。

设穿过最多点的直线所穿过的全部点编号从小到大排序的列表为S，你仅需返回[S[0],S[1]]作为答案，若有多条直线穿过了相同数量的点，则选择S[0]值较小的直线返回，S[0]相同则选择S[1]值较小的直线返回。

示例：

输入： [[0,0],[1,1],[1,0],[2,0]]
输出： [0,2]
解释： 所求直线穿过的3个点的编号为[0,2,3]
提示：

2 <= len(Points) <= 300
len(Points[i]) = 2
'''
from typing import List
from collections import defaultdict
'''
思路：哈希 数学
任意2点a,b可以构成一条直线，直线的角度由tan=(a.y-b.y)/(a.x-b.x)确定。可以将tan作为key，加入哈希表，经过一点的所有直线拥有相同的角度，最终统计哈希表key的计数最多的即为答案。

时间复杂度：O(n^2)，需要两两组合所有的直线
空间复杂度：O(n^2)
'''


class Solution:
    def bestLine(self, points: List[List[int]]) -> List[int]:
        n = len(points)
        sets = []
        for i in range(n - 1):
            counter = defaultdict(set)
            for j in range(i + 1, n):
                p1, p2 = points[i], points[j]
                if p1[0] < p2[0]:  # 确保x较大的在前面，保证tan的正确
                    p1, p2 = p2, p1
                tan = 'none' if p1[0] == p2[0] else (p1[1] - p2[1]) / (p1[0] - p2[0])
                counter[tan].add(i)
                counter[tan].add(j)
            # 遍历所有角度，找到同角度最大的集合
            for s in counter.values():
                if len(sets) > 0 and len(s) > len(sets[0]):
                    sets.clear()
                if len(sets) == 0 or len(s) > len(sets[0]):
                    sets.append(s)
        # 从所有同长度的点集合中找到最小的2个点
        ans = [float('inf'), float('inf')]
        for s in sets:
            p1, p2 = float('inf'), float('inf')
            for p in s:
                if p1 > p:
                    p2 = p1
                    p1 = p
                elif p2 > p:
                    p2 = p
            if ans[0] > p1 or (ans[0] == p1 and ans[1] > p2):
                ans = [p1, p2]
        return ans


s = Solution()
print(s.bestLine([[0, 0], [1, 1], [1, 0], [2, 0]]))
