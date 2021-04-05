'''
最小差值 I

给你一个整数数组 A，请你给数组中的每个元素 A[i] 都加上一个任意数字 x （-K <= x <= K），从而得到一个新数组 B 。

返回数组 B 的最大值和最小值之间可能存在的最小差值。
'''
from typing import List
'''
思路：一次遍历。
一次遍历得到最大值和最小值，最小差值为max(maxVal-minVal-2K, 0)
时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        maxVal, minVal = A[0], A[0]
        for i in range(1, len(A)):
            if maxVal < A[i]:
                maxVal = A[i]
            if minVal > A[i]:
                minVal = A[i]
        return max(maxVal - minVal - 2 * K, 0)


s = Solution()
print(s.smallestRangeI(A=[1], K=0))
print(s.smallestRangeI(A=[0, 10], K=2))
print(s.smallestRangeI(A=[1, 3, 6], K=3))
