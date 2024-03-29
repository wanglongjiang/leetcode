'''
剑指 Offer II 013. 二维子矩阵的和
给定一个二维矩阵 matrix，以下类型的多个请求：

计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2) 。
实现 NumMatrix 类：

NumMatrix(int[][] matrix) 给定整数矩阵 matrix 进行初始化
int sumRegion(int row1, int col1, int row2, int col2) 返回左上角 (row1, col1) 、右下角 (row2, col2) 的子矩阵的元素总和。
 

示例 1：



输入:
["NumMatrix","sumRegion","sumRegion","sumRegion"]
[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]
输出:
[null, 8, 11, 12]

解释:
NumMatrix numMatrix = new NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (红色矩形框的元素总和)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (绿色矩形框的元素总和)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (蓝色矩形框的元素总和)
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
-105 <= matrix[i][j] <= 10^5
0 <= row1 <= row2 < m
0 <= col1 <= col2 < n
最多调用 10^4 次 sumRegion 方法
 

注意：本题与主站 304 题相同： https://leetcode-cn.com/problems/range-sum-query-2d-immutable/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/O4NDxx
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：前缀数组
设置一个辅助二维数组m*n，每个元素存储从0，0到该点的所有元素和
子矩阵的和为子矩阵右下角的值，加上上左上角的值、减去右上角的值、减去左下角的值
'''


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m = len(matrix) + 1
        n = 1 if m == 1 else len(matrix[0]) + 1
        self.sums = [[0] * n for i in range(m)]
        sums = self.sums
        for i in range(m - 1):
            for j in range(n - 1):
                sums[i + 1][j + 1] = sums[i + 1][j] + sums[i][j + 1] + matrix[i][j] - sums[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sums[row2 + 1][col2 + 1] + self.sums[row1][col1] - self.sums[row2 + 1][col1] - self.sums[row1][col2 + 1]
