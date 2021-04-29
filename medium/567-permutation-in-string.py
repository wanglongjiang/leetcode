'''
字符串的排列
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的 子串 。
提示：

输入的字符串只包含小写字母
两个字符串的长度都在 [1, 10,000] 之间
'''
'''
思路：滑动窗口计数
与438题类似，因为输入都是小写字母，可以使用长度为26的数组存储s1的各字母计数
然后使用滑动窗口遍历s2，判断滑动窗内的计数是否与s1的计数相同
时间复杂度：O(26*n)
空间复杂度：O(1)
'''


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        base = ord('a')
        if n2 < n1:
            return False
        pcount = [0] * 26
        for c in s1:
            pcount[ord(c) - base] += 1
        scount = [0] * 26
        for i in range(n1):
            scount[ord(s2[i]) - base] += 1
        if scount == pcount:
            return True
        i = 0
        while i + n1 < n2:
            scount[ord(s2[i]) - base] -= 1
            scount[ord(s2[i + n1]) - base] += 1
            i += 1
            if scount == pcount:
                return True
        return False


s = Solution()
print(s.checkInclusion(s1="ab", s2="eidbaooo"))
print(s.checkInclusion(s1="ab", s2="eidboaoo"))
