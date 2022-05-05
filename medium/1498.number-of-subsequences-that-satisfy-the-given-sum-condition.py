'''
满足条件的子序列数目
给你一个整数数组 nums 和一个整数 target 。

请你统计并返回 nums 中能满足其最小元素与最大元素的 和 小于或等于 target 的 非空 子序列的数目。

由于答案可能很大，请将结果对 10^9 + 7 取余后返回。

 

示例 1：

输入：nums = [3,5,6,7], target = 9
输出：4
解释：有 4 个子序列满足该条件。
[3] -> 最小元素 + 最大元素 <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)
示例 2：

输入：nums = [3,3,6,8], target = 10
输出：6
解释：有 6 个子序列满足该条件。（nums 中可以有重复数字）
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
示例 3：

输入：nums = [2,3,3,4,6,7], target = 12
输出：61
解释：共有 63 个非空子序列，其中 2 个不满足条件（[6,7], [7]）
有效序列总数为（63 - 2 = 61）
示例 4：

输入：nums = [5,2,4,1,7,6,8], target = 16
输出：127
解释：所有非空子序列都满足条件 (2^7 - 1) = 127
 

提示：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
1 <= target <= 10^6
'''
from typing import List
import bisect
'''
思路：排序 双指针
子序列的最大值和最小值之和，其他介于最大和最小值之间的元素出现在子序列的哪个地方是没有影响的。
所以可以先对数组进行排序
然后遍历每个元素nums[i]，如果能找到一个坐标j，满足i<=j，且nums[i]+nums[j]<=target，那么i与i..j之间的元素可以任意组成子序列，子序列的数量是i..j的全组合数量

时间复杂度：O(nlogn)
空间复杂度：O(1)
'''


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans, m = 0, 10**9 + 7
        j = n - 1
        for i in range(n):
            if j >= n:  # 首次定位用二分查找
                j = bisect.bisect_right(nums, target - nums[i], i)
                if j < i:
                    break
            else:  # 双指针查找j
                for j in range(j, i - 1, -1):
                    if nums[i] + nums[j] <= target:
                        break
                else:
                    break
            ans = (ans + 2**(j - i)) % m
        return ans


s = Solution()
print(s.numSubseq(nums=[3, 5, 6, 7], target=9))
print(s.numSubseq(nums=[3, 3, 6, 8], target=10))
print(s.numSubseq(nums=[2, 3, 3, 4, 6, 7], target=12))
