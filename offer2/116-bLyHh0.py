'''
剑指 Offer II 116. 朋友圈

一个班上有 n 个同学，其中一些彼此是朋友，另一些不是。朋友关系是可以传递的，如果 a 与 b 直接是朋友，且 b 与 c 是直接朋友，那么 a 与 c 就是间接朋友。

定义 朋友圈 就是一组直接或者间接朋友的同学集合。

给定一个 n x n 的矩阵 isConnected 表示班上的朋友关系，其中 isConnected[i][j] = 1 表示第 i 个同学和第 j 个同学是直接朋友，而 isConnected[i][j] = 0 表示二人不是直接朋友。

返回矩阵中 朋友圈的数量。

 

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
 

注意：本题与主站 547 题相同： https://leetcode-cn.com/problems/number-of-provinces/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bLyHh0
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
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
