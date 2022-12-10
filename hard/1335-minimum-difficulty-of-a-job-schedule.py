'''
1335. 工作计划的最低难度
困难
85
相关企业
你需要制定一份 d 天的工作计划表。工作之间存在依赖，要想执行第 i 项工作，你必须完成全部 j 项工作（ 0 <= j < i）。

你每天 至少 需要完成一项任务。工作计划的总难度是这 d 天每一天的难度之和，而一天的工作难度是当天应该完成工作的最大难度。

给你一个整数数组 jobDifficulty 和一个整数 d，分别代表工作难度和需要计划的天数。第 i 项工作的难度是 jobDifficulty[i]。

返回整个工作计划的 最小难度 。如果无法制定工作计划，则返回 -1 。

 

示例 1：



输入：jobDifficulty = [6,5,4,3,2,1], d = 2
输出：7
解释：第一天，您可以完成前 5 项工作，总难度 = 6.
第二天，您可以完成最后一项工作，总难度 = 1.
计划表的难度 = 6 + 1 = 7 
示例 2：

输入：jobDifficulty = [9,9,9], d = 4
输出：-1
解释：就算你每天完成一项工作，仍然有一天是空闲的，你无法制定一份能够满足既定工作时间的计划表。
示例 3：

输入：jobDifficulty = [1,1,1], d = 3
输出：3
解释：工作计划为每天一项工作，总难度为 3 。
示例 4：

输入：jobDifficulty = [7,1,7,1,7,1], d = 3
输出：15
示例 5：

输入：jobDifficulty = [11,111,22,222,33,333,44,444], d = 6
输出：843
 

提示：

1 <= jobDifficulty.length <= 300
0 <= jobDifficulty[i] <= 1000
1 <= d <= 10
'''
from math import inf
from typing import List
'''
[TOC]

# 思路
动态规划

# 解题方法
这道题时间上是将jobDifficulty数组分成d个子数组，使所有子数组的最大值之和最小

设数组dp[d][n]，dp[i][j]意思是截止第i天，第i天的子数组右边界为j时所有子数组的最大值之和，状态转移方程为：
> dp[i][j] = min(dp[i-1][k]+max(jobDifficulty[k..j])),k取值范围为0..j-1

# 复杂度
- 时间复杂度: 
> $O(dn^2)$ 

- 空间复杂度: 
> $O(dn^2)$
'''


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        dp = [[inf] * n for _ in range(d)]
        # 初始化
        maxVal = -inf
        for j in range(n):
            maxVal = max(maxVal, jobDifficulty[j])
            dp[0][j] = maxVal
        # 开始dp计算
        for i in range(1, d):
            for j in range(i, n):
                maxVal = -inf
                for k in range(j - 1, i - 2, -1):  # 从大到小遍历k，便于求当前子数组最大值maxVal
                    maxVal = max(maxVal, jobDifficulty[k + 1])
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + maxVal)
        return dp[-1][-1]


s = Solution()
assert s.minDifficulty(jobDifficulty=[1, 1, 1], d=3) == 3
assert s.minDifficulty(jobDifficulty=[6, 5, 4, 3, 2, 1], d=2) == 7
assert s.minDifficulty(jobDifficulty=[9, 9, 9], d=4) == -1
assert s.minDifficulty(jobDifficulty=[7, 1, 7, 1, 7, 1], d=3) == 15
assert s.minDifficulty(jobDifficulty=[11, 111, 22, 222, 33, 333, 44, 444], d=6) == 843
