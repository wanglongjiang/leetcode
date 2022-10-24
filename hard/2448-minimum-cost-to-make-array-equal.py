'''
2448. 使数组相等的最小开销
给你两个下标从 0 开始的数组 nums 和 cost ，分别包含 n 个 正 整数。

你可以执行下面操作 任意 次：

将 nums 中 任意 元素增加或者减小 1 。
对第 i 个元素执行一次操作的开销是 cost[i] 。

请你返回使 nums 中所有元素 相等 的 最少 总开销。

 

示例 1：

输入：nums = [1,3,5,2], cost = [2,3,1,14]
输出：8
解释：我们可以执行以下操作使所有元素变为 2 ：
- 增加第 0 个元素 1 次，开销为 2 。
- 减小第 1 个元素 1 次，开销为 3 。
- 减小第 2 个元素 3 次，开销为 1 + 1 + 1 = 3 。
总开销为 2 + 3 + 3 = 8 。
这是最小开销。
示例 2：

输入：nums = [2,2,2,2,2], cost = [4,2,8,1,3]
输出：0
解释：数组中所有元素已经全部相等，不需要执行额外的操作。
 

提示：

n == nums.length == cost.length
1 <= n <= 105
1 <= nums[i], cost[i] <= 106
'''
from typing import List
'''
思路：二分查找
设x为nums要调整到的值，成本函数f(x) = sum(abs(nums[i]-x)*cost[i])
该函数为凸函数，可以用二分查找进行查询。
每次计算f(mid),f(mid+1)，
如果f(mid)更小，说明最小值更接近f(mid)，下次迭代需要使区间变成[low,mid]
否则需要使区间变成[mid+1,high]

时间复杂度：O(nlog(max(nums)))
空间复杂度：O(1)
'''


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def f(x):
            return sum(abs(num - x) * c for num, c in zip(nums, cost))

        low, high = 0, max(nums)
        while low < high:
            mid = (low + high) >> 1
            cost1, cost2 = f(mid), f(mid + 1)
            if cost1 < cost2:
                high = mid
            else:
                low = mid + 1
        return f(low)


s = Solution()
print(s.minCost(nums=[2, 2, 2, 2, 2], cost=[4, 2, 8, 1, 3]))
assert s.minCost(
    [735103, 366367, 132236, 133334, 808160, 113001, 49051, 735598, 686615, 665317, 999793, 426087, 587000, 649989, 509946, 743518],
    [724182, 447415, 723725, 902336, 600863, 287644, 13836, 665183, 448859, 917248, 397790, 898215, 790754, 320604, 468575, 825614]) == 1907611126748
print(s.minCost(nums=[1, 3, 5, 2], cost=[2, 3, 1, 14]))
