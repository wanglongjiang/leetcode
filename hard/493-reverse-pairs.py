'''
翻转对
给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。

你需要返回给定数组中的重要翻转对的数量。

注意:

给定数组的长度不会超过50000。
输入数组中的所有数字都在32位整数的表示范围内。
'''
from typing import List
'''
思路1，暴力搜索
从第1个开始，搜索后续每个nums[i]>2*nums[j]，需要2重循环
时间复杂度：O(n^2)
空间复杂度：O(1)

思路2，最小堆
从右向左建立最小堆，在建堆过程中查找堆中小于nums[i]/2的值的数量
时间复杂度：建堆需要O(nlogn)，查找过程需要使用dfs，最坏情况下是O(n^2)

思路3，线段树

'''


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        pass
