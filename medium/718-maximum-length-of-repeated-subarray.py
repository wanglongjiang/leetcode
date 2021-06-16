'''
最长重复子数组

给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。


示例：

输入：
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出：3
解释：
长度最长的公共子数组是 [3, 2, 1] 。
 

提示：

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
'''
from typing import List
'''
思路：动态规划
该题是最长公共子序列LCS的简化版
设一个二维数组dp[i][j]，意思是nums1[i]与nums2[j]进行匹配时的最长公共子数组长度
状态转移公式为
dp[i][j] = 如果 nums1[i]==nums[j] ，为dp[i-1][j-1]+1；否则为0
结果为dp中最大值

时间复杂度：O(mn),m=nums1.length,n=nums2.length
空间复杂度：O(mn)
'''


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        ans = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(ans, dp[i][j])
        return ans


s = Solution()
print(s.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
