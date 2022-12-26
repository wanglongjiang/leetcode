'''
1478. 安排邮筒
困难
108
相关企业
给你一个房屋数组houses 和一个整数 k ，其中 houses[i] 是第 i 栋房子在一条街上的位置，现需要在这条街上安排 k 个邮筒。

请你返回每栋房子与离它最近的邮筒之间的距离的 最小 总和。

答案保证在 32 位有符号整数范围以内。

 

示例 1：



输入：houses = [1,4,8,10,20], k = 3
输出：5
解释：将邮筒分别安放在位置 3， 9 和 20 处。
每个房子到最近邮筒的距离和为 |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5 。
示例 2：



输入：houses = [2,3,5,12,18], k = 2
输出：9
解释：将邮筒分别安放在位置 3 和 14 处。
每个房子到最近邮筒距离和为 |2-3| + |3-3| + |5-3| + |12-14| + |18-14| = 9 。
示例 3：

输入：houses = [7,4,6,1], k = 1
输出：8
示例 4：

输入：houses = [3,6,14,10], k = 4
输出：0
 

提示：

n == houses.length
1 <= n <= 100
1 <= houses[i] <= 10^4
1 <= k <= n
数组 houses 中的整数互不相同。
'''
from functools import lru_cache
from math import inf
from typing import List
'''
[TOC]

# 思路
动态规划

# 解题方法
该问题实际上是将数组houses分成k组，每个子数组内放置一个邮筒，使每个元素距离邮筒距离和最小。


可以设数组dp[n][n]，dp[i][j]的意思是截止第i个子数组，子数组截止houses[j]的最小邮筒距离和，状态转移方程为：
> dp[i][j] = min(dp[i-1][i]..dp[i-1][j-1])+子数组内最小邮筒距离
状态转移方程的含义为：第i个右边界为j的子数组，它是第i-1个右边界为i..j-1的子数组中最小的和+子数组内最小邮筒距离。

子数组内最小邮筒距离可以这么计算：如果是奇数组，放到正中间房子距离最小，如果是偶数组，放到中间2个房子之间任意一个位置都可以。
等于abs(subarr[0]-subarr[-1])+abs(subarr[1]-subarr[-2])...

# 复杂度
- 时间复杂度: 
> $O(n^3)$ 

- 空间复杂度: 
> $O(n^2)$
'''


class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        n = len(houses)
        houses.sort()
        dp = [[inf] * n for _ in range(k)]

        # 计算子数组start..end放置一个邮筒的最小距离和
        @lru_cache
        def minDis(start, end):
            ans = 0
            while start < end:
                ans += abs(houses[start] - houses[end])
                start += 1
                end -= 1
            return ans

        # 初始化第1个数组
        for j in range(n):
            dp[0][j] = minDis(0, j)
        # 开始动态规划计算
        for i in range(1, k):
            for j in range(i, n - (k - i - 1)):
                for mid in range(i - 1, j):  # mid为第i-1个子数组的右边界
                    dp[i][j] = min(dp[i][j], dp[i - 1][mid] + minDis(mid + 1, j))
        return dp[-1][-1]


s = Solution()
assert s.minDistance(houses=[3, 6, 14, 10], k=4) == 0
assert s.minDistance(houses=[2, 3, 5, 12, 18], k=2) == 9
assert s.minDistance(houses=[7, 4, 6, 1], k=1) == 8
