'''
目标和

给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，
你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

 
提示：

数组非空，且长度不会超过 20 。
初始的数组的和不会超过 1000 。
保证返回的最终结果能被 32 位整数存下。

提示：

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 100
'''
from typing import List
from collections import defaultdict
'''
思路1，回溯
暴力回溯所有的符号变化

时间复杂度：O(2^n)，n最大为20，大概是10^6
空间复杂度：O(n)

思路2，哈希+回溯
将数组分成2部分，分别对2部分数组和进行计数，存到哈希表中
然后遍历其中一个哈希表，在另外一个哈希表中查找target-val，如果存在，进行累计

时间复杂度：O(2^(n/2))
空间复杂度：O(2^(n/2))
'''


class Solution:
    # 思路2
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            return 1 if abs(nums[0]) == abs(target) else 0
        leftcounter, rightcounter = defaultdict(int), defaultdict(int)
        mid = n // 2

        # 统计2部分所有的和的计数
        def countSum(counter, index, end, total):
            if index == end - 1:
                counter[total + nums[index]] += 1
                counter[total - nums[index]] += 1
            else:
                countSum(counter, index + 1, end, total + nums[index])
                countSum(counter, index + 1, end, total - nums[index])

        countSum(leftcounter, 0, mid, 0)
        countSum(rightcounter, mid, n, 0)
        # 遍历leftcounter，找rightcounter中与其配对的数量
        ans = 0
        for num, count in leftcounter.items():
            ans += count * rightcounter[target - num]
        return ans

    # 思路1
    def findTargetSumWays1(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = 0

        def backtrack(index, total):
            nonlocal count
            if index == n - 1:
                if total + nums[index] == target:
                    count += 1
                if total - nums[index] == target:
                    count += 1
            else:
                backtrack(index + 1, total + nums[index])
                backtrack(index + 1, total - nums[index])

        backtrack(0, 0)
        return count


s = Solution()
print(s.findTargetSumWays([1000], -1000))
print(s.findTargetSumWays([1, 1, 1, 1, 1], 3))
print(s.findTargetSumWays([17, 2, 1, 20, 17, 36, 6, 47, 5, 23, 19, 9, 4, 26, 46, 41, 12, 11, 12, 8], 26))
print(s.findTargetSumWays([1, 0], 1))
