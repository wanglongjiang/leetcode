'''
1976. 到达目的地的方案数
你在一个城市里，城市由 n 个路口组成，路口编号为 0 到 n - 1 ，某些路口之间有 双向 道路。
输入保证你可以从任意路口出发到达其他任意路口，且任意两个路口之间最多有一条路。

给你一个整数 n 和二维整数数组 roads ，其中 roads[i] = [ui, vi, timei] 表示在路口 ui 和 vi 之间有一条需要花费 timei 时间才能通过的道路。
你想知道花费 最少时间 从路口 0 出发到达路口 n - 1 的方案数。

请返回花费 最少时间 到达目的地的 路径数目 。由于答案可能很大，将结果对 109 + 7 取余 后返回。

 

示例 1：


输入：n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
输出：4
解释：从路口 0 出发到路口 6 花费的最少时间是 7 分钟。
四条花费 7 分钟的路径分别为：
- 0 ➝ 6
- 0 ➝ 4 ➝ 6
- 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
- 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6
示例 2：

输入：n = 2, roads = [[1,0,10]]
输出：1
解释：只有一条从路口 0 到路口 1 的路，花费 10 分钟。
 

提示：

1 <= n <= 200
n - 1 <= roads.length <= n * (n - 1) / 2
roads[i].length == 3
0 <= ui, vi <= n - 1
1 <= timei <= 109
ui != vi
任意两个路口之间至多有一条路。
从任意路口出发，你能够到达其他任意路口。
'''
import heapq
from math import inf
from typing import List
'''
思路：Dijkstra
调用2次Dijkstra，
第1次使用Dijkstra，找到从0节点到达各节点的最短时间，并保存到数组dist[n]中。
设一个数组ans，保存只用最短时间，从0节点到达该节点的方案数
第2次，使用Dijkstra，只有处于最短时间上的路径才更新ans数组，同时每个节点只进入队列一次（因为该节点在出队列前，它的所有前置节点肯定会先出队列，并更新好自身的方案数）

时间复杂度：O(n^2)
空间复杂度：O(n^2)
'''


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        m = 10**9 + 7
        g = [[] for _ in range(n)]  # 存储边的邻接表
        d = [[0] * n for _ in range(n)]  # 存储距离的矩阵
        for road in roads:
            g[road[0]].append(road[1])
            g[road[1]].append(road[0])
            d[road[0]][road[1]] = road[2]
            d[road[1]][road[0]] = road[2]
        # 用Dijkstra进行遍历
        heap = [(0, 0)]  # 堆中每个元素由2元组：（到达时间，节点id，到达该节点方案数）构成
        dist = [inf] * n  # 从0节点到达各节点的时间
        dist[0] = 0
        # 第一次遍历，只更新从0节点到达各节点的最短时间
        while heap:
            time, node = heapq.heappop(heap)
            for nextnode in g[node]:
                if (nexttime := time + d[node][nextnode]) < dist[nextnode]:
                    dist[nextnode] = nexttime  # 更新到达时间
                    heapq.heappush(heap, (nexttime, nextnode))
        # 第二次遍历，更新到达各节点的方案数
        heap = [(0, 0)]  # 堆中每个元素由2元组：（到达时间，节点id）构成
        ans = [0] * n  # 0到达各节点的方案数
        ans[0] = 1
        marked = set()
        marked.add(0)
        while heap:
            time, node = heapq.heappop(heap)
            for nextnode in g[node]:
                if (nexttime := time + d[node][nextnode]) == dist[nextnode]:
                    ans[nextnode] = (ans[node] + ans[nextnode]) % m
                    if nextnode not in marked:  # 每个节点只需要进入队列遍历一次
                        marked.add(nextnode)
                        heapq.heappush(heap, (nexttime, nextnode))
        return ans[-1]


s = Solution()
print(s.countPaths(n=2, roads=[[1, 0, 10]]))
print(s.countPaths(n=7, roads=[[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]))
