'''
剑指 Offer 13. 机器人的运动范围

地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，
它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。
请问该机器人能够到达多少个格子？

 

示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 2：

输入：m = 3, n = 1, k = 0
输出：1
提示：

1 <= n,m <= 100
0 <= k <= 20
'''
'''
思路：图 BFS
遍历每个单元格的坐标，求其数位和，查看是否<=k，如果满足条件将matrix[i][j]设置为1
然后从matrix[0][0]开始出发，BFS遍历值为1的相邻节点。

时间复杂度：O(mn)
空间复杂度：O(mn)
'''


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        matrix = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                pi, pj = i, j
                s = 0
                while pi:
                    s += pi % 10
                    pi //= 10
                while pj:
                    s += pj % 10
                    pj //= 10
                if s <= k:
                    matrix[i][j] = 1
        ans = 1
        # bfs遍历与0,0相连的所有为1的点
        q, nextq = [], []
        q.append((0, 0))
        matrix[0][0] = 2
        while q:
            i, j = q.pop()
            for ni, nj in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] == 1:
                    matrix[ni][nj] = 2
                    nextq.append((ni, nj))
                    ans += 1
            if not q:
                q, nextq = nextq, q
        return ans
