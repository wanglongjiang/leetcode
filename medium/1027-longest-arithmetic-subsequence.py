'''
1027. 最长等差数列
给定一个整数数组 A，返回 A 中最长等差子序列的长度。

回想一下，A 的子序列是列表 A[i_1], A[i_2], ..., A[i_k] 其中 0 <= i_1 < i_2 < ... < i_k <= A.length - 1。
并且如果 B[i+1] - B[i]( 0 <= i < B.length - 1) 的值都相同，那么序列 B 是等差的。



示例 1：

输入：[3,6,9,12]
输出：4
解释：
整个数组是公差为 3 的等差数列。
示例 2：

输入：[9,4,7,2,10]
输出：3
解释：
最长的等差子序列是 [4,7,10]。
示例 3：

输入：[20,1,15,3,10,5,8]
输出：4
解释：
最长的等差子序列是 [20,15,10,5]。


提示：

2 <= A.length <= 2000
0 <= A[i] <= 10000
'''
from typing import List
from collections import defaultdict
'''
思路：动态规划 哈希
设哈希表dp，key为整数，是2个数的差，val为哈希表，它的key为数字下标，val为等差序列长度
状态转移方程为：
dp[d][i] = dp[d][j]+1，其中j<i，且nums[i]-nums[j]==d。
具体算法见代码及注释

时间复杂度：O(n^2)
空间复杂度：O(n^2)
'''


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = defaultdict(dict)
        ans = 0
        for i in range(len(nums)):
            for j in range(i):
                d = nums[i] - nums[j]  # 计算nums[i]与之前所有元素的差
                if j not in dp[d]:
                    dp[d][i] = 2  # 如果之前没有i,j之间的等差序列长度，保存为2
                    ans = max(ans, 2)
                else:
                    dp[d][i] = dp[d][j] + 1  # 等差序列长度+1
                    ans = max(ans, dp[d][i])
        return ans


s = Solution()
print(s.longestArithSeqLength([3, 6, 9, 12]))
print(s.longestArithSeqLength([9, 4, 7, 2, 10]))
print(s.longestArithSeqLength([20, 1, 15, 3, 10, 5, 8]))
