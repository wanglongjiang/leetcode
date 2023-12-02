'''
[TOC]

# 思路
贪心

# 解题方法
按照2、4、6、8...的等差序列进行拆分，余数加到序列中最大的那个上

# 复杂度
- 时间复杂度: 
> $O(logn)$ 

- 空间复杂度: 
> $O(1)$
'''

from typing import List


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum & 1:
            return []
        # 二分查找该偶数可以拆分成多大的数组
        size = 1
        low, high = 1, int(finalSum**0.5) + 1
        while low < high:
            size = (low + high) // 2
            seqSum = size * (2 + 2 * size) // 2  # 计算2.4.6.8...这个序列的和
            if seqSum < finalSum:
                low = size + 1
            elif seqSum == finalSum:
                high = low
            else:
                high = size
        ans = [2 * (i + 1) for i in range(size)]
        seqSum = (size) * (2 + 2 * (size)) // 2
        if seqSum < finalSum:
            ans[-1] += finalSum - seqSum
        elif seqSum > finalSum:
            diff = ans.pop() - (seqSum - finalSum)
            ans[-1] += diff
        return ans


s = Solution()
assert s.maximumEvenSplit(10) == [2, 8]
assert s.maximumEvenSplit(28) == [2, 4, 6, 16]
assert s.maximumEvenSplit(12) == [2, 4, 6]
assert s.maximumEvenSplit(7) == []
