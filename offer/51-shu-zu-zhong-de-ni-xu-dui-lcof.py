'''
剑指 Offer 51. 数组中的逆序对

在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

 

示例 1:

输入: [7,5,6,4]
输出: 5
 

限制：

0 <= 数组长度 <= 50000
'''
from typing import List
from sortedcontainers import SortedList
'''
思路：有序集合
设一个sortedList（有序集合），从右至左遍历数组，对于当前元素nums[i]
> 查询sortedList中<nums[i]的元素个数，所有这些元素可以与nums[i]构成逆序对，个数累计到结果中
> 让后将nums[i]插入sortedList（有序集合）中

时间复杂度：O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        li = SortedList()
        ans = 0
        for i in range(len(nums) - 1, -1, -1):
            ans += li.bisect_left(nums[i])
            li.add(nums[i])
        return ans
