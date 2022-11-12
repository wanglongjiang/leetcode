'''
1368. 使网格图至少有一条有效路径的最小代价
困难
113
相关企业
给你一个 m x n 的网格图 grid 。 grid 中每个格子都有一个数字，对应着从该格子出发下一步走的方向。 grid[i][j] 中的数字可能为以下几种情况：

1 ，下一步往右走，也就是你会从 grid[i][j] 走到 grid[i][j + 1]
2 ，下一步往左走，也就是你会从 grid[i][j] 走到 grid[i][j - 1]
3 ，下一步往下走，也就是你会从 grid[i][j] 走到 grid[i + 1][j]
4 ，下一步往上走，也就是你会从 grid[i][j] 走到 grid[i - 1][j]
注意网格图中可能会有 无效数字 ，因为它们可能指向 grid 以外的区域。

一开始，你会从最左上角的格子 (0,0) 出发。我们定义一条 有效路径 为从格子 (0,0) 出发，每一步都顺着数字对应方向走，
最终在最右下角的格子 (m - 1, n - 1) 结束的路径。有效路径 不需要是最短路径 。

你可以花费 cost = 1 的代价修改一个格子中的数字，但每个格子中的数字 只能修改一次 。

请你返回让网格图至少有一条有效路径的最小代价。

 

示例 1：



输入：grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
输出：3
解释：你将从点 (0, 0) 出发。
到达 (3, 3) 的路径为： (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) 
花费代价 cost = 1 使方向向下 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) 
花费代价 cost = 1 使方向向下 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) 
花费代价 cost = 1 使方向向下 --> (3, 3)
总花费为 cost = 3.
示例 2：



输入：grid = [[1,1,3],[3,2,2],[1,1,4]]
输出：0
解释：不修改任何数字你就可以从 (0, 0) 到达 (2, 2) 。
示例 3：



输入：grid = [[1,2],[4,3]]
输出：1
示例 4：

输入：grid = [[2,2,2],[2,2,2]]
输出：3
示例 5：

输入：grid = [[4]]
输出：0
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 100
'''
from collections import deque
from typing import List
'''
[TOC]

# 思路
双队列BFS

# 解题方法
> 由题目知道，遍历到一个节点后，该节点前进方向上的节点与当前节点距离是相同的
> 这里采用2个队列，当前队列queue1存放所有当前距离相同的节点、queue2存放已经在queue1处理过的节点
> 遍历queue1，遍历到一个节点后，节点前进方向上的所有节点加入queue1，直至所有可以直接到达的节点都被遍历完，处理完的加入queue2
> 遍历queue2，将其他方向上的下一节点加入queue1
> 重复上述过程，直至queue1为空


# 复杂度
- 时间复杂度: 
> $O(mn)$

- 空间复杂度: 
> $O(mn)$
'''


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        posOffset = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}  # 沿每个前进方向上前进后的坐标偏移
        m, n = len(grid), len(grid[0])
        queue1, queue2 = deque(), deque()
        marked = set()
        queue1.append((0, 0))
        marked.add((0, 0))
        dis = 0
        while queue1:
            # 处理queue1，将当前队列中节点及节点前进方向的所有节点都遍历完，然后将其加入queue2
            while queue1:
                x, y = queue1.popleft()
                queue2.append((x, y))
                if x == m - 1 and y == n - 1:  # 到达终点
                    return dis
                # 先沿着前进方向前进，将能够到达的节点加入当前队列
                nextX, nextY = x, y
                while True:
                    nextX, nextY = posOffset[grid[nextX][nextY]][0] + nextX, posOffset[grid[nextX][nextY]][1] + nextY
                    # 下一个位置如果未遍历过，加入当前队列；否则退出
                    if 0 <= nextX < m and 0 <= nextY < n and (nextX, nextY) not in marked:
                        queue1.append((nextX, nextY))
                        marked.add((nextX, nextY))
                    else:
                        break
            # 处理queue2，将已经遍历完的节点不在其原有前进方向上的邻接节点加入下一个队列
            while queue2:
                x, y = queue2.popleft()
                # 将其他方向上的下一坐标加入下一队列
                for dir in filter(lambda d: d != grid[x][y], range(1, 5)):
                    nextX, nextY = posOffset[dir][0] + x, posOffset[dir][1] + y
                    if 0 <= nextX < m and 0 <= nextY < n and (nextX, nextY) not in marked:
                        queue1.append((nextX, nextY))
                        marked.add((nextX, nextY))
            dis += 1


s = Solution()
assert s.minCost([[3, 4, 3], [2, 2, 2], [2, 1, 1], [4, 3, 2], [2, 1, 4], [2, 4, 1], [3, 3, 3], [1, 4, 2], [2, 2, 1], [2, 1, 1], [3, 3, 1], [4, 1, 4], [2, 1, 4],
                  [3, 2, 2], [3, 3, 1], [4, 4, 1], [1, 2, 2], [1, 1, 1], [1, 3, 4], [1, 2, 1], [2, 2, 4], [2, 1, 3], [1, 2, 1], [4, 3, 2], [3, 3, 4], [2, 2, 1],
                  [3, 4, 3], [4, 2, 3], [4, 4, 4]]) == 18
assert s.minCost([[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]) == 3
assert s.minCost([[1, 1, 3], [3, 2, 2], [1, 1, 4]]) == 0
assert s.minCost([[1, 2], [4, 3]]) == 1
assert s.minCost([[2, 2, 2], [2, 2, 2]]) == 3
assert s.minCost([[4]]) == 0
