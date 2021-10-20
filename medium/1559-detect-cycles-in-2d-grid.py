'''
1559. 二维网格图中探测环
给你一个二维字符网格数组 grid ，大小为 m x n ，你需要检查 grid 中是否存在 相同值 形成的环。

一个环是一条开始和结束于同一个格子的长度 大于等于 4 的路径。对于一个给定的格子，你可以移动到它上、下、左、右四个方向相邻的格子之一，
可以移动的前提是这两个格子有 相同的值 。

同时，你也不能回到上一次移动时所在的格子。比方说，环  (1, 1) -> (1, 2) -> (1, 1) 是不合法的，
因为从 (1, 2) 移动到 (1, 1) 回到了上一次移动时的格子。

如果 grid 中有相同值形成的环，请你返回 true ，否则返回 false 。



示例 1：



输入：grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
输出：true
解释：如下图所示，有 2 个用不同颜色标出来的环：

示例 2：



输入：grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
输出：true
解释：如下图所示，只有高亮所示的一个合法环：

示例 3：



输入：grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
输出：false


提示：

m == grid.length
n == grid[i].length
1 <= m <= 500
1 <= n <= 500
grid 只包含小写英文字母。
'''
from typing import List
'''
思路：DFS
相邻的单元格如果有相同的值，那么这2个单元格之间有一条路径。
用DFS遍历所有路径，如果路径上经过了以往遍历过的单元格，说明有环路。

时间复杂度：O(mn)
空间复杂度：O(mn)
'''


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        marked = [[False] * n for _ in range(m)]

        # DFS 遍历，如果有环路返回true。注意这里有一个prev，确保搜索路径时不会走回头路。
        def dfs(node, prev):
            for x, y in [(node[0] + 1, node[1]), (node[0] - 1, node[1]), (node[0], node[1] + 1), (node[0], node[1] - 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) != prev and grid[node[0]][node[1]] == grid[x][y]:
                    if marked[x][y]:
                        return True
                    marked[x][y] = True
                    if dfs((x, y), node):
                        return True
            return False

        for i in range(m):
            for j in range(n):
                if not marked[i][j]:
                    marked[i][j] = True
                    if dfs((i, j), (i, j)):
                        return True
        return False


s = Solution()
print(s.containsCycle([["a", "a", "a", "a"], ["a", "b", "b", "a"], ["a", "b", "b", "a"], ["a", "a", "a", "a"]]))
print(s.containsCycle([["c", "c", "c", "a"], ["c", "d", "c", "c"], ["c", "c", "e", "c"], ["f", "c", "c", "c"]]))
print(s.containsCycle([["a", "b", "b"], ["b", "z", "b"], ["b", "b", "a"]]))
