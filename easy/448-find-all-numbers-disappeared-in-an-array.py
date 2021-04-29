'''
找到所有数组中消失的数字
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。
'''
from typing import List
'''
思路：计数
用长度为n的数组计数
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = [0] * n
        for i in range(n):
            count[nums[i] - 1] += 1
        ans = []
        for i in range(n):
            if count[i] == 0:
                ans.append(i + 1)
        return ans
