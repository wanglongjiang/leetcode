'''
2316. 统计无向图中无法互相到达点对数
给你一个整数 n ，表示一张 无向图 中有 n 个节点，编号为 0 到 n - 1 。同时给你一个二维整数数组 edges ，
其中 edges[i] = [ai, bi] 表示节点 ai 和 bi 之间有一条 无向 边。

请你返回 无法互相到达 的不同 点对数目 。

 

示例 1：



输入：n = 3, edges = [[0,1],[0,2],[1,2]]
输出：0
解释：所有点都能互相到达，意味着没有点对无法互相到达，所以我们返回 0 。
示例 2：



输入：n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
输出：14
解释：总共有 14 个点对互相无法到达：
[[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]]
所以我们返回 14 。
 

提示：

1 <= n <= 105
0 <= edges.length <= 2 * 105
edges[i].length == 2
0 <= ai, bi < n
ai != bi
不会有重复边。
'''
from functools import reduce
from typing import Counter, List
'''
思路：并查集
1、用并查集将节点分成若干集合
2、统计各个集合的大小
3、任意2个集合大小的乘积即为这2个集合中不能互相到达的点对数量。

时间复杂度：O(n)
空间复杂度：O(n)
'''


# 并查集套路
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        rooti = self.find(i)
        rootj = self.find(j)
        if rooti != rootj:
            if rooti > rootj:
                rooti, rootj = rootj, rooti
            self.parent[rootj] = rooti


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for e in edges:
            uf.union(e[0], e[1])
        count = Counter(uf.find(i) for i in range(n))  # 统计各个集合的大小
        return sum(size * (n - size) for size in count.values()) // 2  # 计算所有任意2个集合大小的乘积


s = Solution()
print(s.countPairs(n=7, edges=[[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]))
print(s.countPairs(n=3, edges=[[0, 1], [0, 2], [1, 2]]))
