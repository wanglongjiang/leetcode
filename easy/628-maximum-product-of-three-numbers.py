'''
三个数的最大乘积
给你一个整型数组 nums ，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

 

示例 1：

输入：nums = [1,2,3]
输出：6
示例 2：

输入：nums = [1,2,3,4]
输出：24
示例 3：

输入：nums = [-1,-2,-3]
输出：-6
 

提示：

3 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-of-three-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：贪心
如果数组中都是正数，肯定是最大的3个数之积
如果数组中有负数，结果是最大的数*max(最小的2个数乘积，第2大*第3大)

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        min1, min2, max1, max2, max3 = float('inf'), float('inf'), float('-inf'), float('-inf'), float('-inf')
        for num in nums:
            if min1 > num:
                min2 = min1
                min1 = num
            elif min2 > num:
                min2 = num
            if max1 < num:
                max3 = max2
                max2 = max1
                max1 = num
            elif max2 < num:
                max3 = max2
                max2 = num
            elif max3 < num:
                max3 = num
        return max1 * max(max2 * max3, min1 * min2) if max1 >= 0 else max1 * min(max2 * max3, min1 * min2)


s = Solution()
print(s.maximumProduct([-1, -2, -3, -4]))
print(s.maximumProduct([1, 2, 3, -4, -5]))
print(s.maximumProduct([1, 2, 3, 4, -5]))
