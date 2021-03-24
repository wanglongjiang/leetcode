'''
132 模式
给你一个整数数组 nums ，数组中共有 n 个整数。132 模式的子序列 由三个整数 nums[i]、nums[j] 和 nums[k] 组成，
并同时满足：i < j < k 和 nums[i] < nums[k] < nums[j] 。

如果 nums 中存在 132 模式的子序列 ，返回 true ；否则，返回 false 。


进阶：很容易想到时间复杂度为 O(n^2) 的解决方案，你可以设计一个时间复杂度为 O(n logn) 或 O(n) 的解决方案吗？

提示：

n == nums.length
1 <= n <= 10^4
-10^9 <= nums[i] <= 10^9
'''
from typing import List
'''
思路1，单调栈。正序遍历数组。这种算法可以将数组切分成单调递增的子数组，每个元素在入栈前需要遍历每个子数组的最大最小值，判断是否在范围内。
最坏情况下是O(n^2)，会超时。
思路2，单调栈。逆序遍历数组。stack栈顶元素是中间最大值，right是仅小于栈顶元素且位于栈顶元素右侧的第3个值，当前元素为左侧第1个值。
栈内元素从栈顶往栈底单调递减。
算法基本思路：
    1、逆序遍历到的元素nums[i]，如果小于right，返回true。
    2、如果大于栈顶元素，需要将栈顶元素出栈直至栈顶元素大于nums[i]或者栈为空，出栈的元素放入right，然后将nums[i]入栈。经过这样操作之后
    stack栈顶元素始终比right大，且栈顶元素也在right的左边。
    重复上面1、2
'''


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        stack = []
        right = float('-inf')
        for i in range(n - 1, -1, -1):
            if nums[i] < right:
                return True
            while stack and stack[-1] < nums[i]:
                right = stack.pop()
            stack.append(nums[i])
        return False


s = Solution()
print(s.find132pattern([3, 5, 0, 3, 4]))
