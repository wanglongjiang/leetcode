'''
1391. 检查网格中是否存在有效路径
给你一个 m x n 的网格 grid。网格里的每个单元都代表一条街道。grid[i][j] 的街道可以是：

1 表示连接左单元格和右单元格的街道。
2 表示连接上单元格和下单元格的街道。
3 表示连接左单元格和下单元格的街道。
4 表示连接右单元格和下单元格的街道。
5 表示连接左单元格和上单元格的街道。
6 表示连接右单元格和上单元格的街道。


你最开始从左上角的单元格 (0,0) 开始出发，网格中的「有效路径」是指从左上方的单元格 (0,0) 开始、一直到右下方的 (m-1,n-1) 结束的路径。
该路径必须只沿着街道走。

注意：你 不能 变更街道。

如果网格中存在有效的路径，则返回 true，否则返回 false 。

 

示例 1：



输入：grid = [[2,4,3],[6,5,2]]
输出：true
解释：如图所示，你可以从 (0, 0) 开始，访问网格中的所有单元格并到达 (m - 1, n - 1) 。
示例 2：



输入：grid = [[1,2,1],[1,2,1]]
输出：false
解释：如图所示，单元格 (0, 0) 上的街道没有与任何其他单元格上的街道相连，你只会停在 (0, 0) 处。
示例 3：

输入：grid = [[1,1,2]]
输出：false
解释：你会停在 (0, 1)，而且无法到达 (0, 2) 。
示例 4：

输入：grid = [[1,1,1,1,1,1,3]]
输出：true
示例 5：

输入：grid = [[2],[2],[2],[2],[2],[2],[6]]
输出：true
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 300
1 <= grid[i][j] <= 6
'''

from typing import List
'''
思路：DFS
用DFS遍历所有路径，查看是否能够到达终点

时间复杂度：O(mn)
空间复杂度：O(mn)，最坏情况下所有节点都会经过且在一个路径上
'''


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        marked = [[False] * n for _ in range(m)]

        def canLeft(i, j):  # 是否能从i,j向左移动
            return j > 0 and not marked[i][j - 1] and (grid[i][j - 1] == 1 or grid[i][j - 1] == 4 or grid[i][j - 1] == 6) and dfs(i, j - 1)

        def canRight(i, j):  # 是否能从i,j向右移动
            return j < n - 1 and not marked[i][j + 1] and (grid[i][j + 1] == 1 or grid[i][j + 1] == 3 or grid[i][j + 1] == 5) and dfs(i, j + 1)

        def canUp(i, j):  # 是否能从i,j向上移动
            return i > 0 and not marked[i - 1][j] and (grid[i - 1][j] == 2 or grid[i - 1][j] == 3 or grid[i - 1][j] == 4) and dfs(i - 1, j)

        def canDown(i, j):  # 是否能从i,j向下移动
            return i < m - 1 and not marked[i + 1][j] and (grid[i + 1][j] == 2 or grid[i + 1][j] == 5 or grid[i + 1][j] == 6) and dfs(i + 1, j)

        # 深度优先遍历
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return True
            marked[i][j] = True
            if grid[i][j] == 1:
                if canLeft(i, j) or canRight(i, j):
                    return True
                return False
            if grid[i][j] == 2:
                if canUp(i, j) or canDown(i, j):
                    return True
                return False
            if grid[i][j] == 3:
                if canLeft(i, j) or canDown(i, j):
                    return True
                return False
            if grid[i][j] == 4:
                if canRight(i, j) or canDown(i, j):
                    return True
                return False
            if grid[i][j] == 5:
                if canUp(i, j) or canLeft(i, j):
                    return True
                return False
            if grid[i][j] == 6:
                if canUp(i, j) or canRight(i, j):
                    return True
                return False

        return dfs(0, 0)


s = Solution()
print(s.hasValidPath([[2, 4, 3], [6, 5, 2]]))
print(s.hasValidPath([[1, 2, 1], [1, 2, 1]]))
print(s.hasValidPath([[1, 1, 2]]))
print(s.hasValidPath([[1, 1, 1, 1, 1, 1, 3]]))
print(s.hasValidPath([[2], [2], [2], [2], [2], [2], [6]]))
