'''
1856. 子数组最小乘积的最大值
一个数组的 最小乘积 定义为这个数组中 最小值 乘以 数组的 和 。

比方说，数组 [3,2,5] （最小值是 2）的最小乘积为 2 * (3+2+5) = 2 * 10 = 20 。
给你一个正整数数组 nums ，请你返回 nums 任意 非空子数组 的最小乘积 的 最大值 。由于答案可能很大，请你返回答案对  109 + 7 取余 的结果。

请注意，最小乘积的最大值考虑的是取余操作 之前 的结果。题目保证最小乘积的最大值在 不取余 的情况下可以用 64 位有符号整数 保存。

子数组 定义为一个数组的 连续 部分。

 

示例 1：

输入：nums = [1,2,3,2]
输出：14
解释：最小乘积的最大值由子数组 [2,3,2] （最小值是 2）得到。
2 * (2+3+2) = 2 * 7 = 14 。
示例 2：

输入：nums = [2,3,3,1,2]
输出：18
解释：最小乘积的最大值由子数组 [3,3] （最小值是 3）得到。
3 * (3+3) = 3 * 6 = 18 。
示例 3：

输入：nums = [3,1,5,6,4,2]
输出：60
解释：最小乘积的最大值由子数组 [5,6,4] （最小值是 4）得到。
4 * (5+6+4) = 4 * 15 = 60 。
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 107
'''
import itertools
from typing import List
'''
单调栈 前缀和
设一个单调递增栈，内部保存nums的下标和值。
遍历nums，
- 如果遇到的元素比栈顶的大，入栈。
- 如果遇到的元素比栈顶的小，持续出栈直至栈顶不大于当前元素，出栈的元素因为比当前元素大，它作为最小值会截止到当前下标，可以计算它作为最小元素的乘积了。
遍历nums一遍之后，剩余的栈内元素，其作为最小值从其下标开始，截止数组末尾，都需要计算乘积。

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        pres = list(itertools.accumulate(nums))  # 计算前缀和，用于后面计算子数组的最小乘积
        stk, n = [], len(nums)
        for i, num in enumerate(nums):
            leftIdx = i
            while stk and stk[-1][1] > num:  # 将所有比当前元素num大的栈内元素出栈
                j, numj = stk.pop()
                ans = max(ans, numj * (pres[i - 1] - pres[j] + nums[j]))  # 计算以nums[j]作为最小值的乘积
                leftIdx = j
            if not stk or stk[-1][1] < num:  # 栈为空，或者栈顶小于当前元素（栈顶有可能等于当前元素，这种清空需要抛弃），才将当前元素入栈
                stk.append((leftIdx, nums[i]))
        for i, numi in stk:
            ans = max(ans, numi * (pres[n - 1] - pres[i] + nums[i]))  # 计算以nums[i]作为最小值的乘积
        return ans % (10**9 + 7)


s = Solution()
print(s.maxSumMinProduct([3, 1, 5, 6, 4, 2]))
print(s.maxSumMinProduct([1, 2, 3, 2]))
print(s.maxSumMinProduct([2, 3, 3, 1, 2]))
assert s.maxSumMinProduct([1, 1, 3, 2, 2, 2, 1, 5, 1, 5]) == 25
