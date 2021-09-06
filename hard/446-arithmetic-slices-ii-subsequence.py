'''
等差数列划分 II - 子序列
给你一个整数数组 nums ，返回 nums 中所有 等差子序列 的数目。

如果一个序列中 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该序列为等差序列。

例如，[1, 3, 5, 7, 9]、[7, 7, 7, 7] 和 [3, -1, -5, -9] 都是等差序列。
再例如，[1, 1, 2, 5, 7] 不是等差序列。
数组中的子序列是从数组中删除一些元素（也可能不删除）得到的一个序列。

例如，[2,5,10] 是 [1,2,1,2,4,1,5,10] 的一个子序列。
题目数据保证答案是一个 32-bit 整数。

 

示例 1：

输入：nums = [2,4,6,8,10]
输出：7
解释：所有的等差子序列为：
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
示例 2：

输入：nums = [7,7,7,7,7]
输出：16
解释：数组中的任意子序列都是等差子序列。
 

提示：

1  <= nums.length <= 1000
-2^31 <= nums[i] <= 23^1 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/arithmetic-slices-ii-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
from collections import defaultdict
'''
思路：哈希+动态规划

用动态规划求差不为0的等差序列个数：
> 设二维哈希表dp，dp[d][i]的含义是，截止nums的第j个元素，差为d的等差序列的个数。
> 用双重循环遍历所有的i,j下标组合(i>j)，动态规划状态转移方程为
> 初始值dp[d][i] = 1
> d = nums[i]-nums[j]
> dp[d][i]+=dp[d][j]

时间复杂度：O(n^2)
空间复杂度：O(n^2)
'''


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0
        dp = defaultdict(dict)
        n = len(nums)
        for i in range(n):
            for j in range(i):
                d = nums[i] - nums[j]
                if i not in dp[d]:
                    dp[d][i] = 1
                else:
                    dp[d][i] += 1
                if j in dp[d] and dp[d][j] > 0:
                    ans += dp[d][j]
                    dp[d][i] += dp[d][j]
        return ans


s = Solution()
print(s.numberOfArithmeticSlices([4, 5, 5, 6, 5, 6, 7, 8]))
print(
    s.numberOfArithmeticSlices([
        79, 20, 64, 28, 67, 81, 60, 58, 97, 85, 92, 96, 82, 89, 46, 50, 15, 2, 36, 44, 54, 2, 90, 37, 7, 79, 26, 40, 34, 67, 64, 28, 60, 89, 46, 31, 9, 95, 43,
        19, 47, 64, 48, 95, 80, 31, 47, 19, 72, 99, 28, 46, 13, 9, 64, 4, 68, 74, 50, 28, 69, 94, 93, 3, 80, 78, 23, 80, 43, 49, 77, 18, 68, 28, 13, 61, 34, 44,
        80, 70, 55, 85, 0, 37, 93, 40, 47, 47, 45, 23, 26, 74, 45, 67, 34, 20, 33, 71, 48, 96
    ]))
print(s.numberOfArithmeticSlices([4, 5, 5, 6, 7, 4, 5, 6]))
print(s.numberOfArithmeticSlices([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(s.numberOfArithmeticSlices([7, 7, 7, 7, 7]))
print(s.numberOfArithmeticSlices([2, 4, 6, 8, 10]))
