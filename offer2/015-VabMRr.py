'''
剑指 Offer II 015. 字符串中的所有变位词
给定两个字符串 s 和 p，找到 s 中所有 p 的 变位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

变位词 指字母相同，但排列不同的字符串。

 

示例 1:

输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的变位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的变位词。
 示例 2:

输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的变位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的变位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的变位词。
 

提示:

1 <= s.length, p.length <= 3 * 10^4
s 和 p 仅包含小写字母
 

注意：本题与主站 438 题相同： https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/VabMRr
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
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
