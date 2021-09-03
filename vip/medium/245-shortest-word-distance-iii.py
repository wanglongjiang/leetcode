'''
245. 最短单词距离 III
给定一个单词列表和两个单词 word1 和 word2，返回列表中这两个单词之间的最短距离。

word1 和 word2 是有可能相同的，并且它们将分别表示为列表中两个独立的单词。

示例:
假设 words = ["practice", "makes", "perfect", "coding", "makes"].

输入: word1 = “makes”, word2 = “coding”
输出: 1
输入: word1 = "makes", word2 = "makes"
输出: 3
注意:
你可以假设 word1 和 word2 都在列表里。
'''
from typing import List
'''
思路：贪心
如果2个单词相同，找到2个最近的索引；
如果2个单词不同，遍历所有单词，遇到2个单词之一，判断：如果2个单词都有正常的索引，更新2个单词之间最近的索引，

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        ans = float('inf')
        if word1 == word2:
            preIdx = -1
            for i, word in enumerate(wordsDict):
                if word == word1:
                    if preIdx < 0:
                        preIdx = i
                    else:
                        ans = min(ans, i - preIdx)
                        preIdx = i
        else:
            idx1, idx2 = -1, -1
            for i, word in enumerate(wordsDict):
                if word == word1:
                    idx1 = i
                    if idx2 >= 0:
                        ans = min(ans, idx1 - idx2)
                elif word == word2:
                    idx2 = i
                    if idx1 >= 0:
                        ans = min(ans, idx2 - idx1)
        return ans


s = Solution()
print(s.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], 'makes', 'coding'))
print(s.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], 'makes', 'makes'))
