'''
合并石头的最低成本
有 N 堆石头排成一排，第 i 堆中有 stones[i] 块石头。

每次移动（move）需要将连续的 K 堆石头合并为一堆，而这个移动的成本为这 K 堆石头的总数。

找出把所有石头合并成一堆的最低成本。如果不可能，返回 -1 。

提示：
1 <= stones.length <= 30
2 <= K <= 30
1 <= stones[i] <= 100
'''
from typing import List
'''
思路：滑动窗口暴力扫描
每次合并，都会减少K-1次石头，最后剩1堆石头，因此stones的长度n必须为n%(K-1)==1，如果不满足这个条件，不可能。
每堆石头，如果合并了x次，相当于val*x，所以采用贪心策略，每次从中挑选K个数的序列总最小的
时间复杂度：最坏情况下O(n!)
'''


class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        pass
