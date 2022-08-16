'''
面试题 17.22. 单词转换
给定字典中的两个词，长度相等。写一个方法，把一个词转换成另一个词， 但是一次只能改变一个字符。每一步得到的新词都必须能在字典中找到。

编写一个程序，返回一个可能的转换序列。如有多个可能的转换序列，你可以返回任何一个。

示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出:
["hit","hot","dot","lot","log","cog"]
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: []

解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-transformer-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
from collections import defaultdict
'''
思路：图 DFS
将每个单词视为图中的节点，任意2个单词，如果只替换1个字符就能转换，则这2个单词之间有一条边。
1. 构造图。遍历所有的单词，每个单词替换每个位置的字符为'-'后，加入哈希表，哈希表中与其相同的单词与当前单词有一条边。
2. 用DFS查找从beginword开始，endWord结束的路径

时间复杂度：O(mn)
空间复杂度：O(mn)
'''


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        wordList.append(beginWord)
        n, m = len(wordList), len(beginWord)
        # 将可以转换的单词表示为图
        g = [[] for _ in range(n)]
        hashmap = defaultdict(list)
        end = -1
        for i, word in enumerate(wordList):
            if word == endWord:
                end = i
            for j in range(m):
                key = word[:j] + '-' + word[j + 1:]
                for otherWordIdx in hashmap[key]:
                    g[otherWordIdx].append(i)
                g[i].extend(hashmap[key])
                hashmap[key].append(i)
        if end < 0:
            return []
        # dfs遍历可能的路径
        marked = [False] * n
        marked[n - 1] = True

        def dfs(node, path):
            path.append(wordList[node])
            if node == end:
                return path
            for other in g[node]:
                if not marked[other]:
                    marked[other] = True
                    p = dfs(other, path)
                    if p:
                        return p
            path.pop()
            return None

        path = dfs(n - 1, [])
        return path if path else []


s = Solution()
print(s.findLadders('a', 'c', ['a', 'b', 'c']))  # TODO ["a","b","c"]
print(s.findLadders(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
print(s.findLadders(beginWord="hit", endWord="cig", wordList=["hot", "dot", "dog", "lot", "cig"]))
