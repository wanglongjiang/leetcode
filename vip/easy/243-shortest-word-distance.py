'''
243. 最短单词距离
给定一个单词列表和两个单词 word1 和 word2，返回列表中这两个单词之间的最短距离。

示例:
假设 words = ["practice", "makes", "perfect", "coding", "makes"]

输入: word1 = “coding”, word2 = “practice”
输出: 3
输入: word1 = "makes", word2 = "coding"
输出: 1
注意:
你可以假设 word1 不等于 word2, 并且 word1 和 word2 都在列表里。
'''
from typing import List
'''
思路：数组的遍历
便利一次数组，如果元素等于2个单词之一，更新他们的索引，计算距离

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        n, idx1, idx2 = len(wordsDict), float('inf'), float('inf')
        ans = float('inf')
        for i, word in enumerate(wordsDict):
            if word == word1:
                idx1 = i
            elif word == word2:
                idx2 = i
            if idx1 < n and idx2 < n:
                ans = min(ans, abs(idx1 - idx2))
        return ans


s = Solution()
print(s.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", word2="practice"))
print(s.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", word2="coding"))
