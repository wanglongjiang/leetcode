'''
1712. 将数组分成三个子数组的方案数
我们称一个分割整数数组的方案是 好的 ，当它满足：

数组被分成三个 非空 连续子数组，从左至右分别命名为 left ， mid ， right 。
left 中元素和小于等于 mid 中元素和，mid 中元素和小于等于 right 中元素和。
给你一个 非负 整数数组 nums ，请你返回 好的 分割 nums 方案数目。由于答案可能会很大，请你将结果对 109 + 7 取余后返回。

 

示例 1：

输入：nums = [1,1,1]
输出：1
解释：唯一一种好的分割方案是将 nums 分成 [1] [1] [1] 。
示例 2：

输入：nums = [1,2,2,2,5,0]
输出：3
解释：nums 总共有 3 种好的分割方案：
[1] [2] [2,2,5,0]
[1] [2,2] [2,5,0]
[1,2] [2,2] [5,0]
示例 3：

输入：nums = [3,2,1]
输出：0
解释：没有好的分割方案。
 

提示：

3 <= nums.length <= 105
0 <= nums[i] <= 104
'''
from bisect import bisect_left, bisect_right
from itertools import accumulate
from typing import List
'''
思路：二分查找
'''


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        pre = list(accumulate(nums))
        ans = 0
        for i in range(n):
            l = max(i + 1, bisect_left(pre, pre[i] + pre[i]))
            r = min(n - 1, bisect_right(pre, (pre[i] + pre[-1]) // 2))
            ans = (ans + max(0, r - l)) % mod
        return ans % mod
