'''
最大连续1的个数 III

给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。

返回仅包含 1 的最长（连续）子数组的长度。
'''
from typing import List
'''
解题思路：滑动窗口
遍历数组A，2个指针分别指向开始和当前字符，将遇到的第1个0转为2，直至K=0，
此后如果再遇到0，最大长度记录下来，将最左边的指针向前滚动至遇到的第1个2，后面，同时2翻转为0
右边指针继续向前滚动
时间复杂度：O(N),空间复杂度O(1)
'''


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        maxLen, currentLen = 0, 0
        left = 0
        for right in range(len(A)):
            if A[right]:
                currentLen += 1
            else:
                if K > 0:
                    K -= 1
                    A[right] = 2
                    currentLen += 1
                else:
                    maxLen = max(maxLen, currentLen)
                    # 滑动左边指针直至遇到1个原先的0
                    while A[left] == 1:
                        left += 1
                    # 恢复原值0
                    A[left] = 0
                    # 左边指针指向下一个元素
                    left += 1
                    currentLen = right - left + 1
        currentLen = right - left + 1
        maxLen = max(maxLen, currentLen)
        return maxLen


s = Solution()
print(s.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
print(
    s.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
                  3))
