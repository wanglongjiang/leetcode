'''
剑指 Offer II 008. 和大于等于 target 的最短子数组
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。
如果不存在符合条件的子数组，返回 0 。

 

示例 1：

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
示例 2：

输入：target = 4, nums = [1,4,4]
输出：1
示例 3：

输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0
 

提示：

1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
 

进阶：

如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。
 

注意：本题与主站 209 题相同：https://leetcode-cn.com/problems/minimum-size-subarray-sum/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/2VG8Kg
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：滑动窗口
典型的滑动窗口问题，设置left，right指针，窗口内数据之和>=target时，left指针右移，不满足条件时right右移
时间复杂度：O(n)，窗口从左滑动到右边
空间复杂度：O(1)
'''


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right, n = 0, 0, len(nums)
        s = 0
        minLen = float('inf')
        while left < n and right <= n:
            while right < n and s < target:  # 向右移动right指针，直至满足窗口内整数之和s>=target
                s += nums[right]
                right += 1
            if s >= target:
                minLen = min(minLen, right - left)  # 更新最小长度
                if minLen == 1:
                    return minLen  # 如果最小长度为1，不需要向后搜索了，1就是最小值
            s -= nums[left]  # 向右移动left指针
            left += 1
        return minLen if minLen <= n else 0  # 如果minLen ==n，未找到满足条件的窗口，要返回0


s = Solution()
print(s.minSubArrayLen(15, [1, 2, 3, 4, 5]) == 5)
print(s.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]) == 2)
