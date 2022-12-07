'''
1775. 通过最少操作次数使数组的和相等
中等
65
相关企业
给你两个长度可能不等的整数数组 nums1 和 nums2 。两个数组中的所有值都在 1 到 6 之间（包含 1 和 6）。

每次操作中，你可以选择 任意 数组中的任意一个整数，将它变成 1 到 6 之间 任意 的值（包含 1 和 6）。

请你返回使 nums1 中所有数的和与 nums2 中所有数的和相等的最少操作次数。如果无法使两个数组的和相等，请返回 -1 。

 

示例 1：

输入：nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
输出：3
解释：你可以通过 3 次操作使 nums1 中所有数的和与 nums2 中所有数的和相等。以下数组下标都从 0 开始。
- 将 nums2[0] 变为 6 。 nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2] 。
- 将 nums1[5] 变为 1 。 nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2] 。
- 将 nums1[2] 变为 2 。 nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2] 。
示例 2：

输入：nums1 = [1,1,1,1,1,1,1], nums2 = [6]
输出：-1
解释：没有办法减少 nums1 的和或者增加 nums2 的和使二者相等。
示例 3：

输入：nums1 = [6,6], nums2 = [1]
输出：3
解释：你可以通过 3 次操作使 nums1 中所有数的和与 nums2 中所有数的和相等。以下数组下标都从 0 开始。
- 将 nums1[0] 变为 2 。 nums1 = [2,6], nums2 = [1] 。
- 将 nums1[1] 变为 2 。 nums1 = [2,2], nums2 = [1] 。
- 将 nums2[0] 变为 4 。 nums1 = [2,2], nums2 = [4] 。
 

提示：

1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[i] <= 6
'''
from typing import List
'''
[TOC]

# 思路
计数 贪心

# 解题方法
首先，计算2个数组的和。如果2个数组大小不一致，那么需要将大数组里面的值变小，小数组里面的值变大。如果想要操作次数最少，小数组的1变成6，大数组的6变成1收益最大。

基于上面的贪心思路，对2个数组的1~6进行计数，小数组从小到大，依次将1~5变成6，大数组从大到小，依次将6~2变成1，找到最小的变动次数。

# 复杂度
- 时间复杂度: 
> $O(n)$ 

- 空间复杂度: 
> $O(1)$
'''


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        if sum1 == sum2:
            return 0
        if sum1 > sum2:  # 确保nums1是较小的数组
            nums1, nums2 = nums2, nums1
        counter1, counter2 = [0] * 7, [0] * 7
        for num in nums1:
            counter1[num] += 1
        for num in nums2:
            counter2[num] += 1
        diff = abs(sum1 - sum2)
        ans = 0
        for i in range(1, 6):
            ans += min(diff // (6 - i) + (1 if diff % (6 - i) else 0), counter1[i])  # 将较小数组里面的数字i变成6
            diff = max(0, diff - counter1[i] * (6 - i))
            ans += min(diff // (6 - i) + (1 if diff % (6 - i) else 0), counter2[6 - i + 1])  # 将较大数组里面的数字i变成1
            diff = max(0, diff - counter2[6 - i + 1] * (6 - i))
        return ans if diff == 0 else -1


s = Solution()
assert s.minOperations(nums1=[6, 6], nums2=[1]) == 3
assert s.minOperations(nums1=[1, 2, 3, 4, 5, 6], nums2=[1, 1, 2, 2, 2, 2]) == 3
