'''
出界的路径数
给你一个大小为 m x n 的网格和一个球。球的起始坐标为 [startRow, startColumn] 。
你可以将球移到在四个方向上相邻的单元格内（可以穿过网格边界到达网格之外）。你 最多 可以移动 maxMove 次球。

给你五个整数 m、n、maxMove、startRow 以及 startColumn ，找出并返回可以将球移出边界的路径数量。
因为答案可能非常大，返回对 109 + 7 取余 后的结果。

 

示例 1：


输入：m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
输出：6
示例 2：


输入：m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
输出：12
 

提示：

1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow < m
0 <= startColumn < n

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/out-of-boundary-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：动态规划
从startRow,startCol到外面的路径比较多，时间上会超出。
逆向思维，动态规划累计从边界往起点的路径。
设三维数组dp[k][i][j]为移动k步，到达坐标i,j的路径数为4个邻居单元格的路径和。
状态转移方程为：
dp[k][i][j] = dp[k-1][i-1][j]+dp[k-1][i+1][j]+dp[k-1][i][j-1]+dp[k-1][i][j+1]


时间复杂度：O(mn*maxMove)
空间复杂度：O(mn*maxMove)
'''


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[[0] * n for _ in range(m)] for _ in range(maxMove + 1)]
        for k in range(1, maxMove + 1):
            for i in range(m):
                for j in range(n):
                    a = 1 if i == 0 else dp[k - 1][i - 1][j]
                    b = 1 if i == m - 1 else dp[k - 1][i + 1][j]
                    c = 1 if j == 0 else dp[k - 1][i][j - 1]
                    d = 1 if j == n - 1 else dp[k - 1][i][j + 1]
                    dp[k][i][j] = (a + b + c + d) % 1000000007
        return dp[maxMove][startRow][startColumn]
