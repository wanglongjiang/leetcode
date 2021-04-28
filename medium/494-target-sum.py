'''
目标和

给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，
你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

 
提示：

数组非空，且长度不会超过 20 。
初始的数组的和不会超过 1000 。
保证返回的最终结果能被 32 位整数存下。
'''
from typing import List
'''
思路1，回溯
暴力回溯所有的符号变化
时间复杂度：O(2^n)
空间复杂度：O(n)
'''


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = 0

        def backtrack(index, total):
            nonlocal count
            if index == n - 1:
                if total + nums[index] == target or total - nums[index] == target:
                    count += 1
            else:
                backtrack(index + 1, total + nums[index])
                backtrack(index + 1, total - nums[index])

        backtrack(0, 0)
        return count


s = Solution()
print(s.findTargetSumWays([1, 1, 1, 1, 1], 3))
