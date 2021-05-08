'''
省份数量
有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。

省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。

给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。

返回矩阵中 省份 的数量。

 

示例 1：


输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
输出：2
示例 2：


输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
输出：3
 

提示：

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] 为 1 或 0
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
'''
from typing import List
'''
思路1：并查集
1、遍历矩阵，将各个城市编号加入并查集
2、查询各个城市所属的根节点，加入set
3、最后set的大小即为省份
时间复杂度：O(n*nlogn*n)
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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        union = UnionFind(n)
        for i in range(n):
            for j in range(i):  # 因isConnected[i][j] == isConnected[j][i]，所以只需要查询矩阵的一半
                if isConnected[i][j]:
                    union.unite(i, j)
        ans = set()
        for i in range(n):
            ans.add(union.find(i))
        return len(ans)


s = Solution()
print(s.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(s.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
