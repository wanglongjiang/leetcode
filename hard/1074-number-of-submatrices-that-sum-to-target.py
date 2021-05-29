'''
元素和为目标值的子矩阵数量

给出矩阵 matrix 和目标值 target，返回元素总和等于目标值的非空子矩阵的数量。

子矩阵 x1, y1, x2, y2 是满足 x1 <= x <= x2 且 y1 <= y <= y2 的所有单元 matrix[x][y] 的集合。

如果 (x1, y1, x2, y2) 和 (x1', y1', x2', y2') 两个子矩阵中部分坐标不同（如：x1 != x1'），那么这两个子矩阵也不同。

 

示例 1：



输入：matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
输出：4
解释：四个只含 0 的 1x1 子矩阵。
示例 2：

输入：matrix = [[1,-1],[-1,1]], target = 0
输出：5
解释：两个 1x2 子矩阵，加上两个 2x1 子矩阵，再加上一个 2x2 子矩阵。
示例 3：

输入：matrix = [[904]], target = 0
输出：0
 

提示：

1 <= matrix.length <= 100
1 <= matrix[0].length <= 100
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8
'''
from typing import List
from collections import defaultdict
'''
思路：前缀和+哈希
1. 求出从左上到右下的矩阵前缀和
2. 对于任意2行构成的子矩阵，右边界由左到由扩大范围，其前缀和为subsum，
    > 如果subsum等于target，符合条件的矩阵数+1
    > 设subsum-target=needsum，如果needsum在该子矩阵的子矩阵中出现过，说明该子矩阵减去子子矩阵也符合条件。
    如何求子子矩阵的和呢，我们在2.求子矩阵的前缀和时是从小到达扩大范围的，可以在这个过程中用哈希表记住。

时间复杂度：O(mn^2)
空间复杂度：O(mn)
'''


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        # 计算前缀和，多出的1行1列可以简化计算过程
        presums = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                presums[i][j] = matrix[i - 1][j - 1] + presums[i - 1][j] + presums[i][j - 1] - presums[i - 1][j - 1]
        # 由任意两行构成子矩阵
        ans = 0
        for row1 in range(1, m + 1):
            for row2 in range(row1, m + 1):
                subsumsCounter = defaultdict(int)  # 该哈希表记住所有遍历过的子矩阵前缀和个数
                for col in range(1, n + 1):
                    subsum = presums[row2][col] - presums[row1 - 1][col]  # 计算从row1行到row2行，从1列到col列构成的子矩阵和
                    if subsum == target:
                        ans += 1
                    if (subsum - target) in subsumsCounter:
                        ans += subsumsCounter[subsum - target]
                    subsumsCounter[subsum] += 1
        return ans
