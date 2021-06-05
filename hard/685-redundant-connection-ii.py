'''
冗余连接 II
在本问题中，有根树指满足以下条件的 有向 图。该树只有一个根节点，所有其他节点都是该根节点的后继。
该树除了根节点之外的每一个节点都有且只有一个父节点，而根节点没有父节点。

输入一个有向图，该图由一个有着 n 个节点（节点值不重复，从 1 到 n）的树及一条附加的有向边构成。
附加的边包含在 1 到 n 中的两个不同顶点间，这条附加的边不属于树中已存在的边。

结果图是一个以边组成的二维数组 edges 。 每个元素是一对 [ui, vi]，用以表示 有向 图中连接顶点 ui 和顶点 vi 的边，其中 ui 是 vi 的一个父节点。

返回一条能删除的边，使得剩下的图是有 n 个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。

 

示例 1：


输入：edges = [[1,2],[1,3],[2,3]]
输出：[2,3]
示例 2：


输入：edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
输出：[4,1]
 

提示：

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ui, vi <= n
'''
from typing import List
'''
思路：并查集
建立一个并查集，对于1个有向边[from,to]，意思是from为父，to为子，
如果在并查集中已经存在to为父，from为子，也就是从from查找其根节点为to，这个边就是冗余的边，需要记录下来。
如果在并查集中from,to的根节点相同，也是冗余的边，需要记录下来
根据上面的思路写出算法：
1. 建立并查集
2. 遍历所有的边，加入并查集，对于当前边edge[i]=[from,to]，
> 如果union.find(from)==to，则edge[i]为冗余边
> 如果union.find(from)==union.find(to)，则edge[i]是冗余边
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
            self.parent[rootj] = rooti


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        union = UnionFind(len(edges) + 1)
        ans = []
        for edge in edges:
            if union.find(edge[0]) != edge[1] and union.find(edge[0]) != union.find(edge[1]):
                union.unite(edge[0], edge[1])
            else:
                ans = edge
        return ans


s = Solution()
print(s.findRedundantDirectedConnection([[1, 2], [1, 3], [2, 3]]))
print(s.findRedundantDirectedConnection([[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]))
