'''
三维形体的表面积
给你一个 n * n 的网格 grid ，上面放置着一些 1 x 1 x 1 的正方体。

每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。

放置好正方体后，任何直接相邻的正方体都会互相粘在一起，形成一些不规则的三维形体。

请你返回最终这些形体的总表面积。

注意：每个形体的底面也需要计入表面积中。

 

示例 1：


输入：grid = [[2]]
输出：10
示例 2：


输入：grid = [[1,2],[3,4]]
输出：34
示例 3：


输入：grid = [[1,0],[0,2]]
输出：16
示例 4：


输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
输出：32
示例 5：


输入：grid = [[2,2,2],[2,1,2],[2,2,2]]
输出：46
 

提示：

n == grid.length
n == grid[i].length
1 <= n <= 50
0 <= grid[i][j] <= 50

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/surface-area-of-3d-shapes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：矩阵
xy平面上的表面积就是所有的不为0的单元格数*2（乘以2的原因是有顶部和底部2个面）
yz,xz面上的表面积，需要遍历每个柱体，柱体靠近边界的面积是高度，
与其他柱体交界的表面积，只有较高的柱体，高出的部分才计算表面积

时间复杂度：O(n^2)
空间复杂度：O(1)
'''


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    ans += 2  # 添加顶部和底部面的面积
                    for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        if x < 0 or x == n:  # 添加x面的投影
                            ans += grid[i][j]
                        elif y < 0 or y == n:  # 添加y面的投影
                            ans += grid[i][j]
                        elif grid[i][j] > grid[x][y]:  # 添加高于相邻柱面的投影
                            ans += grid[i][j] - grid[x][y]
        return ans
