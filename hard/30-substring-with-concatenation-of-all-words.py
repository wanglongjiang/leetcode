'''
串联所有单词的子串
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

'''
from typing import List
'''
思路：滑动窗口
'''


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordLen = len(words[0])
        wordNum = len(words)
        wordsMap = {}
        for word in words:
            if word in wordsMap:
                wordsMap[word] += 1
            else:
                wordsMap[word] = 1
        ans = []
        i = 0
        while i <= len(s) - (wordLen * wordNum):
            tmpMap = wordsMap.copy()
            wd = s[i:i + wordLen]
            if wd in tmpMap:
                tmpMap[wd] -= 1
                for j in range(i + wordLen, i + wordNum * wordLen, wordLen):
                    wd = s[j:j + wordLen]
                    if wd not in tmpMap:
                        break
                    if tmpMap[wd] == 0:
                        break
                    tmpMap[wd] -= 1
                else:
                    ans.append(i)
            i += 1
        return ans


s = Solution()
print(s.findSubstring("aaaaaaaaaaaaaa", ["aa", "aa"]))
print(s.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))
print(s.findSubstring("barfoothefoobarman", ["foo", "bar"]))
print(s.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))
