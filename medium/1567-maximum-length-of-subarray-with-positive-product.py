'''
乘积为正数的最长子数组长度
给你一个整数数组 nums ，请你求出乘积为正数的最长子数组的长度。

一个数组的子数组是由原数组中零个或者更多个连续数字组成的数组。

请你返回乘积为正数的最长子数组长度。

 

示例  1：

输入：nums = [1,-2,-3,4]
输出：4
解释：数组本身乘积就是正数，值为 24 。
示例 2：

输入：nums = [0,1,-2,-3,-4]
输出：3
解释：最长乘积为正数的子数组为 [1,-2,-3] ，乘积为 6 。
注意，我们不能把 0 也包括到子数组中，因为这样乘积为 0 ，不是正数。
示例 3：

输入：nums = [-1,-2,-3,0,1]
输出：2
解释：乘积为正数的最长子数组是 [-1,-2] 或者 [-2,-3] 。
示例 4：

输入：nums = [-1,2]
输出：1
示例 5：

输入：nums = [1,2,3,5,-6,4,0,10]
输出：4
 

提示：

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-length-of-subarray-with-positive-product
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路，滑动窗口
0与任何数的乘积都是0，因此可以将数组看成被0分割的子数组，在各个子数组中查找乘积为正数的长度。
1、right指针向右移动，neg累计left至right指针之间的负数个数，如果负数个数为偶数，则记录最大子数组长度，直至right遇到0或末尾。
2、向右移动left指针，neg减去负数的个数，如果负数个数为偶数，则记录最大子数组长度，直至left追上right。
重复以上过程直至left指针移动到末尾。

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        left, right, n = 0, 0, len(nums)
        neg, ans = 0, 0
        while left < n:
            while right < n and nums[right] != 0:  # 移动right指针直至遇到0，这中间用neg累计负数个数，ans记录最大的正数长度
                neg += 1 if nums[right] < 0 else 0
                right += 1
                if neg % 2 == 0:
                    ans = max(ans, right - left)
            while left + 1 < right:  # 移动left指针，这中间用neg累计负数个数，ans记录最大的长度
                neg -= 1 if nums[left] < 0 else 0
                left += 1
                if neg % 2 == 0:
                    ans = max(ans, right - left)
            while right < n and nums[right] == 0:  # 跳过0
                right += 1
            left = right
            neg = 0
        return int(ans)


s = Solution()
print(s.getMaxLen([1, -2, -3, 4]))
print(s.getMaxLen([0, 1, -2, -3, -4]))
print(s.getMaxLen([-1, -2, -3, 0, 1]))
print(s.getMaxLen([-1, 2]))
print(s.getMaxLen([1, 2, 3, 5, -6, 4, 0, 10]))
