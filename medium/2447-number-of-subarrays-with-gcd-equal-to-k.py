'''
2447. 最大公因数等于 K 的子数组数目
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 nums 的子数组中元素的最大公因数等于 k 的子数组数目。

子数组 是数组中一个连续的非空序列。

数组的最大公因数 是能整除数组中所有元素的最大整数。

 

示例 1：

输入：nums = [9,3,1,2,6,3], k = 3
输出：4
解释：nums 的子数组中，以 3 作为最大公因数的子数组如下：
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
示例 2：

输入：nums = [4], k = 7
输出：0
解释：不存在以 7 作为最大公因数的子数组。
 

提示：

1 <= nums.length <= 1000
1 <= nums[i], k <= 109
'''
from math import gcd
from typing import List
'''
思路：动态规划
设二维数组dp[n][n]，dp[i][j]是子数组nums[i..j]的最大公因数，状态转移方程为
dp[i][j]=gcd(dp[i][j-1],nums[j])
最后统计dp中值k的个数即可

时间复杂度：O(n^2)
空间复杂度：O(n^2)
'''


class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]  # 初始化
            ans += 1 if nums[i] == k else 0
        for i in range(n):
            for j in range(i + 1, n):
                dp[i][j] = gcd(dp[i][j - 1], nums[j])
                d, m = divmod(dp[i][j], k)
                if d == 0 or m > 0:  # 因子不含k，提前退出
                    break
                ans += 1 if dp[i][j] == k else 0
        return ans


s = Solution()
assert s.subarrayGCD(nums=[9, 3, 1, 2, 6, 3], k=3) == 4
assert s.subarrayGCD(nums=[4], k=7) == 0
