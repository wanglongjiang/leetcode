'''
不同路径
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？
'''
'''
解题思路：数学中的组合公式
一个m*n的网络，想要移动到右下角，可以看成是m-1个向下指令与n-1个的向右指令的组合
组合公式为=(m-1+n-1)!/(m-1)!*(n-1)!
'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m, n = (m - 1, n - 1) if m > n else (n - 1, m - 1)
        nFac, sumFac = 1, 1
        for i in range(1, n + 1):
            nFac *= i
            sumFac *= m + i
        return sumFac // nFac


s = Solution()
print(s.uniquePaths(3, 7))
print(s.uniquePaths(3, 2))
print(s.uniquePaths(7, 3))
print(s.uniquePaths(3, 3))
