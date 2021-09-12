'''
重塑矩阵
在MATLAB中，有一个非常有用的函数 reshape，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。

给出一个由二维数组表示的矩阵，以及两个正整数r和c，分别表示想要的重构的矩阵的行数和列数。

重构后的矩阵需要将原始矩阵的所有元素以相同的行遍历顺序填充。

如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。

'''
from typing import List
'''
思路：能重塑的前提是原矩阵元素数==新矩阵的元素数，满足条件后，依次输出每行
'''


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        oldRow = len(nums)
        oldCol = len(nums[0])
        if r * c != oldRow * oldCol:
            return nums
        ansMatrix = []
        for i in range(r):
            ansMatrix.append([])
            for j in range(c):
                totoalIndex = i * c + j
                ansMatrix[i].append(nums[totoalIndex // oldCol][totoalIndex % oldCol])
        return ansMatrix


s = Solution()
print(s.matrixReshape([[1, 2]], 1, 1))
print(s.matrixReshape([[1, 2], [3, 4]], 2, 4))
print(s.matrixReshape([[1, 2], [3, 4]], 1, 4))
