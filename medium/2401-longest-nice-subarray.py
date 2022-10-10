'''
2401. 最长优雅子数组
给你一个由 正 整数组成的数组 nums 。

如果 nums 的子数组中位于 不同 位置的每对元素按位 与（AND）运算的结果等于 0 ，则称该子数组为 优雅 子数组。

返回 最长 的优雅子数组的长度。

子数组 是数组中的一个 连续 部分。

注意：长度为 1 的子数组始终视作优雅子数组。

 

示例 1：

输入：nums = [1,3,8,48,10]
输出：3
解释：最长的优雅子数组是 [3,8,48] 。子数组满足题目条件：
- 3 AND 8 = 0
- 3 AND 48 = 0
- 8 AND 48 = 0
可以证明不存在更长的优雅子数组，所以返回 3 。
示例 2：

输入：nums = [3,1,5,11,13]
输出：1
解释：最长的优雅子数组长度为 1 ，任何长度为 1 的子数组都满足题目条件。
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 109
'''
from typing import List
'''
思路：滑动窗口 位运算
设一个滑动窗口，
滑动窗口滑过nums，如果新的元素加入窗口内，没有重复的1，则扩大窗口
否则缩小窗口，直至与新元素不会有重复的1为止。
上述滑动过程中记录窗口的大小

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left, i, n = 0, 0, len(nums)
        bitset, ans = 0, 0
        while i < n:
            while i < n and (bitset & nums[i]) == 0:  # 扩大窗口大小，直至nums[i]与之前的位有重复
                bitset |= nums[i]
                i += 1
            ans = max(ans, i - left)
            if i < n:
                while True:
                    bitset ^= nums[left]
                    left += 1
                    if bitset & nums[i] == 0:  # 缩小窗口，直至窗口内的位与nums[i]不再重复
                        break
        return ans


s = Solution()
assert s.longestNiceSubarray([1, 3, 8, 48, 10]) == 3
