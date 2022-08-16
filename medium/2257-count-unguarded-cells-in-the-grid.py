'''
2257. 统计网格图中没有被保卫的格子数
给你两个整数 m 和 n 表示一个下标从 0 开始的 m x n 网格图。同时给你两个二维整数数组 guards 和 walls ，其中 guards[i] = [rowi, coli] 且 walls[j] = [rowj, colj] ，
分别表示第 i 个警卫和第 j 座墙所在的位置。

一个警卫能看到 4 个坐标轴方向（即东、南、西、北）的 所有 格子，除非他们被一座墙或者另外一个警卫 挡住 了视线。如果一个格子能被 至少 一个警卫看到，那么我们说这个格子被 保卫 了。

请你返回空格子中，有多少个格子是 没被保卫 的。

 

示例 1：



输入：m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
输出：7
解释：上图中，被保卫和没有被保卫的格子分别用红色和绿色表示。
总共有 7 个没有被保卫的格子，所以我们返回 7 。
示例 2：



输入：m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
输出：4
解释：上图中，没有被保卫的格子用绿色表示。
总共有 4 个没有被保卫的格子，所以我们返回 4 。
 

提示：

1 <= m, n <= 105
2 <= m * n <= 105
1 <= guards.length, walls.length <= 5 * 104
2 <= guards.length + walls.length <= m * n
guards[i].length == walls[j].length == 2
0 <= rowi, rowj < m
0 <= coli, colj < n
guards 和 walls 中所有位置 互不相同 。
'''
from functools import reduce
from typing import List
'''
思路：模拟
模拟警卫的视线，向4个方向前进，把能看到的单元格标记上。
最后统计未使用的单元格。
时间复杂度：O(m*n)
空间复杂度：O(m*n)
'''


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for g in guards:  # 所有的警卫标记上1
            grid[g[0]][g[1]] = 1
        for w in walls:  # 所有的墙壁标记上1
            grid[w[0]][w[1]] = 1
        for g in guards:  # 遍历所有的警卫，向其4个方向前进
            for i in range(1, m):  # 向上
                if g[0] - i < 0 or grid[g[0] - i][g[1]] == 1:  # 如果遇到边界，或者遇到警卫或者墙壁，不需要继续前进
                    break
                grid[g[0] - i][g[1]] = 2  # 能保护的标记成2
            for i in range(1, m):  # 向下
                if g[0] + i == m or grid[g[0] + i][g[1]] == 1:  # 如果遇到边界，或者遇到警卫或者墙壁，不需要继续前进
                    break
                grid[g[0] + i][g[1]] = 2  # 能保护的标记成2
            for i in range(1, n):  # 向左
                if g[1] - i < 0 or grid[g[0]][g[1] - i] == 1:  # 如果遇到边界，或者遇到警卫或者墙壁，不需要继续前进
                    break
                grid[g[0]][g[1] - i] = 2  # 能保护的标记成2
            for i in range(1, n):  # 向右
                if g[1] + i == n or grid[g[0]][g[1] + i] == 1:  # 如果遇到边界，或者遇到警卫或者墙壁，不需要继续前进
                    break
                grid[g[0]][g[1] + i] = 2  # 能保护的标记成2
        return sum(map(lambda row: reduce(lambda x, y: x + (0 if y else 1), row, 0), grid))


s = Solution()
print(s.countUnguarded(m=4, n=6, guards=[[0, 0], [1, 1], [2, 3]], walls=[[0, 1], [2, 2], [1, 4]]))
