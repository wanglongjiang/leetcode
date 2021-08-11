'''
剑指 Offer II 040. 矩阵中最大的矩形
给定一个由 0 和 1 组成的矩阵 matrix ，找出只包含 1 的最大矩形，并返回其面积。

注意：此题 matrix 输入格式为一维 01 字符串数组。

 

示例 1：



输入：matrix = ["10100","10111","11111","10010"]
输出：6
解释：最大矩形如上图所示。
示例 2：

输入：matrix = []
输出：0
示例 3：

输入：matrix = ["0"]
输出：0
示例 4：

输入：matrix = ["1"]
输出：1
示例 5：

输入：matrix = ["00"]
输出：0
 

提示：

rows == matrix.length
cols == matrix[0].length
0 <= row, cols <= 200
matrix[i][j] 为 '0' 或 '1'
 

注意：本题与主站 85 题相同（输入参数格式不同）： https://leetcode-cn.com/problems/maximal-rectangle/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/PLYXKQ
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路1，暴力搜索。遍历每个坐标(x,y)，从该点向右下逐步扩大矩阵范围，判断是否全部为1
    该算法的时间复杂度：遍历坐标m*n，扩大矩阵m*n，总时间复杂度为：O(m*n*m*n)，按照数据量为16*10^8，会超出时间限制
思路2，记忆表+单调栈。
    84题也是求最大矩形，本题的输入是矩阵。可以将本题的数据转化为84题的list。
    1、针对矩阵m的每列，从上往下遍历，计算当前位置是第几个连续的'1'，这样得到连续为1的统计矩阵m2。
    2、对矩阵m2的每一行，调用84题的求最大矩形的算法（单调栈），遍历完成后，得到最大矩形面积
    时间复杂度：O(m*n)，第1次遍历矩阵是O(m*n)，第2次是m次调用84题的O(n)算法，也是O(m*n)
    空间复杂度：O(m*n)，需要辅助矩阵m2
'''


class Solution:
    def maximalRectangle(self, matrix: List[str]) -> int:
        rows = len(matrix)
        cols = len(matrix[0]) if rows else 0
        m2 = [[0] * cols for i in range(rows)]
        maxArea = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    if i:
                        m2[i][j] = m2[i - 1][j] + 1
                    else:
                        m2[i][j] = 1
        for i in range(rows):
            maxArea = max(maxArea, self.largestRectangleArea(m2[i]))
        return maxArea

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        vstack = []
        istack = []
        for i in range(n):
            if vstack and vstack[-1] > heights[i]:
                endIndex = i
                while vstack and vstack[-1] > heights[i]:
                    height = vstack.pop()
                    beginIndex = istack.pop()
                    maxArea = max(maxArea, (endIndex - beginIndex) * height)
                vstack.append(heights[i])
                istack.append(beginIndex)
            else:
                vstack.append(heights[i])
                istack.append(i)
        if vstack:
            endIndex = n
            while vstack:
                height = vstack.pop()
                beginIndex = istack.pop()
                maxArea = max(maxArea, (endIndex - beginIndex) * height)
        return maxArea
