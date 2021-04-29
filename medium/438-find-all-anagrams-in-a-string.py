'''
找到字符串中所有字母异位词

给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：

字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。
'''
from typing import List
'''
思路：计数
因为只有英文字母，可以将p中的字符进行计数，得到长度为26的数组pcount，存储每个字母的计数
然后设一个长度为len(p)的滑动窗口，记录s中子串的字母计数scount，如果scount=pcount则找到1个位置
时间复杂度：O(26*n)
空间复杂度：O(1)
'''


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        m, n = len(p), len(s)
        base = ord('a')
        if len(s) < m:
            return ans
        pcount = [0] * 26
        for c in p:
            pcount[ord(c) - base] += 1
        scount = [0] * 26
        for i in range(m):
            scount[ord(s[i]) - base] += 1
        if scount == pcount:
            ans.append(0)
        i = 0
        while i + m < n:
            scount[ord(s[i]) - base] -= 1
            scount[ord(s[i + m]) - base] += 1
            i += 1
            if scount == pcount:
                ans.append(i)
        return ans


s = Solution()
print(s.findAnagrams("cbaebabacd", "abc"))
print(s.findAnagrams("abab", "ab"))
