'''
1020. 飞地的数量
给出一个二维数组 A，每个单元格为 0（代表海）或 1（代表陆地）。

移动是指在陆地上从一个地方走到另一个地方（朝四个方向之一）或离开网格的边界。

返回网格中无法在任意次数的移动中离开网格边界的陆地单元格的数量。



示例 1：

输入：[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
输出：3
解释：
有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。
示例 2：

输入：[[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
输出：0
解释：
所有 1 都在边界上或可以到达边界。


提示：

1 <= A.length <= 500
1 <= A[i].length <= 500
0 <= A[i][j] <= 1
所有行的大小都相同
'''
from typing import List
'''
思路：DFS
首先，统计所有陆地单元格的数量；
然后，用DFS从所有边界处单元格出发，遍历能到达的单元格，并计数。
最后，上面2个计数之差即为答案。

时间复杂度：O(mn)
空间复杂度：O(mn)
'''


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = []  # 栈，用于遍历所有从边界处的能到达的陆地单元格
        allCount, sideCount = 0, 0
        marked = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    allCount += 1  # 所有陆地单元格计数
                    if i == 0 or i == m - 1 or j == 0 or j == n - 1:  # 边界处的陆地单元格加入栈，以备后续DFS
                        sideCount += 1
                        q.append((i, j))
                        marked.add((i, j))
        while q:
            i, j = q.pop()
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:  # 尝试向4个方向前进
                if 0 <= x < m and 0 <= y < n and grid[x][y] and (x, y) not in marked:  # 合法的陆地单元格，且之前未遍历过
                    marked.add((x, y))  # 标记为已遍历
                    q.append((x, y))  # 加入栈，待遍历
                    sideCount += 1  # 能到达的单元格数量+1
        return allCount - sideCount


s = Solution()
print(s.numEnclaves([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
print(s.numEnclaves([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]))
