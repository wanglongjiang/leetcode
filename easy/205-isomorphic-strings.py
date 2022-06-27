'''
同构字符串
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，
字符可以映射到自己本身。
'''
'''
思路：用哈希表维护s中的字符到t中的字符的映射关系
时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp, mp2 = {}, {}
        for i in range(len(s)):
            sc = s[i]
            if sc in mp:
                if mp[sc] != t[i]:
                    return False
            else:
                if t[i] in mp2:
                    return False
                mp[sc] = t[i]
                mp2[t[i]] = sc
        return True


s = Solution()
print(s.isIsomorphic("badc", "baba"))
print(s.isIsomorphic(s="egg", t="add"))
print(s.isIsomorphic(s="foo", t="bar"))
print(s.isIsomorphic(s="paper", t="title"))
