'''
2477. 到达首都的最少油耗
中等
19
相关企业
给你一棵 n 个节点的树（一个无向、连通、无环图），每个节点表示一个城市，编号从 0 到 n - 1 ，且恰好有 n - 1 条路。
0 是首都。给你一个二维整数数组 roads ，其中 roads[i] = [ai, bi] ，表示城市 ai 和 bi 之间有一条 双向路 。

每个城市里有一个代表，他们都要去首都参加一个会议。

每座城市里有一辆车。给你一个整数 seats 表示每辆车里面座位的数目。

城市里的代表可以选择乘坐所在城市的车，或者乘坐其他城市的车。相邻城市之间一辆车的油耗是一升汽油。

请你返回到达首都最少需要多少升汽油。

 

示例 1：



输入：roads = [[0,1],[0,2],[0,3]], seats = 5
输出：3
解释：
- 代表 1 直接到达首都，消耗 1 升汽油。
- 代表 2 直接到达首都，消耗 1 升汽油。
- 代表 3 直接到达首都，消耗 1 升汽油。
最少消耗 3 升汽油。
示例 2：



输入：roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2
输出：7
解释：
- 代表 2 到达城市 3 ，消耗 1 升汽油。
- 代表 2 和代表 3 一起到达城市 1 ，消耗 1 升汽油。
- 代表 2 和代表 3 一起到达首都，消耗 1 升汽油。
- 代表 1 直接到达首都，消耗 1 升汽油。
- 代表 5 直接到达首都，消耗 1 升汽油。
- 代表 6 到达城市 4 ，消耗 1 升汽油。
- 代表 4 和代表 6 一起到达首都，消耗 1 升汽油。
最少消耗 7 升汽油。
示例 3：



输入：roads = [], seats = 1
输出：0
解释：没有代表需要从别的城市到达首都。
 

提示：

1 <= n <= 105
roads.length == n - 1
roads[i].length == 2
0 <= ai, bi < n
ai != bi
roads 表示一棵合法的树。
1 <= seats <= 105
'''
from typing import List
'''
[TOC]

# 思路
dfs

# 解题方法
从节点0开始，用DFS遍历所有节点，每个节点会统计子节点数量，从本节点出发，一起向上一节点出发需要的油=(子节点数+1)/seats。
将需要的油的数量和子树的节点数返回给上级。

# 复杂度
- 时间复杂度: 
> $O(n)$ 

- 空间复杂度: 
> $O(h)$
'''


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj = [[] for _ in range(len(roads) + 1)]
        for r in roads:
            adj[r[0]].append(r[1])
            adj[r[1]].append(r[0])

        def dfs(node, parentNode):
            nodeNum, gasoline = 1 if node else 0, 0  # 子树的节点数, 子树需要的汽油数
            for nextnode in adj[node]:
                if nextnode != parentNode:
                    childNum, childGasoline = dfs(nextnode, node)
                    nodeNum += childNum
                    gasoline += childGasoline
            if node:  # 非0节点，需要的汽油数是节点数/seats
                return (nodeNum, gasoline + nodeNum // seats + (1 if nodeNum % seats else 0))
            else:  # 0节点，需要的汽油数是子节点的汽油数和
                return gasoline

        return dfs(0, 0)


s = Solution()
assert s.minimumFuelCost([[0, 1], [0, 2], [1, 3], [1, 4]], 5) == 4
assert s.minimumFuelCost(roads=[[0, 1], [0, 2], [0, 3]], seats=5) == 3
assert s.minimumFuelCost(roads=[[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], seats=2) == 7
assert s.minimumFuelCost(roads=[], seats=1) == 0
