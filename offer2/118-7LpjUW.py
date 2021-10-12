'''
剑指 Offer II 118. 多余的边
树可以看成是一个连通且 无环 的 无向 图。

给定往一棵 n 个节点 (节点值 1～n) 的树中添加一条边后的图。添加的边的两个顶点包含在 1 到 n 中间，且这条附加的边不属于树中已存在的边。图的信息记录于长度为 n 的二维数组 edges ，edges[i] = [ai, bi] 表示图中在 ai 和 bi 之间存在一条边。

请找出一条可以删去的边，删除后可使得剩余部分是一个有着 n 个节点的树。如果有多个答案，则返回数组 edges 中最后出现的边。

 

示例 1：



输入: edges = [[1,2],[1,3],[2,3]]
输出: [2,3]
示例 2：



输入: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
输出: [1,4]
 

提示:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
edges 中无重复元素
给定的图是连通的 
 

注意：本题与主站 684 题相同： https://leetcode-cn.com/problems/redundant-connection/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/7LpjUW
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
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

    def union(self, i, j):
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
                union.union(edge[0], edge[1])
            else:
                ans = edge
        return ans
