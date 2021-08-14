'''
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
'''
'''
思路：KMP算法
用KMP算法进行字符串查找。
1. 首先预处理needle，创建dfa
2. 执行查找过程

时间复杂度：O(m+n),m=len(needle),n=len(haystack)
空间复杂度：O(m)
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        m, n = len(needle), len(haystack)
        dfa = [[0] * m for _ in range(26)]
        dfa[ord(needle[0]) - ord('a')][0] = 1
        x = 0
        for i in range(1, m):
            for c in range(26):
                dfa[c][i] = dfa[c][x]  # 复制匹配失败的值
            charIdx = ord(needle[i]) - ord('a')
            dfa[charIdx][i] = i + 1  # 设置匹配成功的值
            x = dfa[charIdx][x]
        i, j = 0, 0
        while i < n and j < m:
            j = dfa[ord(haystack[i]) - ord('a')][j]
            i += 1
        if j == m:
            return i - m
        return -1
