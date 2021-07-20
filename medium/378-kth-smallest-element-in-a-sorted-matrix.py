'''
有序矩阵中第 K 小的元素
给你一个 n x n 矩阵 matrix ，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是 排序后 的第 k 小元素，而不是第 k 个 不同 的元素。

 

示例 1：

输入：matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
输出：13
解释：矩阵中的元素为 [1,5,9,10,11,12,13,13,15]，第 8 小元素是 13
示例 2：

输入：matrix = [[-5]], k = 1
输出：-5
 

提示：

n == matrix.length
n == matrix[i].length
1 <= n <= 300
-10^9 <= matrix[i][j] <= 10^9
题目数据 保证 matrix 中的所有行和列都按 非递减顺序 排列
1 <= k <= n^2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
import heapq
'''
思路1，堆
遍历所有的矩阵中的元素，然后用堆（优先队列）保存最小的k个数

时间复杂度：O(n^n*logk)
空间复杂度：O(k)
'''


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for row in matrix:
            for num in row:
                if len(heap) < k:
                    heapq.heappush(heap, -num)
                else:
                    if -num > heap[0]:
                        heapq.heappushpop(heap, -num)
        return -heap[0]


s = Solution()
print(s.kthSmallest(matrix=[[1, 5, 9], [10, 11, 13], [12, 13, 15]], k=8))
print(s.kthSmallest(matrix=[[-5]], k=1))
