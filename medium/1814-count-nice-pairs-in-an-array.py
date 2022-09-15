'''
1814. 统计一个数组中好对子的数目
给你一个数组 nums ，数组中只包含非负整数。定义 rev(x) 的值为将整数 x 各个数字位反转得到的结果。比方说 rev(123) = 321 ， rev(120) = 21 。
我们称满足下面条件的下标对 (i, j) 是 好的 ：

0 <= i < j < nums.length
nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
请你返回好下标对的数目。由于结果可能会很大，请将结果对 109 + 7 取余 后返回。

 

示例 1：

输入：nums = [42,11,1,97]
输出：2
解释：两个坐标对为：
 - (0,3)：42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121 。
 - (1,2)：11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12 。
示例 2：

输入：nums = [13,10,35,24,76]
输出：4
 

提示：

1 <= nums.length <= 105
0 <= nums[i] <= 109
'''
from itertools import count
import math
from typing import Counter, List
'''
思路：数学 交换律 组合公式
利用交换律，公式：nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
可以转为：nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
这样就转为了针对同一个数字计算nums[i] - rev(nums[i])的值，然后放入哈希表计数
用哈希表计数完成后，对于计数超过2的，用组合公式计算对数

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def f(num):
            return num - int(''.join(str(num)[::-1]))

        ans, m = 0, 10**9 + 7
        for count in Counter(f(num) for num in nums).values():
            if count >= 2:
                ans = (ans + math.factorial(count) // (2 * math.factorial(count - 2))) % m  # 用组合公式计算从count中挑选2个的组合数
        return ans


s = Solution()
assert s.countNicePairs([42, 11, 1, 97]) == 2
assert s.countNicePairs([13, 10, 35, 24, 76]) == 4
