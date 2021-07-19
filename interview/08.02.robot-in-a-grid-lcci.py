'''
面试题 08.02. 迷路的机器人
设想有个机器人坐在一个网格的左上角，网格 r 行 c 列。机器人只能向下或向右移动，但不能走到一些被禁止的网格（有障碍物）。
设计一种算法，寻找机器人从左上角移动到右下角的路径。



网格中的障碍物和空位置分别用 1 和 0 来表示。

返回一条可行的路径，路径由经过的网格的行号和列号组成。左上角为 0 行 0 列。如果没有可行的路径，返回空数组。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: [[0,0],[0,1],[0,2],[1,2],[2,2]]
解释:
输入中标粗的位置即为输出表示的路径，即
0行0列（左上角） -> 0行1列 -> 0行2列 -> 1行2列 -> 2行2列（右下角）
'''
from typing import List
'''
思路：BFS
时间复杂度：O(r*c)
空间复杂度：O(r*c)
'''


# Node用于追踪路径
class Node:
    def __init__(self, i, j, prev):
        self.i, self.j = i, j
        self.prev = prev


class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        if not obstacleGrid or not obstacleGrid[0]:
            return []
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        vis = [[False] * n for _ in range(m)]
        q, nextq = [], []
        q.append(Node(0, 0, None))
        path = None
        while q:
            node = q.pop()
            if node.i == (m - 1) and node.j == (n - 1):
                path = node
                break
            if node.i < (m - 1) and obstacleGrid[node.i + 1][node.j] == 0 and not vis[node.i + 1][node.j]:  # 向右移动一步
                vis[node.i + 1][node.j] = True
                nextq.append(Node(node.i + 1, node.j, node))
            if node.j < (n - 1) and obstacleGrid[node.i][node.j + 1] == 0 and not vis[node.i][node.j + 1]:  # 向下移动一步
                vis[node.i][node.j + 1] = True
                nextq.append(Node(node.i, node.j + 1, node))
            if not q:
                q, nextq = nextq, q
        ans = []
        if path:
            while path:
                ans.append([path.i, path.j])
                path = path.prev
            ans.reverse()
        return ans
