'''
剑指 Offer 53 - II. 0～n-1中缺失的数字
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

 

示例 1:

输入: [0,1,3]
输出: 2
示例 2:

输入: [0,1,2,3,4,5,6,7,9]
输出: 8
 

限制：

1 <= 数组长度 <= 10000
'''
from typing import List
'''
思路1，数组
设一个大小为n的数组arr，每个元素初始化为False，遍历nums，设置arr[nums[i]]为True
经过上面的处理后，只剩下缺少的arr[x]为False，遍历一次arr即可找出
时间复杂度：O(n)
空间复杂度：O(n)

思路2，数学
0~n-1的总和是sum= n*(n+1)/2
可以用sum减去nums中所有元素，最后余数即为缺少的数
时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)
