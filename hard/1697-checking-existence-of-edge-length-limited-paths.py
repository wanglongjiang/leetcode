'''
检查边长度限制的路径是否存在

给你一个 n 个点组成的无向图边集 edgeList ，其中 edgeList[i] = [ui, vi, disi] 表示点 ui 和点 vi 之间有一条长度为 disi 的边。
请注意，两个点之间可能有 超过一条边 。

给你一个查询数组queries ，其中 queries[j] = [pj, qj, limitj] ，你的任务是对于每个查询 queries[j] ，
判断是否存在从 pj 到 qj 的路径，且这条路径上的每一条边都 严格小于 limitj 。

请你返回一个 布尔数组 answer ，其中 answer.length == queries.length ，当 queries[j] 的查询结果为 true 时，
answer 第 j 个值为 true ，否则为 false 。

 

示例 1：
输入：n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
输出：[false,true]
解释：上图为给定的输入数据。注意到 0 和 1 之间有两条重边，分别为 2 和 16 。
对于第一个查询，0 和 1 之间没有小于 2 的边，所以我们返回 false 。
对于第二个查询，有一条路径（0 -> 1 -> 2）两条边都小于 5 ，所以这个查询我们返回 true 。

示例 2：
输入：n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]
输出：[true,false]
解释：上图为给定数据。
 

提示：

2 <= n <= 10^5
1 <= edgeList.length, queries.length <= 10^5
edgeList[i].length == 3
queries[j].length == 3
0 <= ui, vi, pj, qj <= n - 1
ui != vi
pj != qj
1 <= disi, limitj <= 10^9
两个点之间可能有 多条 边。

'''
from typing import List
'''
思路：排序+并查集
如果是每次查询都查询图的路径，时间复杂度为O(mn)，m为queries.length，n为图中节点数量，会超时。
换个思路，将queries和edgeList都按照距离从小到大进行排序，查询queries[i]的时候，将小于limiti的所有图的边加入并查集，
如果queries[i]中的2个顶点连通了，该查询为true，否则为false

时间复杂度：O(nlogn+mlogm)，2个排序的需要的时间复杂度都是O(nlogn)，然后查询过程需要O(n)
空间复杂度：O(n)，需要并查集存放图
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
            if rooti > rootj:
                rooti, rootj = rootj, rooti
                i, j = j, i
            self.parent[rootj] = rooti


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key=lambda edge: edge[2])  # 排序
        m = len(queries)
        qs = sorted(zip(queries, range(m)), key=lambda item: item[0][2])  # 排序
        ans = [False] * m
        i, edgesSize = 0, len(edgeList)
        union = UnionFind(n)
        for q in qs:
            while i < edgesSize and edgeList[i][2] < q[0][2]:  # 将小于当前查询距离的边加入并查集
                union.union(edgeList[i][0], edgeList[i][1])
                i += 1
            if union.find(q[0][0]) == union.find(q[0][1]):  # 查询的2个顶点如果连通，写入结果
                ans[q[1]] = True
        return ans
