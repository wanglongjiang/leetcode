'''
522. 最长特殊序列 II
给定字符串列表，你需要从它们中找出最长的特殊序列。最长特殊序列定义如下：该序列为某字符串独有的最长子序列（即不能是其他字符串的子序列）。

子序列可以通过删去字符串中的某些字符实现，但不能改变剩余字符的相对顺序。空序列为所有字符串的子序列，任何字符串为其自身的子序列。

输入将是一个字符串列表，输出是最长特殊序列的长度。如果最长特殊序列不存在，返回 -1 。



示例：

输入: "aba", "cdc", "eae"
输出: 3


提示：

所有给定的字符串长度不会超过 10 。
给定字符串列表的长度将在 [2, 50 ] 之间。
'''
from typing import List
'''
思路：排序 字符串
1. 字符串按照长度从长到短排序
2. 对于每个字符串，判断它是否是其他字符串（长度大于等于它）的子序列

时间复杂度：O(n^2*m)
空间复杂度：O(1)
'''


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(key=lambda s: -len(s))

        def isSubSeq(s1, s2):  # 判断s1是否是s2的子序列
            m, n = len(s1), len(s2)
            i, j = 0, 0
            while i < m and j < n:
                if s1[i] == s2[j]:
                    i += 1
                j += 1
            return i == m

        for i, s1 in enumerate(strs):
            isLus = True
            for j, s2 in enumerate(strs):
                if i == j:
                    continue
                if len(s1) > len(s2):
                    break
                if isSubSeq(s1, s2):
                    isLus = False
                    break
            if isLus:
                return len(s1)
        return -1


s = Solution()
print(s.findLUSlength(["aba", "cdc", "eae"]))
