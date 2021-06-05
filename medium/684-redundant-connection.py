'''
冗余连接
在本问题中, 树指的是一个连通且无环的无向图。

输入一个图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，
这条附加的边不属于树中已存在的边。

结果图是一个以边组成的二维数组。每一个边的元素是一对[u, v] ，满足 u < v，表示连接顶点u 和v的无向图的边。

返回一条可以删去的边，使得结果图是一个有着N个节点的树。如果有多个答案，则返回二维数组中最后出现的边。答案边 [u, v] 应满足相同的格式 u < v。

示例 1：

输入: [[1,2], [1,3], [2,3]]
输出: [2,3]
解释: 给定的无向图为:
  1
 / \\
2 - 3
示例 2：

输入: [[1,2], [2,3], [3,4], [1,4], [1,5]]
输出: [1,4]
解释: 给定的无向图为:
5 - 1 - 2
    |   |
    4 - 3
注意:

输入的二维数组大小在 3 到 1000。
二维数组中的整数在1到N之间，其中N是输入数组的大小。
'''
from typing import List
'''
思路：并查集
建立一个并查集，对于一个树来说，所有的节点都能通过路径连结到根节点，如果有冗余的边加入，2个节点的根节点不会发生变化
根据上面的思路，写出算法：
1. 建立并查集
2. 遍历所有的边，加入并查集，加入前判断2个节点的根节点是否相同。
> 如果根节点相同，将该边记住
所有的边遍历完成后，最后记住的即为结果

时间复杂度：O(n)
空间复杂度：O(n)
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

    def unite(self, i, j):
        rooti = self.find(i)
        rootj = self.find(j)
        if rooti != rootj:
            if rooti > rootj:  # 确保较小的作为根节点
                rooti, rootj = rootj, rooti
                i, j = j, i
            self.parent[rootj] = rooti


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union = UnionFind(len(edges) + 1)
        ans = []
        for edge in edges:
            if union.find(edge[0]) != union.find(edge[1]):
                union.unite(edge[0], edge[1])
            else:
                ans = edge
        return ans


s = Solution()
print(s.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))
print(s.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
