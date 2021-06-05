'''
将矩阵按对角线排序

矩阵对角线 是一条从矩阵最上面行或者最左侧列中的某个元素开始的对角线，沿右下方向一直到矩阵末尾的元素。例如，矩阵 mat 有 6 行 3 列，
从 mat[2][0] 开始的 矩阵对角线 将会经过 mat[2][0]、mat[3][1] 和 mat[4][2] 。

给你一个 m * n 的整数矩阵 mat ，请你将同一条 矩阵对角线 上的元素按升序排序后，返回排好序的矩阵。

 

示例 1：



输入：mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
输出：[[1,1,1,1],[1,2,2,2],[1,2,3,3]]
示例 2：

输入：mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
输出：[[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
 

提示：

m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100
'''
from typing import List
'''
思路：模拟+排序
模拟对角线前进方向，将元素加入数组，然后排序，再将元素写入矩阵

时间复杂度：O(mnlog(min(m,n)))
空间复杂度：O(min(m,n))，需要一个大小为min(m,n)的数组存放对角线数据并进行排序
'''


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        # 从第0行开始遍历对角线
        for col in range(n - 1):
            end = min(m, n)
            ans = []
            for offset in range(end):
                if col + offset < n and offset < m:
                    ans.append(mat[offset][col + offset])
                else:
                    break
            ans.sort()
            for offset in range(end):
                if col + offset < n and offset < m:
                    mat[offset][col + offset] = ans[offset]
                else:
                    break
        # 从第1列开始遍历对角线
        for row in range(1, m - 1):
            end = min(m, n)
            ans = []
            for offset in range(end):
                if row + offset < m and offset < n:
                    ans.append(mat[row + offset][offset])
                else:
                    break
            ans.sort()
            for offset in range(end):
                if row + offset < m and offset < n:
                    mat[row + offset][offset] = ans[offset]
                else:
                    break
        return mat


s = Solution()
print(s.diagonalSort([[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]) == [[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]])
print(
    s.diagonalSort([[11, 25, 66, 1, 69, 7], [23, 55, 17, 45, 15, 52], [75, 31, 36, 44, 58, 8], [22, 27, 33, 25, 68, 4], [84, 28, 14, 11, 5, 50]]) ==
    [[5, 17, 4, 1, 52, 7], [11, 11, 25, 45, 8, 69], [14, 23, 25, 44, 58, 15], [22, 27, 31, 36, 50, 66], [84, 28, 75, 33, 55, 68]])
