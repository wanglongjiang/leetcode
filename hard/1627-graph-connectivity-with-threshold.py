'''
带阈值的图连通性
有 n 座城市，编号从 1 到 n 。编号为 x 和 y 的两座城市直接连通的前提是： x 和 y 的公因数中，至少有一个 严格大于 某个阈值 threshold 。
更正式地说，如果存在整数 z ，且满足以下所有条件，则编号 x 和 y 的城市之间有一条道路：

x % z == 0
y % z == 0
z > threshold
给你两个整数 n 和 threshold ，以及一个待查询数组，请你判断每个查询 queries[i] = [ai, bi] 指向的城市 ai 和 bi 是否连通
（即，它们之间是否存在一条路径）。

返回数组 answer ，其中answer.length == queries.length 。如果第 i 个查询中指向的城市 ai 和 bi 连通，则 answer[i] 为 true ；
如果不连通，则 answer[i] 为 false 。

 

示例 1：
输入：n = 6, threshold = 2, queries = [[1,4],[2,5],[3,6]]
输出：[false,false,true]
解释：每个数的因数如下：
1:   1
2:   1, 2
3:   1, 3
4:   1, 2, 4
5:   1, 5
6:   1, 2, 3, 6
所有大于阈值的的因数已经加粗标识，只有城市 3 和 6 共享公约数 3 ，因此结果是：
[1,4]   1 与 4 不连通
[2,5]   2 与 5 不连通
[3,6]   3 与 6 连通，存在路径 3--6

示例 2：
输入：n = 6, threshold = 0, queries = [[4,5],[3,4],[3,2],[2,6],[1,3]]
输出：[true,true,true,true,true]
解释：每个数的因数与上一个例子相同。但是，由于阈值为 0 ，所有的因数都大于阈值。因为所有的数字共享公因数 1 ，所以所有的城市都互相连通。

示例 3：
输入：n = 5, threshold = 1, queries = [[4,5],[4,5],[3,2],[2,3],[3,4]]
输出：[false,false,false,false,false]
解释：只有城市 2 和 4 共享的公约数 2 严格大于阈值 1 ，所以只有这两座城市是连通的。
注意，同一对节点 [x, y] 可以有多个查询，并且查询 [x，y] 等同于查询 [y，x] 。
 

提示：

2 <= n <= 10^4
0 <= threshold <= n
1 <= queries.length <= 10^5
queries[i].length == 2
1 <= ai, bi <= cities
ai != bi
'''
from typing import List
'''
思路：并查集+数学分解因子
根据题意，公约数严格大于threshold，可以从threshold+1开始，n截止，针对其中每一个数a
求a的因子，a的因子可以从1开始，sqrt(a)截止，分解成2个因子：f1和f2，如果因子f1或f2大于threshold，将a和因子f1或f2加入并查集。
最后查询queries中的2个数是否在同一集合中

时间复杂度：O(n*sqrt(n)+m)，m为queries.length。n最大为10^4，n*sqrt(n)为10^6
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
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        union = UnionFind(n + 1)
        # 分解因子
        for a in range(threshold + 1, n + 1):
            for f1 in range(1, int(a**0.5) + 1):  # 因子分解从1 至 sqrt(a)
                f2, remainder = divmod(a, f1)
                if remainder == 0:  # 找到一个因子后，加入并查集
                    if f1 > threshold:
                        union.unite(f1, a)
                    if f2 > threshold:
                        union.unite(f2, a)
        # 查询结果
        ans = []
        for q in queries:
            if union.find(q[0]) == union.find(q[1]):
                ans.append(True)
            else:
                ans.append(False)
        return ans


s = Solution()
print(s.areConnected(n=6, threshold=2, queries=[[1, 4], [2, 5], [3, 6]]))
print(s.areConnected(n=6, threshold=0, queries=[[4, 5], [3, 4], [3, 2], [2, 6], [1, 3]]))
print(s.areConnected(n=5, threshold=1, queries=[[4, 5], [4, 5], [3, 2], [2, 3], [3, 4]]))
