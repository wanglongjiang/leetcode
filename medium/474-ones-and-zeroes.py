'''
一和零
给你一个二进制字符串数组 strs 和两个整数 m 和 n 。

请你找出并返回 strs 的最大子集的大小，该子集中 最多 有 m 个 0 和 n 个 1 。

如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。
提示：

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] 仅由 '0' 和 '1' 组成
1 <= m, n <= 100
'''
from typing import List
'''
思路：动态规划
设一个二维数组dp[i][j]，含义是还有i个0，j个1时字符串的最大数量。
状态有2个：选择和不选。
设当前字符串有a个0，b个1，
dp[i][j]=max(dp[i][j], dp[i-a][j-b]+1)
根据上面的思路写出代码

时间复杂度：O(mnl)l为字符串长度
空间复杂度：O(mn)
'''


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            a, b = 0, 0  # 统计0,1的个数
            for c in s:
                if c == '0':
                    a += 1
                else:
                    b += 1
            for i in range(m, a - 1, -1):  # 遍历能包含当前字符串的所有组合，计数最大字符串个数
                for j in range(n, b - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - a][j - b] + 1)
        return dp[m][n]
