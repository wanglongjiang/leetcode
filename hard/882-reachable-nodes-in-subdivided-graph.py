'''
882. 细分图中的可到达节点
困难
72
相关企业
给你一个无向图（原始图），图中有 n 个节点，编号从 0 到 n - 1 。你决定将图中的每条边 细分 为一条节点链，每条边之间的新节点数各不相同。

图用由边组成的二维数组 edges 表示，其中 edges[i] = [ui, vi, cnti] 表示原始图中节点 ui 和 vi 之间存在一条边，cnti 是将边 细分 后的新节点总数。注意，cnti == 0 表示边不可细分。

要 细分 边 [ui, vi] ，需要将其替换为 (cnti + 1) 条新边，和 cnti 个新节点。新节点为 x1, x2, ..., xcnti ，新边为 [ui, x1], [x1, x2], [x2, x3], ..., [xcnti+1, xcnti], [xcnti, vi] 。

现在得到一个 新的细分图 ，请你计算从节点 0 出发，可以到达多少个节点？如果节点间距离是 maxMoves 或更少，则视为 可以到达 。

给你原始图和 maxMoves ，返回 新的细分图中从节点 0 出发 可到达的节点数 。

 

示例 1：


输入：edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3
输出：13
解释：边的细分情况如上图所示。
可以到达的节点已经用黄色标注出来。
示例 2：

输入：edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], maxMoves = 10, n = 4
输出：23
示例 3：

输入：edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], maxMoves = 17, n = 5
输出：1
解释：节点 0 与图的其余部分没有连通，所以只有节点 0 可以到达。
 

提示：

0 <= edges.length <= min(n * (n - 1) / 2, 104)
edges[i].length == 3
0 <= ui < vi < n
图中 不存在平行边
0 <= cnti <= 104
0 <= maxMoves <= 109
1 <= n <= 3000
'''
from collections import defaultdict
from heapq import heappush
import heapq
from typing import List
'''
[TOC]

# 思路
Dijkstra

# 解题方法
- 首先将edges转为邻接表
- 从节点0出发，用Dijkstra遍历路径，直至所有节点都被遍历，或者到达maxMoves


根据上面的性质，可以用二分查找。

# 复杂度
- 时间复杂度: 
> $O(n^2)$ 

- 空间复杂度: 
> $O(1)$
'''


class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        adList = defaultdict(list)
        for u, v, nodes in edges:
            adList[u].append([v, nodes])
            adList[v].append([u, nodes])
        used = {}
        visited = set()
        reachableNodes = 0
        pq = [[0, 0]]

        while pq and pq[0][0] <= maxMoves:
            step, u = heapq.heappop(pq)
            if u in visited:
                continue
            visited.add(u)
            reachableNodes += 1
            for v, nodes in adList[u]:
                if nodes + step + 1 <= maxMoves and v not in visited:
                    heappush(pq, [nodes + step + 1, v])
                used[(u, v)] = min(nodes, maxMoves - step)

        for u, v, nodes in edges:
            reachableNodes += min(nodes, used.get((u, v), 0) + used.get((v, u), 0))
        return reachableNodes


s = Solution()
assert s.reachableNodes(edges=[[0, 1, 10], [0, 2, 1], [1, 2, 2]], maxMoves=6, n=3) == 13
assert s.reachableNodes(edges=[[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]], maxMoves=10, n=4) == 23
assert s.reachableNodes(edges=[[1, 2, 4], [1, 4, 5], [1, 3, 1], [2, 3, 4], [3, 4, 5]], maxMoves=17, n=5)
