'''
2453. 摧毁一系列目标
给你一个下标从 0 开始的数组 nums ，它包含若干正整数，表示数轴上你需要摧毁的目标所在的位置。同时给你一个整数 space 。

你有一台机器可以摧毁目标。给机器 输入 nums[i] ，这台机器会摧毁所有位置在 nums[i] + c * space 的目标，其中 c 是任意非负整数。你想摧毁 nums 中 尽可能多 的目标。

请你返回在摧毁数目最多的前提下，nums[i] 的 最小值 。

 

示例 1：

输入：nums = [3,7,8,1,1,5], space = 2
输出：1
解释：如果我们输入 nums[3] ，我们可以摧毁位于 1,3,5,7,9,... 这些位置的目标。
这种情况下， 我们总共可以摧毁 5 个目标（除了 nums[2]）。
没有办法摧毁多于 5 个目标，所以我们返回 nums[3] 。
示例 2：

输入：nums = [1,3,5,2,4,6], space = 2
输出：1
解释：输入 nums[0] 或者 nums[3] 都会摧毁 3 个目标。
没有办法摧毁多于 3 个目标。
由于 nums[0] 是最小的可以摧毁 3 个目标的整数，所以我们返回 1 。
示例 3：

输入：nums = [6,2,5], space = 100
输出：2
解释：无论我们输入哪个数字，都只能摧毁 1 个目标。输入的最小整数是 nums[1] 。
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= space <= 109
'''
from math import inf
from typing import List
'''
思路：模拟
遍历一次nums数组，根据公式计算以nums[i]作为输入时能够摧毁的目标数=(n-nums[i])//space+(1 if 有余数)，找到最小的数值

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        n, maxDestory, ans = len(nums), -inf, inf
        for num in nums:
            d, r = divmod(n - num, space)
            d += 1 if r else 0
            if d > maxDestory:
                maxDestory = d
                ans = num
            elif d == maxDestory and num < ans:
                ans = num
        return ans


s = Solution()
print(s.destroyTargets(nums=[3, 7, 8, 1, 1, 5], space=2))
print(s.destroyTargets(nums=[1, 3, 5, 2, 4, 6], space=2))
print(s.destroyTargets(nums=[6, 2, 5], space=100))
