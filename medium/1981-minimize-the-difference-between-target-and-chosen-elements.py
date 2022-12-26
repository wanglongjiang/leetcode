'''
1981. 最小化目标值与所选元素的差
给你一个大小为 m x n 的整数矩阵 mat 和一个整数 target 。

从矩阵的 每一行 中选择一个整数，你的目标是 最小化 所有选中元素之 和 与目标值 target 的 绝对差 。

返回 最小的绝对差 。

a 和 b 两数字的 绝对差 是 a - b 的绝对值。

 

示例 1：



输入：mat = [[1,2,3],[4,5,6],[7,8,9]], target = 13
输出：0
解释：一种可能的最优选择方案是：
- 第一行选出 1
- 第二行选出 5
- 第三行选出 7
所选元素的和是 13 ，等于目标值，所以绝对差是 0 。
示例 2：



输入：mat = [[1],[2],[3]], target = 100
输出：94
解释：唯一一种选择方案是：
- 第一行选出 1
- 第二行选出 2
- 第三行选出 3
所选元素的和是 6 ，绝对差是 94 。
示例 3：



输入：mat = [[1,2,9,8,7]], target = 6
输出：1
解释：最优的选择方案是选出第一行的 7 。
绝对差是 1 。
 

提示：

m == mat.length
n == mat[i].length
1 <= m, n <= 70
1 <= mat[i][j] <= 70
1 <= target <= 800
'''
from itertools import product
from math import inf
from typing import List
'''
动态规划
设数组dp[m]，dp[i]存放哈希表，含义是截止第i行能够得到的结果集合
状态转移方程为：
dp[i] = dp[i-1]内所有元素+mat[i]内所有元素的组合
因为dp[i]只依赖于上一个状态，所以可以进行空间优化

时间复杂度：O(m*n*target)
空间复杂度：O(target)
'''


class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        vals = set(mat[0])
        for i in range(1, len(mat)):
            vals = set(map(sum, product(vals, mat[i])))
        diff = inf
        diff = min(map(lambda val: abs(val - target), vals))
        return diff


s = Solution()
print(s.minimizeTheDifference(mat=[[15, 15], [5, 15], [2, 15]], target=29))
assert s.minimizeTheDifference(mat=[[1, 2, 9, 8, 7]], target=6) == 1
assert s.minimizeTheDifference(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], target=13) == 0
assert s.minimizeTheDifference(mat=[[1], [2], [3]], target=100) == 94
