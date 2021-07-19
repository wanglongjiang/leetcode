'''
最大宽度坡
给定一个整数数组 A，坡是元组 (i, j)，其中  i < j 且 A[i] <= A[j]。这样的坡的宽度为 j - i。

找出 A 中的坡的最大宽度，如果不存在，返回 0 。

 

示例 1：

输入：[6,0,8,2,1,5]
输出：4
解释：
最大宽度的坡为 (i, j) = (1, 5): A[1] = 0 且 A[5] = 5.
示例 2：

输入：[9,8,1,0,1,9,4,0,4,1]
输出：7
解释：
最大宽度的坡为 (i, j) = (2, 9): A[2] = 1 且 A[9] = 1.
 

提示：

2 <= A.length <= 50000
0 <= A[i] <= 50000
'''
from typing import List
'''
思路：单调栈
首先从左到右遍历nums，元素索引递减入栈（只有小于栈顶元素才入栈），这样能把最小的元素索引入栈。
然后从右到左遍历nums，元素与栈顶元素比较：
> 如果nums[i]大于等于栈顶元素，此时他们之间的宽度即为坡度宽度。
> 持续上面的过程，直至nums[i]小于栈顶元素或为空

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for i, num in enumerate(nums):
            if not stack or nums[stack[-1]] > num:
                stack.append(i)
        ans = 0
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] >= nums[stack[-1]]:
                ans = max(ans, i - stack[-1])
                stack.pop()
        return ans
