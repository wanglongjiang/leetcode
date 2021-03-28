'''
最大间距

给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。

如果数组元素个数小于 2，则返回 0。
你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。
'''
from typing import List
'''
思路：桶排序。
基于比较的算法上限就是O(nlogn)，没有办法达到O(n)
先找出最大值、最小值max,min，(max-min)/(n+1)即为桶的大小
一个数的桶索引是(num-min)/(max-min)*(n+1)，优化下算法，r = max-min，bucketLen=n+1, index = bucketLen*(num-min)//r
最大差出现在1个桶的最小值-前一个桶内最大值。
不会出现在桶内，因为桶内最大差<buketSize = (max-min)/(n+1)。而因为桶有n+1个，必然有空桶存在，也就是最大差必然大于buketSize
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        pass
