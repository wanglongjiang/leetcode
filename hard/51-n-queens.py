from typing import List
'''
思路：回溯
设置1个n*n矩阵,作为算法的数据模型,找到1个解之后就输出
'''


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        matirx = [[]] * n
        for i in range(n):
            matirx[i] = ['.'] * n

        # 判断是否合法的位置,只需要向上搜索同列、左上斜线、右上斜线
        def isValid(row, col):
            left, mid, right = col - 1, col, col + 1
            for row in range(row - 1, -1, -1):
                if left >= 0 and matirx[row][left] == 'Q':
                    return False
                else:
                    left -= 1
                if matirx[row][mid] == 'Q':
                    return False
                if right < n and matirx[row][right] == 'Q':
                    return False
                else:
                    right += 1
            return True

        # 输出当前矩阵到结果list
        def output():
            ans = []
            for i in range(n):
                ans.append(''.join(matirx[i]))
            result.append(ans)

        # 回溯算法
        def queens(row: int):
            for i in range(n):
                # 本位置如果合法，判断是否为最后一行，如果是最后一行，将结果输出，否则进行下一行
                if isValid(row, i):
                    matirx[row][i] = 'Q'
                    if row == n - 1:
                        output()
                    else:
                        queens(row + 1)
                    matirx[row][i] = '.'

        queens(0)
        return result


s = Solution()
print(s.solveNQueens(1))
print(s.solveNQueens(2))
print(s.solveNQueens(3))
print(s.solveNQueens(4))
