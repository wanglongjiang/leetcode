'''
K 连续位的最小翻转次数

在仅包含 0 和 1 的数组 A 中，一次 K 位翻转包括选择一个长度为 K 的（连续）子数组，同时将子数组中的每个 0 更改为 1，而每个 1 更改为 0。

返回所需的 K 位翻转的最小次数，以便数组没有值为 0 的元素。如果不可能，返回 -1。
'''
from typing import List
'''
思路：滑动窗口
'''


class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        length = len(A)
        flipNum = 0
        flipCount = 0
        for i in range(length):
            if i >= K and A[i - K] > 1:
                flipCount ^= 1
                A[i - K] -= 2
            if A[i] == flipCount:
                if i + K > length:
                    return -1
                flipNum += 1
                flipCount ^= 1
                A[i] += 2
        return flipNum


s = Solution()
print(s.minKBitFlips([0, 1, 0], 1))
print(s.minKBitFlips([1, 1, 0], 2))
print(s.minKBitFlips([0, 0, 0, 1, 0, 1, 1, 0], 3))
