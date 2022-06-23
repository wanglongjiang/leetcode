'''
1493. 删掉一个元素以后全为 1 的最长子数组
给你一个二进制数组 nums ，你需要从中删掉一个元素。

请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。

如果不存在这样的子数组，请返回 0 。



提示 1：

输入：nums = [1,1,0,1]
输出：3
解释：删掉位置 2 的数后，[1,1,1] 包含 3 个 1 。
示例 2：

输入：nums = [0,1,1,1,0,1,1,0,1]
输出：5
解释：删掉位置 4 的数字后，[0,1,1,1,1,1,0,1] 的最长全 1 子数组为 [1,1,1,1,1] 。
示例 3：

输入：nums = [1,1,1]
输出：2
解释：你必须要删除一个元素。
示例 4：

输入：nums = [1,1,0,0,1,1,1,0,1]
输出：4
示例 5：

输入：nums = [0,0,0]
输出：0


提示：

1 <= nums.length <= 10^5
nums[i] 要么是 0 要么是 1 。
'''
from typing import List
'''
思路：贪心
遍历数组，遇到连续的1，记录其长度，如果与之前的连续1只相差1个0，记录当前1子数组与前一个1数组的长度和

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        preOneLen = 0  # 记录前一个连续1的长度
        ans = 0
        i, n = 0, len(nums)
        while i < n:
            zeroLen, oneLen = 0, 0  # 记录连续的1，连续0的长度
            while i < n and nums[i] == 0:  # 跳过所有的0
                zeroLen += 1
                i += 1
            while i < n and nums[i]:  # 跳过所有的1
                oneLen += 1
                i += 1
            if zeroLen == 1:  # 与前一个连续性1只隔着1个0，可以连结到一起
                ans = max(ans, oneLen + preOneLen)
            else:  # 与前一个连续1间隔超过1，可以得到的最大长度即为当前连续1 的长度
                ans = max(ans, oneLen)
            preOneLen = oneLen
        return ans if ans < n else n - 1  # 如果全是1，必须删除1个


s = Solution()
print(s.longestSubarray([1, 0, 0, 0, 0]))  # TODO
print(s.longestSubarray([1, 1, 0, 1]))
print(s.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))
print(s.longestSubarray([1, 1, 1]))
print(s.longestSubarray([1, 1, 0, 0, 1, 1, 1, 0, 1]))
print(s.longestSubarray([0, 0, 0]))
