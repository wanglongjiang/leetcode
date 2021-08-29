'''
408. 有效单词缩写
给一个 非空 字符串 s 和一个单词缩写 abbr ，判断这个缩写是否可以是给定单词的缩写。

字符串 "word" 的所有有效缩写为：

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
注意单词 "word" 的所有有效缩写仅包含以上这些。任何其他的字符串都不是 "word" 的有效缩写。

注意:
假设字符串 s 仅包含小写字母且 abbr 只包含小写字母和数字。

示例 1:

给定 s = "internationalization", abbr = "i12iz4n":

函数返回 true.


示例 2:

给定 s = "apple", abbr = "a2e":

函数返回 false.
'''
'''
思路：字符串遍历
遍历abbr所有字符，如果是字母，与word当前字符必须相同
如果是数值，word指针需要跳过指定的数值

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        m, n = len(word), len(abbr)
        i, j = 0, 0
        while i < m and j < n:
            if abbr[j].isdigit():
                k = j
                while k < n and abbr[k].isdigit():
                    k += 1
                count = int(abbr[j:k])
                if count + i > m:
                    return False
                i += count
                j = k
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        return i == m and j == n


s = Solution()
print(s.validWordAbbreviation("internationalization", abbr="i12iz4n"))
print(s.validWordAbbreviation("apple", abbr="a2e"))
