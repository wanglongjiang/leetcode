'''
面试题 01.01. 判定字符是否唯一
实现一个算法，确定一个字符串 s 的所有字符是否全都不同。

示例 1：

输入: s = "leetcode"
输出: false
示例 2：

输入: s = "abc"
输出: true
限制：

0 <= len(s) <= 100
如果你不使用额外的数据结构，会很加分。
'''
'''
思路：迭代
如果不用额外的数据结构，使用2重迭代，对比任意2个字符

时间复杂度：O(n^2)
空间复杂度：O(1)
'''


class Solution:
    def isUnique(self, astr: str) -> bool:
        for i in range(len(astr) - 1):
            for j in range(i + 1, len(astr)):
                if astr[i] == astr[j]:
                    return False
        return True
