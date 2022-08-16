'''
792. 匹配子序列的单词数
给定字符串 S 和单词字典 words, 求 words[i] 中是 S 的子序列的单词个数。

示例:
输入:
S = "abcde"
words = ["a", "bb", "acd", "ace"]
输出: 3
解释: 有三个是 S 的子序列的单词: "a", "acd", "ace"。
注意:

所有在words和 S 里的单词都只由小写字母组成。
S 的长度在 [1, 50000]。
words 的长度在 [1, 5000]。
words[i]的长度在[1, 50]。
'''
from typing import List
from collections import defaultdict
import bisect
'''
思路：字典树 DFS 二分查找
首先将words中所有单词加入字典树。
然后dfs遍历字典树的每个节点，查找s的子序列是否能与字典树中节点匹配。

时间复杂度不好估啊，跑跑看吧
'''


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        root = {}  # 字典树根节点
        endNode = set()

        # 所有的单词加入字典树
        def insert(word):
            node = root
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            endNode.add(id(node))

        for word in words:
            insert(word)
        # 将每个字符的索引加入list，便于后面二分查找
        idxMap = defaultdict(list)
        for i, char in enumerate(s):
            idxMap[char].append(i)

        # 搜索s的子序列是否在字典树中
        def dfs(startIdx, node):
            ans = 0
            for char in node.keys():
                idxs = idxMap[char]
                idx = bisect.bisect_left(idxs, startIdx)  # 在索引中找下一个字符的>=startIdx的最小索引
                if idx < len(idxs):  # 能在s中找到下一个匹配的字符
                    if id(node[char]) in endNode:  # 下一个节点是终点，匹配数+1
                        ans += 1
                    ans += dfs(idxs[idx] + 1, node[char])  # 需要从索引的下一个位置查找下一个字符
            return ans

        return dfs(0, root)


s = Solution()
print(s.numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]))
print(s.numMatchingSubseq("qlhxagxdqh", ["qlhxagxdq", "qlhxagxdq", "lhyiftwtut", "yfzwraahab"]) == 2)  # TODO
