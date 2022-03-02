'''
934. 最短的桥
在给定的二维二进制数组 A 中，存在两座岛。（岛是由四面相连的 1 形成的一个最大组。）

现在，我们可以将 0 变为 1，以使两座岛连接起来，变成一座岛。

返回必须翻转的 0 的最小数目。（可以保证答案至少是 1 。）



示例 1：

输入：A = [[0,1],[1,0]]
输出：1
示例 2：

输入：A = [[0,1,0],[0,0,0],[0,0,1]]
输出：2
示例 3：

输入：A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
输出：1


提示：

2 <= A.length == A[0].length <= 100
A[i][j] == 0 或 A[i][j] == 1
'''
from typing import List
'''
思路：BFS
1. 遍历矩阵，找到第1个1，用BFS找到所有岛屿的陆地；
2. 从该岛屿的所有陆地出发，用BFS查找距离另外一个岛屿最近的距离

时间复杂度：O(n^4)
空间复杂度：O(n^4)
'''


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        island = set()
        for i in range(m):
            for j in range(n):
                if A[i][j]:  # 找到第1块陆地，用bfs找到该岛屿的所有陆地，加入island
                    marked = [[False] * n for _ in range(m)]
                    q, nextq = [], []
                    q.append((i, j))
                    island.add((i, j))
                    marked[i][j] = True
                    while q:
                        x, y = q.pop()
                        for nextx, nexty in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                            if 0 <= nextx < m and 0 <= nexty < n and A[nextx][nexty] and not marked[nextx][nexty]:
                                marked[nextx][nexty] = True
                                nextq.append((nextx, nexty))
                                island.add((nextx, nexty))
                        if not q:
                            q, nextq = nextq, q
                    break  # 找到第1个岛屿后就中止
            if island:
                break  # 找到第1个岛屿后就中止
        # 从该岛屿的所有陆地出发，用BFS查找距离另外一个岛屿最近的距离
        ans = float('inf')
        for i, j in island:
            marked = [[False] * n for _ in range(m)]
            q, nextq = [], []
            q.append((i, j))
            dis = 0
            while q:
                x, y = q.pop()
                for nextx, nexty in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= nextx < m and 0 <= nexty < n:
                        if A[nextx][nexty]:  # 该单元格是陆地
                            if (nextx, nexty) not in island:  # 该陆地属于另外一个岛屿
                                ans = dis
                        else:  # 该单元格是海洋，加入路径
                            if not marked[nextx][nexty]:
                                marked[nextx][nexty] = True
                                nextq.append((nextx, nexty))
                if not q:
                    q, nextq = nextq, q
                    dis += 1
                    if dis >= ans:  # 剪枝，如果超过了以往遍历过的最短距离，不需要再遍历
                        break
        return ans


s = Solution()
print(s.shortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]]))
print(s.shortestBridge([[0, 1], [1, 0]]))
print(s.shortestBridge([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]))
