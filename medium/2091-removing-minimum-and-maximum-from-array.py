'''
2091. 从数组中移除最大值和最小值
给你一个下标从 0 开始的数组 nums ，数组由若干 互不相同 的整数组成。

nums 中有一个值最小的元素和一个值最大的元素。分别称为 最小值 和 最大值 。你的目标是从数组中移除这两个元素。

一次 删除 操作定义为从数组的 前面 移除一个元素或从数组的 后面 移除一个元素。

返回将数组中最小值和最大值 都 移除需要的最小删除次数。

 

示例 1：

输入：nums = [2,10,7,5,4,1,8,6]
输出：5
解释：
数组中的最小元素是 nums[5] ，值为 1 。
数组中的最大元素是 nums[1] ，值为 10 。
将最大值和最小值都移除需要从数组前面移除 2 个元素，从数组后面移除 3 个元素。
结果是 2 + 3 = 5 ，这是所有可能情况中的最小删除次数。
示例 2：

输入：nums = [0,-4,19,1,8,-2,-3,5]
输出：3
解释：
数组中的最小元素是 nums[1] ，值为 -4 。
数组中的最大元素是 nums[2] ，值为 19 。
将最大值和最小值都移除需要从数组前面移除 3 个元素。
结果是 3 ，这是所有可能情况中的最小删除次数。 
示例 3：

输入：nums = [101]
输出：1
解释：
数组中只有这一个元素，那么它既是数组中的最小值又是数组中的最大值。
移除它只需要 1 次删除操作。
 

提示：

1 <= nums.length <= 10^5
-10^5 <= nums[i] <= 10^5
nums 中的整数 互不相同
'''
from typing import List
'''
思路：贪心
找到最大、最小值的坐标，删除一个距离边界较近的元素，然后再删除距离新的边界更近的元素

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minIdx, maxIdx = 0, 0
        n = len(nums)
        for i in range(n):
            if nums[minIdx] > nums[i]:
                minIdx = i
            elif nums[maxIdx] < nums[i]:
                maxIdx = i
        ans = min(minIdx + 1, maxIdx + 1, n - minIdx, n - maxIdx)  # 移除第1个距离边界最近的元素
        if ans == minIdx + 1 or ans == n - minIdx:  # 第1个被移除的是最小元素，计算最大元素距离边界最小值
            return ans + min(abs(maxIdx - minIdx), maxIdx + 1, n - maxIdx)
        else:  # 第1个被移除的是最大元素，计算最小元素距离边界最小值
            return ans + min(abs(maxIdx - minIdx), minIdx + 1, n - minIdx)


s = Solution()
print(s.minimumDeletions([41, -47, -26, 57, 82, -23, 47, 52, 42, 79, 2, 77, 0, -4, 1, -99, -57, 72, -95]))
print(s.minimumDeletions([2, 10, 7, 5, 4, 1, 8, 6]))
print(s.minimumDeletions([0, -4, 19, 1, 8, -2, -3, 5]))
print(s.minimumDeletions([101]))
