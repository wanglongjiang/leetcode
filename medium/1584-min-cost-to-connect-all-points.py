'''
连接所有点的最小费用
给你一个points 数组，表示 2D 平面上的一些点，其中 points[i] = [xi, yi] 。

连接点 [xi, yi] 和点 [xj, yj] 的费用为它们之间的 曼哈顿距离 ：|xi - xj| + |yi - yj| ，其中 |val| 表示 val 的绝对值。

请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有 一条简单路径时，才认为所有点都已连接。

 

示例 1：



输入：points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
输出：20
解释：

我们可以按照上图所示连接所有点得到最小总费用，总费用为 20 。
注意到任意两个点之间只有唯一一条路径互相到达。
示例 2：

输入：points = [[3,12],[-2,5],[-4,1]]
输出：18
示例 3：

输入：points = [[0,0],[1,1],[1,0],[-1,1]]
输出：4
示例 4：

输入：points = [[-1000000,-1000000],[1000000,1000000]]
输出：4000000
示例 5：

输入：points = [[0,0]]
输出：0
 

提示：

1 <= points.length <= 1000
-106 <= xi, yi <= 106
所有点 (xi, yi) 两两不同。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-cost-to-connect-all-points
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
import heapq
'''
思路：最小生成树 堆
用最小生成树的Kruskal算法。
1. 遍历任意2个顶点间的边，加入最小堆heap
1. 依次从最小堆中取出成本最小的边，加入并查集，累计成本

时间复杂度：O(n^2log(n^2))
空间复杂度：O(n^2)
'''


# 定义并查集
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        rooti = self.find(i)
        rootj = self.find(j)
        if rooti != rootj:
            if rooti > rootj:  # 确保较小的作为根节点
                rooti, rootj = rootj, rooti
                i, j = j, i
            self.parent[rootj] = rooti


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        # 将任意2个顶点之间的边加入最小堆
        heap = []
        for i in range(n):
            for j in range(i + 1, n):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(heap, (cost, i, j))
        # 依次取出权重最小的边，加入并查集
        unionFind = UnionFind(n * n)
        ans = 0
        while heap:
            cost, i, j = heapq.heappop(heap)
            if unionFind.find(i) != unionFind.find(j):  # 如果2个顶点不在一颗树中，进行连结
                unionFind.union(i, j)
                ans += cost
        return ans


s = Solution()
print(s.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
print(s.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]))
print(s.minCostConnectPoints([[0, 0], [1, 1], [1, 0], [-1, 1]]))
print(s.minCostConnectPoints([[-1000000, -1000000], [1000000, 1000000]]))
print(s.minCostConnectPoints([[0, 0]]))
