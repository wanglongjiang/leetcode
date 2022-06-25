'''
2289. 使数组按非递减顺序排列
给你一个下标从 0 开始的整数数组 nums 。在一步操作中，移除所有满足 nums[i - 1] > nums[i] 的 nums[i] ，
其中 0 < i < nums.length 。

重复执行步骤，直到 nums 变为 非递减 数组，返回所需执行的操作数。

 

示例 1：

输入：nums = [5,3,4,4,7,3,6,11,8,5,11]
输出：3
解释：执行下述几个步骤：
- 步骤 1 ：[5,3,4,4,7,3,6,11,8,5,11] 变为 [5,4,4,7,6,11,11]
- 步骤 2 ：[5,4,4,7,6,11,11] 变为 [5,4,7,11,11]
- 步骤 3 ：[5,4,7,11,11] 变为 [5,7,11,11]
[5,7,11,11] 是一个非递减数组，因此，返回 3 。
示例 2：

输入：nums = [4,5,7,7,13]
输出：0
解释：nums 已经是一个非递减数组，因此，返回 0 。
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 109
'''

from turtle import st
from typing import List
'''
思路：单调栈
设立一个单调栈stk，
从右向左遍历nums，使单调栈中元素从栈顶到栈底为递增序列。
遍历过程中遇到栈顶元素小于nums[i]，需要将栈顶元素出栈

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stk = []
        for num in nums[::-1]:
            cnt = 0
            while stk and num > stk[-1][0]:
                cnt = max(cnt + 1, stk.pop()[1])  # 需要消除的个数取 cnt+1或者上个消除个数中的较大值
            stk.append((num, cnt))
        return max(cnt for num, cnt in stk)


s = Solution()
print(s.totalSteps([10, 1, 2, 3, 4, 5, 6, 1, 2, 3]))
