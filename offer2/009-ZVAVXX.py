'''
剑指 Offer II 009. 乘积小于 K 的子数组
给定一个正整数数组 nums和整数 k ，请找出该数组内乘积小于 k 的连续的子数组的个数。

 

示例 1:

输入: nums = [10,5,2,6], k = 100
输出: 8
解释: 8 个乘积小于 100 的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于100的子数组。
示例 2:

输入: nums = [1,2,3], k = 0
输出: 0
 

提示: 

1 <= nums.length <= 3 * 10^4
1 <= nums[i] <= 1000
0 <= k <= 10^6
 

注意：本题与主站 713 题相同：https://leetcode-cn.com/problems/subarray-product-less-than-k/ 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ZVAVXX
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：滑动窗口
设left,right指针，2个指针构成滑动窗口。初始都指向0。
设变量product，它为滑动窗口内元素的乘积，初始为nums[0]。
当product*nums[right+1]<k时，向右移动right指针，此时以right为结尾的子数组都是符合要求，ans+= right-left+1
当product*nums[right+1]>=k时，向左移动left指针，直至<k。

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = 0, 0
        product = nums[0]
        ans = 0
        while right < n:
            while product < k:  # 累乘，直至窗口内元素和>=k
                ans += right - left + 1  # 以right为截止的子串数量为right-left+1
                if right + 1 < n:
                    right += 1
                    product *= nums[right]  # 累乘
                else:
                    break
            if product < k and right == n - 1:  # 如果到了末尾，乘积仍然小于k，不需要继续遍历了
                break
            while left < n and left < right and product >= k:  # 将窗口左侧元素依次移出，直至乘积小于k
                product /= nums[left]
                left += 1
            if left < n and left == right and product >= k:  # 单个元素值超过k，需要向右移动窗口
                left += 1
                right += 1
                if left < n:
                    product = nums[left]
        return ans


s = Solution()
print(s.numSubarrayProductLessThanK([10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3], 19))
print(s.numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100))
# 1,2,3,4,3:6,8:7,3:8,3:10,6:12,2:14,10:15,10:16,9:17,3:18
print(s.numSubarrayProductLessThanK(nums=[1, 2, 3], k=0))
