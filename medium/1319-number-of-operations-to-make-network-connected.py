'''
连通网络的操作次数

用以太网线缆将 n 台计算机连接成一个网络，计算机的编号从 0 到 n-1。线缆用 connections 表示，
其中 connections[i] = [a, b] 连接了计算机 a 和 b。

网络中的任何一台计算机都可以通过网络直接或者间接访问同一个网络中其他任意一台计算机。

给你这个计算机网络的初始布线 connections，你可以拔开任意两台直连计算机之间的线缆，并用它连接一对未直连的计算机。
请你计算并返回使所有计算机都连通所需的最少操作次数。如果不可能，则返回 -1 。 

 

示例 1：



输入：n = 4, connections = [[0,1],[0,2],[1,2]]
输出：1
解释：拔下计算机 1 和 2 之间的线缆，并将它插到计算机 1 和 3 上。
示例 2：



输入：n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
输出：2
示例 3：

输入：n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
输出：-1
解释：线缆数量不足。
示例 4：

输入：n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]
输出：0
 

提示：

1 <= n <= 10^5
1 <= connections.length <= min(n*(n-1)/2, 10^5)
connections[i].length == 2
0 <= connections[i][0], connections[i][1] < n
connections[i][0] != connections[i][1]
没有重复的连接。
两台计算机不会通过多条线缆连接。

'''
from typing import List
'''
思路：并查集
n台计算机如果想要连成1个网络，最少需要n-1条线，如果不够这个数量，肯定无法组成一个网络。
如果多于n-1条线，需要用并查集检查有多少个网络，如果网络数量为m，则需要m-1次操作可以将所有网络连结起来。

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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        union = UnionFind(n)
        for conn in connections:
            union.unite(conn[0], conn[1])
        ans = 0
        for i in range(n):
            if union.find(i) == i:
                ans += 1
        return ans - 1


s = Solution()
print(s.makeConnected(n=6, connections=[[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]))
print(s.makeConnected(n=6, connections=[[0, 1], [0, 2], [0, 3], [1, 2]]))
print(s.makeConnected(n=5, connections=[[0, 1], [0, 2], [3, 4], [2, 3]]))
