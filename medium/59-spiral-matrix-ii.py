'''
螺旋矩阵 II
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
'''
from typing import List
'''
思路：
与54题类似，模拟螺旋的路径，根据方向指令表，分层转圈
设置一个方向指令表，当前进时，按照前进的方向从指令表中取出指令对当前坐标进行修改。
初始前进方向为left，
每当前进一步会有三种结果：
    1、回到原点，这种情况下是转完了一圈，此时需要进入内环（每深入一环，左上角、右下角坐标需要向内移动）
    2、超出范围，这种情况下需要转向下一个方向，下一个方向为指令表中的下一条记录
    3、在范围内，继续前进
'''


class Solution:
    def __init__(self):
        super().__init__()
        # 列表中存储了4个方向（右，下，左，上）前进后对原坐标的修改
        self.step = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[]] * n
        for i in range(n):
            matrix[i] = [0] * n
        direction = 0  # 初始方向为向左
        beginPoint = 0, 0  # 开始点
        endPoint = n - 1, n - 1  # 最大坐标
        i, j = 0, 0  # 当前坐标从0，0开始
        total = n * n  # 数组所有数字总和
        count = 0
        while True:
            matrix[i][j] = count + 1
            count += 1
            if count == total:
                break
            step = self.step[direction]
            nextPoint = (step[0] + i, step[1] + j)
            if nextPoint == beginPoint:  # 回到原点，进入内圈
                beginPoint = (beginPoint[0] + 1, beginPoint[1] + 1)
                endPoint = (endPoint[0] - 1, endPoint[1] - 1)
                direction = 0
                nextPoint = (i, j + 1)
            elif nextPoint[0] < beginPoint[0] or nextPoint[1] < beginPoint[
                    1] or nextPoint[0] > endPoint[0] or nextPoint[
                        1] > endPoint[1]:  # 超出范围,转向
                # 转向，由于self中方向按照右、下、左、上排列，下一个方向为mod4
                direction = (direction + 1) % 4
                step = self.step[direction]
                nextPoint = (step[0] + i, step[1] + j)
            i, j = nextPoint
        return matrix


s = Solution()
print(s.generateMatrix(3))
print(s.generateMatrix(2))
print(s.generateMatrix(1))
