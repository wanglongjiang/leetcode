'''
剑指 Offer 61. 扑克牌中的顺子
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，
可以看成任意数字。A 不能视为 14。

 

示例 1:

输入: [1,2,3,4,5]
输出: True
 

示例 2:

输入: [0,0,1,2,5]
输出: True
 

限制：

数组长度为 5 

数组的数取值为 [0, 13] .
'''
from typing import List
'''
思路：数组 哈希
遍历一次数组，找到最大值，最小值，同时确保不出现重复的数字（0除外）
然后最大值-最小值不能大于4即可

时间复杂度：O(1)
空间复杂度：O(1)
'''


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        mx, mi = float('-inf'), float('inf')
        union = set()
        for num in nums:
            if num != 0:
                if num in union:  # 不能有重复数字
                    return False
                union.add(num)
                mx = max(mx, num)
                mi = min(mi, num)
        return mx - mi <= 4
