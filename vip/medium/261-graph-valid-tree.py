'''
261. 以图判树
给定从 0 到 n-1 标号的 n 个结点，和一个无向边列表（每条边以结点对来表示），请编写一个函数用来判断这些边是否能够形成一个合法有效的树结构。

示例 1：

输入: n = 5, 边列表 edges = [[0,1], [0,2], [0,3], [1,4]]
输出: true
示例 2:

输入: n = 5, 边列表 edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
输出: false
注意：你可以假定边列表 edges 中不会出现重复的边。由于所有的边是无向边，边 [0,1] 和边 [1,0] 是相同的，因此不会同时出现在边列表 edges 中。
'''
from typing import List
'''
思路：并查集
连结n个节点的树，必然有n-1条边，不满足这个条件，返回false
然后将所有节点加入并查集，最后判断所有的节点的根节点是否都是同一个

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:  # 连结n个节点的树，必然有n-1条边，不满足这个条件，返回false
            return False
        uf = UnionFind(n)
        for e in edges:  # 所有的节点，加入并查集
            uf.union(e[0], e[1])
        for i in range(n):
            if uf.find(i) != 0:  # 根节点不为0，没有连结到树
                return False
        return True


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
