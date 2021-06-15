'''
颜色交替的最短路径

在一个有向图中，节点分别标记为 0, 1, ..., n-1。这个图中的每条边不是红色就是蓝色，且存在自环或平行边。

red_edges 中的每一个 [i, j] 对表示从节点 i 到节点 j 的红色有向边。类似地，
blue_edges 中的每一个 [i, j] 对表示从节点 i 到节点 j 的蓝色有向边。

返回长度为 n 的数组 answer，其中 answer[X] 是从节点 0 到节点 X 的红色边和蓝色边交替出现的最短路径的长度。
如果不存在这样的路径，那么 answer[x] = -1。

 

示例 1：

输入：n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
输出：[0,1,-1]
示例 2：

输入：n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
输出：[0,1,-1]
示例 3：

输入：n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
输出：[0,-1,-1]
示例 4：

输入：n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
输出：[0,1,2]
示例 5：

输入：n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
输出：[0,1,1]
 

提示：

1 <= n <= 100
red_edges.length <= 400
blue_edges.length <= 400
red_edges[i].length == blue_edges[i].length == 2
0 <= red_edges[i][j], blue_edges[i][j] < n
'''
from typing import List
'''
思路：BFS
构造redG和blueG 2个有向图，从节点0开始，路径每前进一步就交替2个图的遍历。
这里有自环和平行边，通常的图的遍历过程中，自环和平行边没有作用，需要排除，而在这里，自环和平行边可能是构成交替路径的必要一条边。
因为自环和平行边的存在，对于已访问过的节点，不能再用通常的visited[nodeid]来判定，使用：
visited[color][nodeid]=set()
意思是在某一颜色下，从该节点出发的边如果被访问过，就会加入set



时间复杂度：O(re+be),re为red_edges.length,be为blue_edgets.length
空间复杂度：O(n+re+be)
'''


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        redG, blueG = [[] for _ in range(n)], [[] for _ in range(n)]  # 定义2个有向图
        for e in red_edges:
            redG[e[0]].append(e[1])
        for e in blue_edges:
            blueG[e[0]].append(e[1])
        ans = [float('inf')] * n

        # 定义BFS遍历函数
        def bfs(color):
            q, nextq = [], []
            level, visited = 0, [[set() for _ in range(n)], [set() for _ in range(n)]]  # visited记录边是否被访问过
            q.append(0)
            while q:
                node = q.pop()
                ans[node] = min(ans[node], level)  # 更新到node的最短路径
                nextColor = 0 if color else 1
                for nextNode in (redG[node] if color else blueG[node]):  # 根据颜色遍历
                    if nextNode not in visited[nextColor][node]:
                        nextq.append(nextNode)
                        visited[nextColor][node].add(nextNode)
                if not q:
                    q, nextq = nextq, q
                    level += 1
                    color = nextColor  # 交替变化颜色

        # 分别用2种颜色开始遍历一次
        bfs(0)
        bfs(1)
        return list(map(lambda i: -1 if i == float('inf') else i, ans))


s = Solution()
print(
    s.shortestAlternatingPaths(6, [[4, 1], [3, 5], [5, 2], [1, 4], [4, 2], [0, 0], [2, 0], [1, 1]], [[5, 5], [5, 0], [4, 4], [0, 3], [1, 0]]) ==
    [0, -1, 4, 1, -1, 2])
print(s.shortestAlternatingPaths(5, [[0, 1], [1, 2], [2, 3], [3, 4]], [[1, 2], [2, 3], [3, 1]]) == [0, 1, 2, 3, 7])
print(s.shortestAlternatingPaths(n=3, red_edges=[[0, 1], [1, 2]], blue_edges=[]) == [0, 1, -1])
print(s.shortestAlternatingPaths(n=3, red_edges=[[0, 1]], blue_edges=[[2, 1]]) == [0, 1, -1])
print(s.shortestAlternatingPaths(n=3, red_edges=[[1, 0]], blue_edges=[[2, 1]]) == [0, -1, -1])
print(s.shortestAlternatingPaths(n=3, red_edges=[[0, 1]], blue_edges=[[1, 2]]) == [0, 1, 2])
print(s.shortestAlternatingPaths(n=3, red_edges=[[0, 1], [0, 2]], blue_edges=[[1, 0]]) == [0, 1, 1])
