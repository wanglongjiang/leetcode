'''
不相交的线
在两条独立的水平线上按给定的顺序写下 nums1 和 nums2 中的整数。

现在，可以绘制一些连接两个数字 nums1[i] 和 nums2[j] 的直线，这些直线需要同时满足满足：

 nums1[i] == nums2[j]
且绘制的直线不与任何其他连线（非水平线）相交。
请注意，连线即使在端点也不能相交：每个数字只能属于一条连线。

以这种方法绘制线条，并返回可以绘制的最大连线数。

 

示例 1：


输入：nums1 = [1,4,2], nums2 = [1,2,4]
输出：2
解释：可以画出两条不交叉的线，如上图所示。
但无法画出第三条不相交的直线，因为从 nums1[1]=4 到 nums2[2]=4 的直线将与从 nums1[2]=2 到 nums2[1]=2 的直线相交。


示例 2：
输入：nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
输出：3


示例 3：
输入：nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
输出：2
 

提示：

1 <= nums1.length <= 500
1 <= nums2.length <= 500
1 <= nums1[i], nums2[i] <= 2000
'''
from typing import List
'''
思路：动态规划
直觉上可以用动态规划解决，首先需要确定动态规划状态的变化数量，对于nums1[i]来说，nums2中的每个都可能成为其匹配项，故需要二维数组dp
设n1=nums1.length,n2=nums2.length
那么有二维数组dp[n1+1][n2+1]，dp[i+1][j+1]的含义是：nums1中的第i个元素与nums2中的第j个元素进行匹配时最大的连线数量。
状态转移方程为：
> dp[0][0..n]=0表示nums1还没有开始匹配
> dp[0..n][0]=0表示nums2还没有开始匹配
> 如果nums1[i-1]==nums2[j-1]，则：dp[i][j]==dp[i-1][j-1]+1，说明：如果当前2个元素匹配成功，则当前最大连线数为上一个坐标的最大连线数
> 如果nums1[i-1]!=nums2[j-1]，则：dp[i][j]==max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])，说明：如果当前2个元素匹配失败，则当前最大连续数从上一个坐标、本坐标与上一个坐标找一个最大连线数
最后dp[n1][n2]为结果

时间复杂度：O(n1*n2),n1=nums1.length,n2=nums2.length
空间复杂度：O(n1*n2)，需要一个n1*n2的动态规划辅助数组
'''


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
        return dp[n1][n2]


s = Solution()
print(s.maxUncrossedLines(nums1=[1, 4, 2], nums2=[1, 2, 4]))
print(s.maxUncrossedLines(nums1=[2, 5, 1, 2, 5], nums2=[10, 5, 2, 1, 5, 2]))
print(s.maxUncrossedLines(nums1=[1, 3, 7, 1, 7, 5], nums2=[1, 9, 2, 5, 1]))
