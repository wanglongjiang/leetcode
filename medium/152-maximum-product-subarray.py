'''
乘积最大子数组
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
'''
from typing import List
'''
思路，双指针。
0与任何数的乘积都是0，因此可以将数组看成被0分割的子数组，在各个子数组中查找乘积最大的值。
在一个非0的数组中求最大乘积，需要分析正负性。
    没有负数或者负数为偶数个，最大乘积就是整个数组的乘积
    有奇数个负数，如果第i个元素为负数，则[start,i-1]，[i+1,end]这2个区间的乘积都是最大乘积的候选。
通过下面2个指针交替移动算法可以计算所有[start,i-1]和[i+1,end]的乘积。
1、right指针向右移动，mul累计left至right指针之间的乘积，直至right遇到0或末尾。
2、向右移动left指针，mul除以被移出子数组的元素。
重复以上过程直至left指针移动到末尾。
时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        left, right, n = 0, 0, len(nums)
        mul, product = 1, float('-inf')
        while left < n:
            while right < n and nums[right] != 0:  # 移动right指针直至遇到0，这中间用mul累计乘积，product记录最大的乘积
                mul *= nums[right]
                right += 1
                product = max(product, mul)
            while left + 1 < right:  # 移动left指针，这中间用mul累计乘积，product记录最大的乘积
                mul /= nums[left]
                left += 1
                product = max(product, mul)
            while right < n and nums[right] == 0:  # 跳过0
                product = max(product, 0)  # 有可能所有子数组的乘积都小于0，所以0也是候选
                right += 1
            left = right
            mul = 1
        return int(product)


s = Solution()
print(s.maxProduct([-2, 0, -1]))
print(s.maxProduct([2, 3, -2, 4]))
