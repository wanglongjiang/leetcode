'''
公交路线
给你一个数组 routes ，表示一系列公交线路，其中每个 routes[i] 表示一条公交线路，第 i 辆公交车将会在上面循环行驶。

例如，路线 routes[0] = [1, 5, 7] 表示第 0 辆公交车会一直按序列 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... 这样的车站路线行驶。
现在从 source 车站出发（初始时不在公交车上），要前往 target 车站。 期间仅可乘坐公交车。

求出 最少乘坐的公交车数量 。如果不可能到达终点车站，返回 -1 。

 

示例 1：

输入：routes = [[1,2,7],[3,6,7]], source = 1, target = 6
输出：2
解释：最优策略是先乘坐第一辆公交车到达车站 7 , 然后换乘第二辆公交车到车站 6 。
示例 2：

输入：routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
输出：-1
 

提示：

1 <= routes.length <= 500.
1 <= routes[i].length <= 10^5
routes[i] 中的所有值 互不相同
sum(routes[i].length) <= 10^5
0 <= routes[i][j] < 10^6
0 <= source, target < 10^6
'''
from typing import List
from collections import defaultdict
'''
思路：BFS 哈希
每个公交车为1个节点，2辆公交车之间如果有公共站点，则这2个节点之间有一条边。
算法是：
1. 遍历所有的routes，将公交车之间的边连结起来
2. 从具有source站点的公交车出发，用BFS查找能够到达target站点的公交车的最短路径长度

时间复杂度：O(mn)，n为所有站点的数量，m为所有公交车的数量。最坏情况下是每个公交车都能到达所有站点，这种情况下达到O(mn)
空间复杂度：O(m+n)
'''


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        # 遍历所有的车站，将每个车站能连结的公交车统计出来
        stations = defaultdict(set)
        for i, route in enumerate(routes):
            for station in route:
                stations[station].add(i)
        m = len(routes)
        g = [set() for _ in range(m)]  # 建立图，任意2个公交车如果有相同的站点，则有边
        for station, busIds in stations.items():
            for busId in busIds:
                g[busId].update(busIds)
        # 用BFS查找最少换乘次数
        q, nextq = [], []
        vis = [False] * m
        ans = 1
        q.extend(stations[source])
        while q:
            busId = q.pop()
            if busId in stations[target]:
                return ans
            for nextBus in g[busId]:
                if not vis[nextBus]:
                    vis[nextBus] = True
                    nextq.append(nextBus)
            if not q:
                q, nextq = nextq, q
                ans += 1
        return -1


s = Solution()
print(s.numBusesToDestination(routes=[[1, 2, 7], [3, 6, 7]], source=1, target=6))
print(s.numBusesToDestination(routes=[[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], source=15, target=12))
