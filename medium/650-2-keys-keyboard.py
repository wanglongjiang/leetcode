'''
650. 只有两个键的键盘
最初记事本上只有一个字符 'A' 。你每次可以对这个记事本进行两种操作：

Copy All（复制全部）：复制这个记事本中的所有字符（不允许仅复制部分字符）。
Paste（粘贴）：粘贴 上一次 复制的字符。
给你一个数字 n ，你需要使用最少的操作次数，在记事本上输出 恰好 n 个 'A' 。返回能够打印出 n 个 'A' 的最少操作次数。



示例 1：

输入：3
输出：3
解释：
最初, 只有一个字符 'A'。
第 1 步, 使用 Copy All 操作。
第 2 步, 使用 Paste 操作来获得 'AA'。
第 3 步, 使用 Paste 操作来获得 'AAA'。
示例 2：

输入：n = 1
输出：0


提示：

1 <= n <= 1000
'''
'''
思路：动态规划
字符数必须以倍数进行增长，实际上是求因子
设数组dp[n]，dp[i]的含义是i个字符的的最小操作数，状态转移方程为：
dp[i] = min(dp[j]+k)，其中1<=j<i，且满足i%j==0，i/j==k
状态转移方程含义是如果i是j的k倍，那么j个:字符复制1，粘贴k-1次可以得到i个字符

时间复杂度：O(n^2)
空间复杂度：O(n)
'''


class Solution:
    def minSteps(self, n: int) -> int:
        dp = list(range(n + 1))  # 初始化值为其索引，因为最多情况下是1个字符复制n次
        dp[1] = 0  # 初始就有1个字符，不需要复制
        for i in range(2, n + 1):
            for j in range(1, i // 2 + 1):
                k, r = divmod(i, j)
                if r == 0:
                    dp[i] = min(dp[i], dp[j] + k)
        return dp[n]


s = Solution()
print(s.minSteps(1000))
print(s.minSteps(6))
print(s.minSteps(5))
print(s.minSteps(4))
print(s.minSteps(3))
print(s.minSteps(2))
print(s.minSteps(1))
