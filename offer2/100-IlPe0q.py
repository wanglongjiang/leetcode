'''
剑指 Offer II 100. 三角形中最小路径之和
给定一个三角形 triangle ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。

 

示例 1：

输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
输出：11
解释：如下面简图所示：
   2
  3 4
 6 5 7
4 1 8 3
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
示例 2：

输入：triangle = [[-10]]
输出：-10
 

提示：

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-10^4 <= triangle[i][j] <= 10^4
 

进阶：

你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题吗？
 

注意：本题与主站 120 题相同： https://leetcode-cn.com/problems/triangle/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/IlPe0q
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：动态规划。
对于三角形第i行，第j个元素来说，有动态规划状态转移方程：
1、最短路径p[i][j] = min(p[i-1][j],p[i-1][j-1])，
2、p[0][0] = 0
最后求最后一行的最小值，即为最小路径
时间复杂度：O(n*n)，每个元素遍历一次
空间复杂度：O(n*n)，

'''


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        path = [None] * n
        path[0] = triangle[0]
        for i in range(1, n):
            path[i] = [float('inf')] * (i + 1)
            for j in range(i + 1):
                if j == 0:
                    path[i][j] = path[i - 1][j] + triangle[i][j]
                elif i == j:
                    path[i][j] = path[i - 1][j - 1] + triangle[i][j]
                else:
                    path[i][j] = min(path[i - 1][j - 1] + triangle[i][j], path[i - 1][j] + triangle[i][j])
        return min(path[n - 1])
