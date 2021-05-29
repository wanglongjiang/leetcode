'''
连接词
给定一个 不含重复 单词的字符串数组 words ，编写一个程序，返回 words 中的所有 连接词 。

连接词 的定义为：一个字符串完全是由至少两个给定数组中的单词组成的。

 

示例 1：

输入：words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
输出：["catsdogcats","dogcatsdog","ratcatdogcat"]
解释："catsdogcats"由"cats", "dog" 和 "cats"组成;
     "dogcatsdog"由"dog", "cats"和"dog"组成;
     "ratcatdogcat"由"rat", "cat", "dog"和"cat"组成。
示例 2：

输入：words = ["cat","dog","catdog"]
输出：["catdog"]
 

提示：

1 <= words.length <= 10^4
0 <= words[i].length <= 1000
words[i] 仅由小写字母组成
0 <= sum(words[i].length) <= 6 * 10^5
'''
from typing import List
'''
思路：字典树+深度优先搜索
1. 将字符串从小到达排序
2. 遍历排序好的字符串，然后深度优先查询字符串的各个子串是否都在字典树中，最后将字符串插入字典树

时间复杂度：O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=lambda word: len(word))
        trie = {}
        endIds = set()

        # 添加字符串到字典树中
        def add(word):
            node = trie
            for i in range(len(word)):
                if word[i] not in node:
                    node[word[i]] = {}
                node = node[word[i]]
            endIds.add(id(node))

        # 在字典树中深度优先查找单词的各个构成
        def dfs(word, start):
            node = trie
            for i in range(start, len(word)):
                if word[i] not in node:
                    return False
                node = node[word[i]]
                if id(node) in endIds:  # 如果截止当前字符在字典树中，查找下一部分是否在字典树中
                    if i == len(word) - 1:
                        return True
                    if dfs(word, i + 1):
                        return True
            return False

        ans = []
        for word in words:
            if dfs(word, 0):
                ans.append(word)
            add(word)
        return ans


s = Solution()
print(s.findAllConcatenatedWordsInADict(["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]))
print(s.findAllConcatenatedWordsInADict(["cat", "dog", "catdog"]))
