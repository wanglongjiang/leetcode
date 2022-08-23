'''
2195. 向数组中追加 K 个整数
给你一个整数数组 nums 和一个整数 k 。请你向 nums 中追加 k 个 未 出现在 nums 中的、互不相同 的 正 整数，并使结果数组的元素和 最小 。

返回追加到 nums 中的 k 个整数之和。

 

示例 1：

输入：nums = [1,4,25,10,25], k = 2
输出：5
解释：在该解法中，向数组中追加的两个互不相同且未出现的正整数是 2 和 3 。
nums 最终元素和为 1 + 4 + 25 + 10 + 25 + 2 + 3 = 70 ，这是所有情况中的最小值。
所以追加到数组中的两个整数之和是 2 + 3 = 5 ，所以返回 5 。
示例 2：

输入：nums = [5,6], k = 6
输出：25
解释：在该解法中，向数组中追加的两个互不相同且未出现的正整数是 1 、2 、3 、4 、7 和 8 。
nums 最终元素和为 5 + 6 + 1 + 2 + 3 + 4 + 7 + 8 = 36 ，这是所有情况中的最小值。
所以追加到数组中的两个整数之和是 1 + 2 + 3 + 4 + 7 + 8 = 25 ，所以返回 25 。
 

提示：

1 <= nums.length <= 105
1 <= nums[i], k <= 109
'''

from typing import List
'''
思路：贪心
如果想要得到的数组元素和最小，要添加的数应该是从1开始的自然数，
设n=len(nums)，那么要添加的子数组取值范围为[1, n+k]，设n+k=m，即为[1,m]，其和为s
这种情况下的s，它是n+k个元素的和，比起答案多了n个元素，下一步需要将n个元素从s中减掉。
如果nums[i]<=m，
    如果nums[i]第1次出现，该数值占用了[1,m]的一个位置，该数值需要从s中减去。
    如果nums[i]出现了超过1次，该数值已经之前已经从s中减掉，它不占用[1,m]的位置，但[1,m]又多出了1个数值，需要从大到小减掉m。
如果nums[i]>m，它不占用[1,m]的位置，但[1,m]又多出了1个数值，需要从大到小减掉m。

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        m = len(nums) + k
        s = m * (m + 1) // 2
        nset = set()
        nums.sort()
        for num in nums:
            if num <= m and num not in nset:
                nset.add(num)
                s -= num
            else:
                s -= m
                m -= 1
        return s


s = Solution()
print(s.minimalKSum([96, 44, 99, 25, 61, 84, 88, 18, 19, 33, 60, 86, 52, 19, 32, 47, 35, 50, 94, 17, 29, 98, 22, 21, 72, 100, 40, 84], 35) == 794)  # TODO
print(s.minimalKSum(nums=[1, 4, 25, 10, 25], k=2))
print(s.minimalKSum(nums=[5, 6], k=6))