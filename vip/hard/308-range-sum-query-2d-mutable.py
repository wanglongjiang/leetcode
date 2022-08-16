'''
308. 二维区域和检索 - 可变
给你一个二维矩阵 matrix ，你需要处理下面两种类型的若干次查询：

更新：更新 matrix 中某个单元的值。
求和：计算矩阵 matrix 中某一矩形区域元素的 和 ，该区域由 左上角 (row1, col1) 和 右下角 (row2, col2) 界定。
实现 NumMatrix 类：

NumMatrix(int[][] matrix) 用整数矩阵 matrix 初始化对象。
void update(int row, int col, int val) 更新 matrix[row][col] 的值到 val 。
int sumRegion(int row1, int col1, int row2, int col2) 返回矩阵 matrix 中指定矩形区域元素的 和 ，
该区域由 左上角 (row1, col1) 和 右下角 (row2, col2) 界定。


示例：


输入
["NumMatrix", "sumRegion", "update", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [3, 2, 2], [2, 1, 4, 3]]
输出
[null, 8, null, 10]

解释
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // 返回 8 (即, 左侧红色矩形的和)
numMatrix.update(3, 2, 2);       // 矩阵从左图变为右图
numMatrix.sumRegion(2, 1, 4, 3); // 返回 10 (即，右侧红色矩形的和)


提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
-10^5 <= matrix[i][j] <= 10^5
0 <= row < m
0 <= col < n
-10^5 <= val <= 10^5
0 <= row1 <= row2 < m
0 <= col1 <= col2 < n
最多调用104 次 sumRegion 和 update 方法
'''
from typing import List
'''
TODO sj
'''


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        pass

    def update(self, row: int, col: int, val: int) -> None:
        pass

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        pass


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
