'''
猜字谜
外国友人仿照中国字谜设计了一个英文版猜字谜小游戏，请你来猜猜看吧。

字谜的迷面 puzzle 按字符串形式给出，如果一个单词 word 符合下面两个条件，那么它就可以算作谜底：

单词 word 中包含谜面 puzzle 的第一个字母。
单词 word 中的每一个字母都可以在谜面 puzzle 中找到。
例如，如果字谜的谜面是 "abcdefg"，那么可以作为谜底的单词有 "faced", "cabbage", 和 "baggage"；而 "beefed"（不含字母 "a"）以及 "based"（其中的 "s" 没有出现在谜面中）。
返回一个答案数组 answer，数组中的每个元素 answer[i] 是在给出的单词列表 words 中可以作为字谜迷面 puzzles[i] 所对应的谜底的单词数目。

'''

from typing import List
'''
解题思路：
words的长度为n 10^5，单个单词长度为k <=50
puzzles的长度为m 10^4，单个长度为7
一、暴力算法。针对每个puzzle，遍历words，检查其是否满足条件（word中包含puzzle的首字母，word中所有的字母都在puzzle中出行）
时间复杂度：O(m*n*k) 数据量最大情况下： 5*10^10，空间复杂度为O(1)

二、位映射算法。对于puzzle和word中都是小写字母26个，而且我们对其中每个字符出现几次是不关心的，关心的是word中的字符全部在puzzles中。
基于这个考虑，可以将单词中的一个字符映射到整数中的位，位移为ascii(char)-ascii('a')，可以将puzzle转化为2个整数：1、首字母位映射整数h，2、puzzle的所有字母的映射反码mask
word也转化为映射整数w，如果满足h&w>0 and mask&w==0，则该Word为谜底的单词
转化需要的时间：m*7+n*k
匹配需要的时间:m*n
时间复杂度:O(m*n+n*k+m*7) 数据量最大情况下：10^9+5*10^6+7*10^4，比暴力算法低了1个数量级
空间复杂度：需要puzzles映射整数数组O(m+n)
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        m = len(puzzles)
        heads, masks, answer = [0] * m, [0] * m, [0] * m
        base = ord('a')
        for i in range(m):
            heads[i] = 1 << ord(puzzles[i][0]) - base
            for j in range(7):
                masks[i] |= 1 << ord(puzzles[i][j]) - base
            masks[i] = ~masks[i]
        for word in words:
            wordmap = 0
            for j in range(len(word)):
                wordmap |= 1 << ord(word[j]) - base
            for i in range(m):
                if heads[i] & wordmap > 0 and masks[i] & wordmap == 0:
                    answer[i] += 1
        return answer

三、位映射算法仍然超出时间限制。根据首字母信息，对masks进行划片优化，优化后时间与word中字母集合大小有关，如果字母集合平均为4
相比上面的算法，会加快26/4倍
时间复杂度没有数量级的降低
'''


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        m = len(puzzles)
        masks, answer = [0] * m, [0] * m
        heads = [0] * 26
        masksMap = {}
        charMaps = {}
        base = ord('a')
        for i in range(26):
            heads[i] = 1 << i
            masksMap[heads[i]] = []
            charMaps[chr(base + i)] = heads[i]
        wordSet = set()
        for i in range(m):
            head = charMaps[puzzles[i][0]]
            for j in range(7):
                masks[i] |= charMaps[puzzles[i][j]]
            masks[i] = ~masks[i]
            masksMap[head].append(i)
        for word in words:
            wordSet.add(word)
        for word in words:
            wordmap = 0
            charSets = set()
            for j in range(len(word)):
                charMap = charMaps[word[j]]
                charSets.add(charMap)
                wordmap |= charMap
            for charMap in charSets:
                for index in masksMap[charMap]:
                    if masks[index] & wordmap == 0:
                        answer[index] += 1
        return answer


s = Solution()
print(s.findNumOfValidWords(["aaaa", "asas", "able", "ability", "actt", "actor", "access"], ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]))
