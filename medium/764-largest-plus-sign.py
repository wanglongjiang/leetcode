'''
764. 最大加号标志
在一个 n x n 的矩阵 grid 中，除了在数组 mines 中给出的元素为 0，其他每个元素都为 1。
mines[i] = [xi, yi]表示 grid[xi][yi] == 0

返回  grid 中包含 1 的最大的 轴对齐 加号标志的阶数 。如果未找到加号标志，则返回 0 。

一个 k 阶由 1 组成的 “轴对称”加号标志 具有中心网格 grid[r][c] == 1 ，
以及4个从中心向上、向下、向左、向右延伸，长度为 k-1，由 1 组成的臂。
注意，只有加号标志的所有网格要求为 1 ，别的网格可能为 0 也可能为 1 。

 

示例 1：



输入: n = 5, mines = [[4, 2]]
输出: 2
解释: 在上面的网格中，最大加号标志的阶只能是2。一个标志已在图中标出。
示例 2：



输入: n = 1, mines = [[0, 0]]
输出: 0
解释: 没有加号标志，返回 0 。
 

提示：

1 <= n <= 500
1 <= mines.length <= 5000
0 <= xi, yi < n
每一对 (xi, yi) 都 不重复
'''

from typing import List
'''
思路：前缀和-空间换时间
设置4个辅助矩阵，left,top,bottom,right。
每个矩阵分别记住截止当前单元格，从左往右、从上往下、从下向上、从右向左的1的累计个数（如果有0，重新开始计数）。
最后的结果就是min(left[i][j],top[i][j],bottom[i][j],right[i][j])最大的

时间复杂度：O(n^2)
空间复杂度：O(n^2)
'''


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        # 初始化4个矩阵
        left, right, bottom, top = [[1] * n for _ in range(n)], [[1] * n for _ in range(n)], [[1] * n for _ in range(n)], [[1] * n for _ in range(n)]
        for m in mines:
            left[m[0]][m[1]] = 0
            right[m[0]][m[1]] = 0
            bottom[m[0]][m[1]] = 0
            top[m[0]][m[1]] = 0
        # 下面计算4个矩阵的前缀和
        for i in range(n):
            for j in range(n):
                if left[i][j] and j > 0:
                    left[i][j] = left[i][j - 1] + 1
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if right[i][j] and j < n - 1:
                    right[i][j] = right[i][j + 1] + 1
        for i in range(n):
            for j in range(n):
                if top[i][j] and i > 0:
                    top[i][j] = top[i - 1][j] + 1
        for i in range(n - 1, -1, -1):
            for j in range(n):
                if bottom[i][j] and i < n - 1:
                    bottom[i][j] = bottom[i + 1][j] + 1
        # 查找最大的十字
        ans = 0
        for i in range(n):
            for j in range(n):
                ans = max(ans, min(left[i][j], right[i][j], top[i][j], bottom[i][j]))
        return ans
