'''
剑指 Offer 39. 数组中出现次数超过一半的数字

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

 

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1:

输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2
 

限制：

1 <= 数组长度 <= 50000

 

注意：本题与主站 169 题相同：https://leetcode-cn.com/problems/majority-element/
'''
from typing import List
'''
思路：摩尔投票
用1个变量candidate记录当前候选数字，用1个变量count记录出现次数
> 当nums[i]与candidate相同时，count+1
> 当nums[i]与candidate不同时，如果count为0，将candidate设置为nums[i]，如果count>0，将count-1

因为有一个数超过一半，所以，留到最后的就是这个数

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = None, 0
        for num in nums:
            if num == candidate:
                count += 1
            else:
                if count == 0:
                    candidate = num
                else:
                    count -= 1
        return candidate
