'''
1874. 两个数组的最小乘积和
给定两个长度相等的数组a和b，它们的乘积和为数组中所有的a[i] * b[i]之和，其中0 <= i < a.length。

比如a = [1,2,3,4]，b = [5,2,3,1]时，它们的乘积和为1*5 + 2*2 + 3*3 + 4*1 = 22
现有两个长度都为n的数组nums1和nums2，你可以以任意顺序排序nums1，请返回它们的最小乘积和。

示例 1:

输入: nums1 = [5,3,4,2], nums2 = [4,2,2,5]
输出: 40
解释: 将 num1 重新排列为 [3,5,4,2] 后，可由 [3,5,4,2] 和 [4,2,2,5] 得到最小乘积和 3*4 + 5*2 + 4*2 + 2*5 = 40。
示例 2:

输入: nums1 = [2,1,4,5,7], nums2 = [3,2,4,8,6]
输出: 65
解释: 将 num1 重新排列为 [5,7,4,1,2] 后，可由 [5,7,4,1,2] 和 [3,2,4,8,6] 得到最小乘积和 5*3 + 7*2 + 4*4 + 1*8 + 2*6 = 65。


提示:

n == nums1.length == nums2.length
1 <= n <= 10^5
1 <= nums1[i], nums2[i] <= 100
'''
from typing import List
'''
思路：贪心 排序
因为都是>=1的数值，可以将2个数组进行排序，一个数组的最大值乘另外一个数组的最小值，得到最小成绩和

时间复杂度：O(nlogn)
空间复杂度：O(1)
'''


class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        return sum(map(lambda p: p[0] * p[1], zip(sorted(nums1, reverse=True), sorted(nums2))))


s = Solution()
print(s.minProductSum(nums1=[5, 3, 4, 2], nums2=[4, 2, 2, 5]))
print(s.minProductSum(nums1=[2, 1, 4, 5, 7], nums2=[3, 2, 4, 8, 6]))
