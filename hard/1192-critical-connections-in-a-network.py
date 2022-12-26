'''
1192. 查找集群内的关键连接
困难
218
相关企业
力扣数据中心有 n 台服务器，分别按从 0 到 n-1 的方式进行了编号。它们之间以 服务器到服务器 的形式相互连接组成了一个内部集群，
连接是无向的。用  connections 表示集群网络，connections[i] = [a, b] 表示服务器 a 和 b 之间形成连接。
任何服务器都可以直接或者间接地通过网络到达任何其他服务器。

关键连接 是在该集群中的重要连接，假如我们将它移除，便会导致某些服务器无法访问其他服务器。

请你以任意顺序返回该集群内的所有 关键连接 。

 

示例 1：



输入：n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
输出：[[1,3]]
解释：[[3,1]] 也是正确的。
示例 2:

输入：n = 2, connections = [[0,1]]
输出：[[0,1]]
 

提示：

2 <= n <= 105
n - 1 <= connections.length <= 105
0 <= ai, bi <= n - 1
ai != bi
不存在重复的连接
'''
from typing import List
'''
[TOC]

# 思路
DFS 之 Tarjan

# 解题方法
> 经典的求桥的问题，可以使用Tarjan算法

# 复杂度
- 时间复杂度: 
> $O(n)$

- 空间复杂度: 
> $O(n)$
'''


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # 遍历connections，得到邻接表
        adj = [[] for _ in range(n)]  # 邻接表
        for e in connections:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        dfn, minAncestors = [-1] * n, [-1] * n  # dfn保存dfs顺序，minAncestors保存子图能够访问的最小祖先

        # 定义tarjan深度搜索函数
        def tarjan(x, father, depth):
            dfn[x], minAncestors[x] = depth, depth
            for next in adj[x]:
                if dfn[next] == -1:  # 是子节点
                    tarjan(next, x, depth + 1)
                    minAncestors[x] = min(minAncestors[x], minAncestors[next])
                elif next != father:  # 是祖先
                    minAncestors[x] = min(minAncestors[x], dfn[next])

        tarjan(0, -1, 0)
        # 查找所有的“桥”
        ans = []
        for i in range(n):
            for j in adj[i]:
                if dfn[i] < minAncestors[j]:  # 这种情况说明j及其子图想要访问i，都需要经过j。i,j是一条关键的边。
                    ans.append([i, j])
        return ans


s = Solution()
print(s.criticalConnections(n=4, connections=[[0, 1], [1, 2], [2, 0], [1, 3]]))
print(s.criticalConnections(n=2, connections=[[0, 1]]))
