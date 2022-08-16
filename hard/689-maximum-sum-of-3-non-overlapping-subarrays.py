'''
689. 三个无重叠子数组的最大和
给你一个整数数组 nums 和一个整数 k ，找出三个长度为 k 、互不重叠、且 3 * k 项的和最大的子数组，并返回这三个子数组。

以下标的数组形式返回结果，数组中的每一项分别指示每个子数组的起始位置（下标从 0 开始）。如果有多个结果，返回字典序最小的一个。

 

示例 1：

输入：nums = [1,2,1,2,6,7,5,1], k = 2
输出：[0,3,5]
解释：子数组 [1, 2], [2, 6], [7, 5] 对应的起始下标为 [0, 3, 5]。
也可以取 [2, 1], 但是结果 [1, 3, 5] 在字典序上更大。
示例 2：

输入：nums = [1,2,1,2,1,2,1,2,1], k = 2
输出：[0,2,4]
 

提示：

1 <= nums.length <= 2 * 10^4
1 <= nums[i] < 216
1 <= k <= floor(nums.length / 3)
'''
'''
思路：动态规划
'''


from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        s = [0] * (n + 1)
        dp = [[0] * 4 for i in range(n + 2)]
        # 前缀和
        for i in range(1, n + 1):
            s[i] = s[i - 1] + nums[i - 1]
        x = n + 1
        # 因为需要求解字典序最小的方案所以逆着递推这样最终才可以求解出一开始字典序最小的方案的下标
        # 逆序递推最后一段最小的下标为n - k + 1这里的下标是从1开始的
        for i in range(n - k + 1, 0, -1):
            for j in range(1, 4):
                dp[i][j] = max(dp[i + 1][j], dp[i + k][j - 1] + s[i + k - 1] - s[i - 1])
                if dp[i][3] >= dp[x][3]: x = i
        # 从前往后求解这样可以求出字典序最小的方案
        y = 3
        res = list()
        while y > 0:
            # 当循环结束之后那么说明找到了当前满足的一段那么字典序肯定是最小的, 第一次的时候因为dp[x][y]一定满足要求的所以一定不会进入循环, 只有当当前这一段不满足题目要求的时候才进入循环
            while dp[x][y] != dp[x + k][y - 1] + s[x + k - 1] - s[x - 1]:
                x += 1
            res.append(x - 1)
            x += k
            y -= 1
        return res
