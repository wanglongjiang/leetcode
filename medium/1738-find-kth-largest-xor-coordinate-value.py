'''
找出第 K 大的异或坐标值
给你一个二维矩阵 matrix 和一个整数 k ，矩阵大小为 m x n 由非负整数组成。

矩阵中坐标 (a, b) 的 值 可由对所有满足 0 <= i <= a < m 且 0 <= j <= b < n 的元素 matrix[i][j]（下标从 0 开始计数）执行异或运算得到。

请你找出 matrix 的所有坐标中第 k 大的值（k 的值从 1 开始计数）。

 

示例 1：

输入：matrix = [[5,2],[1,6]], k = 1
输出：7
解释：坐标 (0,1) 的值是 5 XOR 2 = 7 ，为最大的值。
示例 2：

输入：matrix = [[5,2],[1,6]], k = 2
输出：5
解释：坐标 (0,0) 的值是 5 = 5 ，为第 2 大的值。
示例 3：

输入：matrix = [[5,2],[1,6]], k = 3
输出：4
解释：坐标 (1,0) 的值是 5 XOR 1 = 4 ，为第 3 大的值。
示例 4：

输入：matrix = [[5,2],[1,6]], k = 4
输出：0
解释：坐标 (1,1) 的值是 5 XOR 2 XOR 1 XOR 6 = 0 ，为第 4 大的值。
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
0 <= matrix[i][j] <= 106
1 <= k <= m * n
'''
import heapq
from typing import List
'''
思路：位运算+矩阵+堆
每个坐标的异或值是由原点和其构成的子矩阵所有元素异或得到的。可以计算出异或前缀矩阵。然后遍历异或前缀矩阵，将其加入大小为k的堆中。
具体算法：
1. 计算前缀异或矩阵。第0行、第0列的元素，其异或前缀是前面一个前缀再异或元素自身。其余的元素，根据异或性质可知其是上部^左部^左上^自身。
2. 遍历计算出的矩阵所有元素，加入大小为k的最小堆中，如果当前值大于最小值，将其替换，最后堆中最小值即为结果。

时间复杂度：O(m*nlogk)，创建前缀矩阵需要O(m*n)，加入堆需要O(m*nlogk)
空间复杂度：O(m*n)
'''


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        # 计算前缀矩阵
        prefix = [[0] * n for _ in range(m)]
        prefix[0][0] = matrix[0][0]
        for i in range(1, n):  # 计算第0行
            prefix[0][i] = prefix[0][i - 1] ^ matrix[0][i]
        for i in range(1, m):  # 计算第0列
            prefix[i][0] = prefix[i - 1][0] ^ matrix[i][0]
        for i in range(1, m):  # 计算其余位置
            for j in range(1, n):
                prefix[i][j] = prefix[i - 1][j] ^ prefix[i][j - 1] ^ prefix[i - 1][j - 1] ^ matrix[i][j]
        ans = []
        # 遍历前缀矩阵，将其加入大小为k的堆中
        for i in range(m):
            for j in range(n):
                if len(ans) < k:
                    heapq.heappush(ans, prefix[i][j])
                else:
                    if ans[0] < prefix[i][j]:
                        heapq.heapreplace(ans, prefix[i][j])
        return ans[0]


s = Solution()
print(s.kthLargestValue(matrix=[[5, 2], [1, 6]], k=1))
print(s.kthLargestValue(matrix=[[5, 2], [1, 6]], k=2))
print(s.kthLargestValue(matrix=[[5, 2], [1, 6]], k=3))
print(s.kthLargestValue(matrix=[[5, 2], [1, 6]], k=4))
