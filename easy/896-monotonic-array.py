'''
单调数列
如果数组是单调递增或单调递减的，那么它是单调的。

如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。

当给定的数组 A 是单调数组时返回 true，否则返回 false。
'''
from typing import List
'''
思路：遍历数组，用一个变量记录2个相邻整数差，如果正负发生变化，返回false
'''


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        diff = 0
        for i in range(1, len(A)):
            if A[i - 1] != A[i]:
                if diff == 0:
                    diff = A[i] - A[i - 1]
                elif diff > 0 and A[i] - A[i - 1] < 0:
                    return False
                elif diff < 0 and A[i] - A[i - 1] > 0:
                    return False
        return True


s = Solution()
print(s.isMonotonic([1, 2, 2, 3]))
print(s.isMonotonic([6, 5, 4, 4]))
print(s.isMonotonic([1, 3, 2]))
print(s.isMonotonic([1, 2, 4, 5]))
print(s.isMonotonic([1, 1, 1]))
