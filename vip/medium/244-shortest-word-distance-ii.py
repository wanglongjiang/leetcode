'''
244. 最短单词距离 II
请设计一个类，使该类的构造函数能够接收一个单词列表。然后再实现一个方法，该方法能够分别接收两个单词 word1 和 word2，
并返回列表中这两个单词之间的最短距离。您的方法将被以不同的参数调用 多次。

示例:
假设 words = ["practice", "makes", "perfect", "coding", "makes"]

输入: word1 = "coding", word2 = "practice"
输出: 3
输入: word1 = "makes", word2 = "coding"
输出: 1
注意:
你可以假设 word1 不等于 word2, 并且 word1 和 word2 都在列表里。
'''
from typing import List
from collections import defaultdict
import bisect
'''
思路：哈希 二分查找
1、初始化函数，已单词作为key，list作为value，list中存放单词所有的索引
2、shortest函数，二分查找所有的索引，找到距离最近的

时间复杂度：O(nlogn)
'''


class WordDistance:
    def __init__(self, wordsDict: List[str]):
        self.indexs = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.indexs[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        li1, li2 = self.indexs[word1], self.indexs[word2]
        if len(li1) < len(li2):  # 确保较长的为li2，二分查找较长的li2
            li1, li2 = li2, li1
        ans = float('inf')
        for i in li1:
            idx = bisect.bisect(li2, i)
            if idx > 0:
                ans = min(ans, i - li2[idx - 1])
            if idx < len(li2):
                ans = min(ans, li2[idx] - i)
        return ans


s = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
print(s.shortest(word1="coding", word2="practice"))
print(s.shortest(word1="makes", word2="coding"))
