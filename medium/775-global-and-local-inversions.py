'''
775. 全局倒置与局部倒置
给你一个长度为 n 的整数数组 nums ，表示由范围 [0, n - 1] 内所有整数组成的一个排列。

全局倒置 的数目等于满足下述条件不同下标对 (i, j) 的数目：

0 <= i < j < n
nums[i] > nums[j]
局部倒置 的数目等于满足下述条件的下标 i 的数目：

0 <= i < n - 1
nums[i] > nums[i + 1]
当数组 nums 中 全局倒置 的数量等于 局部倒置 的数量时，返回 true ；否则，返回 false 。



示例 1：

输入：nums = [1,0,2]
输出：true
解释：有 1 个全局倒置，和 1 个局部倒置。
示例 2：

输入：nums = [1,2,0]
输出：false
解释：有 2 个全局倒置，和 1 个局部倒置。

提示：

n == nums.length
1 <= n <= 5000
0 <= nums[i] < n
nums 中的所有整数 互不相同
nums 是范围 [0, n - 1] 内所有数字组成的一个排列
'''
from typing import List
'''
思路：数学 贪心
从全局倒置和局部倒置的定义中看出，局部倒置属于全局倒置的一种。
也就是局部倒置的数量肯定小于等于全局倒置的数量。
只要数组中出现1个不属于局部倒置的倒置，那么肯定全局倒置的数量大于局部倒置。
如果一个倒置nums[i]>nums[i+1]，且nums[i]>i+1,那么nums[i]后面肯定有2个以上<i+1的元素，出现了不属于局部倒置的全局倒置，返回false。

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        i, n = 0, len(nums)
        while i < n:
            if i != nums[i]:  # 出现了索引与数值不匹配
                if i + 1 < n and nums[i] == i + 1 and nums[i + 1] == i:  # 是局部倒置，多跳过一个索引
                    i += 1
                else:
                    return False
            i += 1
        return True


s = Solution()
print(s.isIdealPermutation([1, 0, 2]))
print(s.isIdealPermutation([1, 2, 0]))
