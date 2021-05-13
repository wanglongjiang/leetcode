'''
停在原地的方案数
有一个长度为 arrLen 的数组，开始有一个指针在索引 0 处。

每一步操作中，你可以将指针向左或向右移动 1 步，或者停在原地（指针不能被移动到数组范围外）。

给你两个整数 steps 和 arrLen ，请你计算并返回：在恰好执行 steps 次操作以后，指针仍然指向索引 0 处的方案数。

由于答案可能会很大，请返回方案数 模 10^9 + 7 后的结果。

 

示例 1：
输入：steps = 3, arrLen = 2
输出：4
解释：3 步后，总共有 4 种不同的方法可以停在索引 0 处。
向右，向左，不动
不动，向右，向左
向右，不动，向左
不动，不动，不动

示例  2：
输入：steps = 2, arrLen = 4
输出：2
解释：2 步后，总共有 2 种不同的方法可以停在索引 0 处。
向右，向左
不动，不动

示例 3：
输入：steps = 4, arrLen = 2
输出：8


提示：

1 <= steps <= 500
1 <= arrLen <= 10^6
'''
'''
思路：动态规划
设二维动态规划数组dp，第1维长度为steps+1，第2维长度为min(steps,arrLen)+1
dp[i][j]的含义是，走了i步之后，在位置j的方案数
状态转移方程为：
> dp[i][j] = dp[i-1][j-1]+dp[i-1][j]+dp[i-1][j+1]
> 意思是第i步能到达第j个位置的方案是第i-1步时在位置j-1,j,j+1的方案数之和
初始状态dp[0][0]为1，
其他值都是0，需要说明的是，第2维长度是最大步数+1，最后1个元素的目的是当哨兵，简化dp[i-1][j+1]时的判断

复杂度：
> 时间复杂度：O(mn)，需要m*n的动态规划数组
> 空间复杂度：O(mn)
'''


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        m, n = steps + 1, min(arrLen, steps)
        dp = [[0] * (n + 1) for _ in range(m)]
        dp[0][0] = 1
        for i in range(1, m):
            for j in range(n):
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j + 1]
                if j > 0:
                    dp[i][j] += dp[i - 1][j - 1]
        return dp[steps][0] % (10**9 + 7)  # 返回仍然在原点的方案数


s = Solution()
print(s.numWays(steps=3, arrLen=2))
print(s.numWays(steps=2, arrLen=4))
print(s.numWays(steps=4, arrLen=2))
