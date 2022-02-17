'''
688. 骑士在棋盘上的概率
在一个 n x n 的国际象棋棋盘上，一个骑士从单元格 (row, column) 开始，并尝试进行 k 次移动。
行和列是 从 0 开始 的，所以左上单元格是 (0,0) ，右下单元格是 (n - 1, n - 1) 。

象棋骑士有8种可能的走法，如下图所示。每次移动在基本方向上是两个单元格，然后在正交方向上是一个单元格。



每次骑士要移动时，它都会随机从8种可能的移动中选择一种(即使棋子会离开棋盘)，然后移动到那里。

骑士继续移动，直到它走了 k 步或离开了棋盘。

返回 骑士在棋盘停止移动后仍留在棋盘上的概率 。

 

示例 1：

输入: n = 3, k = 2, row = 0, column = 0
输出: 0.0625
解释: 有两步(到(1,2)，(2,1))可以让骑士留在棋盘上。
在每一个位置上，也有两种移动可以让骑士留在棋盘上。
骑士留在棋盘上的总概率是0.0625。
示例 2：

输入: n = 1, k = 0, row = 0, column = 0
输出: 1.00000
 

提示:

1 <= n <= 25
0 <= k <= 100
0 <= row, column <= n
'''
'''
一个骑士有 88 种可能的走法，骑士会从中以等概率随机选择一种。部分走法可能会让骑士离开棋盘，另外的走法则会让骑士移动到棋盘的其他位置，
并且剩余的移动次数会减少 11。

定义 \textit{dp}[\textit{step}][i][j]dp[step][i][j] 表示骑士从棋盘上的点 (i, j)(i,j) 出发，
走了 \textit{step}step 步时仍然留在棋盘上的概率。特别地，当点 (i, j)(i,j) 不在棋盘上时，
\textit{dp}[\textit{step}][i][j] = 0dp[step][i][j]=0；当点 (i, j)(i,j) 在棋盘上
且 \textit{step} = 0step=0 时，\textit{dp}[\textit{step}][i][j] = 1dp[step][i][j]=1。
对于其他情况，\textit{dp}[\textit{step}][i][j] = \dfrac{1}{8} \times \sum\limits_{\textit{di}, \textit{dj}} \textit{dp}[\textit{step}-1][i+\textit{di}][j+\textit{dj}]dp[step][i][j]= 
8
1
​
 × 
di,dj
∑
​
 dp[step−1][i+di][j+dj]。
 其中 (\textit{di}, \textit{dj})(di,dj) 表示走法对坐标的偏移量，
 具体为 (-2, -1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)(−2,−1),(−2,1),(2,−1),(2,1),(−1,−2),(−1,2),(1,−2),(1,2) 共 88 种。

时间复杂度：O(k \times n ^ 2)O(k×n 
2
 )。状态数一共有 O(k \times n ^ 2)O(k×n 
2
 )，每次转移需要考虑 88 种可能的走法，消耗 O(1)O(1) 的时间复杂度，总体的时间复杂度是 O(k \times n ^ 2)O(k×n 
2
 )。

空间复杂度：O(k \times n ^ 2)O(k×n 2
 )。状态数一共有 O(k \times n ^ 2)O(k×n 
2
 )，用一个数组来保存。注意到每一步的状态只由前一步决定，空间复杂度可以优化到 O(n ^ 2)O(n 
2
 )。

'''


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[[0] * n for _ in range(n)] for _ in range(k + 1)]
        for step in range(k + 1):
            for i in range(n):
                for j in range(n):
                    if step == 0:
                        dp[step][i][j] = 1
                    else:
                        for di, dj in ((-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)):
                            ni, nj = i + di, j + dj
                            if 0 <= ni < n and 0 <= nj < n:
                                dp[step][i][j] += dp[step - 1][ni][nj] / 8
        return dp[k][row][column]
