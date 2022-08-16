'''
1858. 包含所有前缀的最长单词
给定一个字符串数组 words，找出 words 中所有的前缀都在 words 中的最长字符串。

例如，令 words = ["a", "app", "ap"]。字符串 "app" 含前缀 "ap" 和 "a" ，都在 words 中。
返回符合上述要求的字符串。如果存在多个（符合条件的）相同长度的字符串，返回字典序中最小的字符串，如果这样的字符串不存在，返回 ""。



示例 1:

输入： words = ["k","ki","kir","kira", "kiran"]
输出： "kiran"
解释： "kiran" 含前缀 "kira"、 "kir"、 "ki"、 和 "k"，这些前缀都出现在 words 中。
示例 2:

输入： words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
输出： "apple"
解释： "apple" 和 "apply" 都在 words 中含有各自的所有前缀。
然而，"apple" 在字典序中更小，所以我们返回之。
示例 3:

输入： words = ["abc", "bc", "ab", "qwe"]
输出： ""


提示：

1 <= words.length <= 10^5
1 <= words[i].length <= 10^5
1 <= sum(words[i].length) <= 10^5
'''
from typing import List
'''
思路：排序 字典树
首先，单词按照长度进行排序，用字典树依次保存前缀在字典树中的单词。
然后，遍历字典树中长度最长的单词，找到字典序最小的。


时间复杂度：O(mn)，m=words.length,n=words[i].length
空间复杂度：O(mn)，最坏情况下字典树需要保存所有的单词
'''


class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = {}  # 字典树根节点
        words.sort(key=lambda word: len(word))  # 按照长度排序，加入字典树时确保前缀先加入
        endwords = []

        def add(word):
            node = root
            for i, char in enumerate(word):
                if char not in node:
                    if i != len(word) - 1:  # 如果前缀不在字典树中，该单词不符合要求
                        return
                    node[char] = {}
                node = node[char]
            endwords.append(word)

        for word in words:
            add(word)
        if not endwords:
            return ""
        # 找到长度最长的单词中字典序最小的
        maxlen = max(map(len, endwords))
        return min(filter(lambda word: len(word) == maxlen, endwords))


s = Solution()
print(s.longestWord(["k", "ki", "kir", "kira", "kiran"]))
print(s.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))
print(s.longestWord(["abc", "bc", "ab", "qwe"]))
