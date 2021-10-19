'''
498. 对角线遍历
给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。



示例:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

输出:  [1,2,4,7,5,3,6,8,9]

解释:



说明:

给定矩阵中的元素总数不会超过 100000 。
'''
from typing import List
'''
思路：矩阵 模拟
按照题意，模拟对角线进行坐标的变换

时间复杂度：O(mn)
空间复杂度：O(1)
'''


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0]) if mat else 0
        moveUp = True  # 对角线前进方向，true为向上，false为向下
        i, j = 0, 0
        ans = []
        while i < m and j < n:
            ans.append(mat[i][j])
            if i == m - 1 and j == n - 1:  # 遍历完最后一个节点，退出
                break
            if moveUp:  # 向右上移动
                if i == 0 or j == n - 1:  # 到达边界
                    moveUp = False  # 调转方向
                    if j == n - 1:  # 到达右边界，下降
                        i += 1
                    else:  # 到达上边界，右移
                        j += 1
                else:  # 向右上移动
                    i -= 1
                    j += 1
            else:  # 向左下移动
                if i == m - 1 or j == 0:  # 到达边界
                    moveUp = True  # 调转方向
                    if i == m - 1:  # 到达下届，右移
                        j += 1
                    else:  # 到达左边界，下降
                        i += 1
                else:  # 向左下移动
                    i += 1
                    j -= 1
        return ans


s = Solution()
print(s.findDiagonalOrder([[2, 5], [8, 4], [0, -1]]) == [2, 5, 8, 0, 4, -1])  # TODO
print(s.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(s.findDiagonalOrder([[1, 2], [3, 4]]))
