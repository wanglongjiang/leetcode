'''
2472. 不重叠回文子字符串的最大数目
困难

给你一个字符串 s 和一个 正 整数 k 。

从字符串 s 中选出一组满足下述条件且 不重叠 的子字符串：

每个子字符串的长度 至少 为 k 。
每个子字符串是一个 回文串 。
返回最优方案中能选择的子字符串的 最大 数目。

子字符串 是字符串中一个连续的字符序列。

 

示例 1 ：

输入：s = "abaccdbbd", k = 3
输出：2
解释：可以选择 s = "abaccdbbd" 中斜体加粗的子字符串。"aba" 和 "dbbd" 都是回文，且长度至少为 k = 3 。
可以证明，无法选出两个以上的有效子字符串。
示例 2 ：

输入：s = "adbcda", k = 2
输出：0
解释：字符串中不存在长度至少为 2 的回文子字符串。
 

提示：

1 <= k <= s.length <= 2000
s 仅由小写英文字母组成
'''
'''
[TOC]

# 思路
动态规划 贪心

# 解题方法
首先，找出所有的回文串：
设dp[n][n]，如果子串s[i:j]为回文串，dp[i][j]存放回文串的长度，状态转移方程为：
dp[i][j] = dp[i+1][j-1] + 2，如果s[i]==s[j]且dp[i+1][j-1]>0
dp[i][j] = 0，如果s[i]!=s[j]

然后，设一个大小为k的滑动窗口滑过0..n，找到所有满足dp[i][j]>0，且（j-i>=k)。

# 复杂度
- 时间复杂度: 
> $O(n^{2})$

- 空间复杂度: 
> $O(n^{2})$
'''


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        # 先找到所有的回文串
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1  # 初始化长度为1的回文串
            if i + 1 < n:
                dp[i][i + 1] = 2 if s[i] == s[i + 1] else 0  # 初始化长度为2的回文串
        for i in range(n - 2, -1, -1):  # 因为状态转移方程中i取决于i+1，所以需要逆序遍历i
            for j in range(n - 1, i + 1, -1):
                if s[i] == s[j] and dp[i + 1][j - 1] > 0:
                    dp[i][j] = dp[i + 1][j - 1] + 2
        # 然后找出最小长度为k的不相交回文串数量
        ans = 0
        i = 0
        while i + k <= n:
            if dp[i][i + k - 1] == k:  # 寻找长度为k的回文串
                ans += 1
                i += k
            elif i + k < n and dp[i][i + k] > k:  # 寻找长度为k+1的回文串
                ans += 1
                i += k + 1
            else:
                i += 1
        return ans


s = Solution()
assert s.maxPalindromes("kwnwkekokedadq", 5) == 2
assert s.maxPalindromes("aaaaa", k=2) == 2
assert s.maxPalindromes("aaaa", k=2) == 2
assert s.maxPalindromes("aaaa", k=1) == 4
assert s.maxPalindromes(s="abaccdbbd", k=3) == 2
assert s.maxPalindromes(s="adbcda", k=2) == 0
