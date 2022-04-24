'''
爱吃香蕉的珂珂

珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。

珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  

珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。

 

示例 1：

输入: piles = [3,6,7,11], H = 8
输出: 4
示例 2：

输入: piles = [30,11,23,4,20], H = 5
输出: 30
示例 3：

输入: piles = [30,11,23,4,20], H = 6
输出: 23
 

提示：

1 <= piles.length <= 10^4
piles.length <= H <= 10^9
1 <= piles[i] <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/koko-eating-bananas
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：二分查找
k最大可能是piles中的最大值（h与piles.length相同时）
k最小可能是1
所以可以用二分查找，在1..max(piles)中选择一个值mid，
用piles[i]除以mid得到这堆香蕉能吃多长时间，一次猜测过程中需要合计所有的时间time
如果time<=h，时间有富裕，需要继续缩小mid的大小
如果time>h,时间不够，需要增加mid的大小

时间复杂度：O(nlogn)
空间复杂度：O(1)
'''


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        start, end = 1, max(piles)
        while start < end:
            mid = (start + end) // 2
            time = 0
            for i in range(n):
                time += (piles[i] + mid - 1) // mid
            if time <= h:
                end = mid
            else:
                start = mid + 1
        return end
