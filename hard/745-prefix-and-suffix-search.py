'''
前缀和后缀搜索
给定多个 words，words[i] 的权重为 i 。

设计一个类 WordFilter 实现函数WordFilter.f(String prefix, String suffix)。
这个函数将返回具有前缀 prefix 和后缀suffix 的词的最大权重。如果没有这样的词，返回 -1。

例子:

输入:
WordFilter(["apple"])
WordFilter.f("a", "e") // 返回 0
WordFilter.f("b", "") // 返回 -1
注意:

words的长度在[1, 15000]之间。
对于每个测试用例，最多会有words.length次对WordFilter.f的调用。
words[i]的长度在[1, 10]之间。
prefix, suffix的长度在[0, 10]之前。
words[i]和prefix, suffix只包含小写字母。
'''
from typing import List
from collections import defaultdict
'''
思路：字典树
> 初始化函数：遍历所有word，将word的所有后缀+'#'+前缀加入字典树，同时，将该字符串经过的节点的权重全部更新
> 查找函数：将后缀+'#'+前缀拼成字符串，在字典树中查找具备这个前缀的字符串权重

时间复杂度：O(n*m*m)，n为words.length，m为word的平均长度
空间复杂度：O(n*m*m)
'''


class WordFilter:
    def __init__(self, words: List[str]):
        self.trie = {}  # 字典树
        self.prefixCount = defaultdict(int)  # 各个前缀的个数
        for k in range(len(words)):
            word = words[k]
            for i in range(len(word)):
                s = word[i:] + '#' + word  # 组成所有后缀与单词的组合
                node = self.trie
                self.prefixCount[id(node)] = k  # 空字符串是所有字符串的前缀，没新增一个字符串，将其权重更新
                for j in range(len(s)):
                    if s[j] not in node:
                        node[s[j]] = {}
                    node = node[s[j]]
                    self.prefixCount[id(node)] = k  # 以其为前缀的字符串权重更新

    def f(self, prefix: str, suffix: str) -> int:
        s = suffix + '#' + prefix
        node = self.trie
        for i in range(len(s)):
            if s[i] not in node:
                return -1
            node = node[s[i]]
        return self.prefixCount[id(node)]


w = WordFilter(["apple"])
print(w.f("a", "e"))
print(w.f("b", ""))
