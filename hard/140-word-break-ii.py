'''
单词拆分 II
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，
使得句子中所有的单词都在词典中。返回所有这些可能的句子。

说明：

分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
'''
from typing import List
'''
思路：回溯+字典树查找。
与139题思路类似。
1、先把wordDict构造成字典树
2、从头开始匹配s，以贪婪模式尽可能长的匹配，把成功匹配的结果以list形式返回，下一次匹配的开头从list其中一个下标开始，
    如果匹配失败，回溯到上一个下标继续匹配。
3、重复过程2，直至s的所有字符都被匹配。
时间复杂度：O(m*n)，最坏情况下是O(m*n)，实际应该远远小于
空间复杂度：O(m+n)，回溯的栈最坏情况下深度为m，字典树空间为n
'''


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.trieCount, trieSize, charsetSize = 0, 1024, 26
        trie = [[0] * charsetSize for _ in range(trieSize)]
        finishIds = set()

        # 将wordDict构造字典树
        def insert(word):
            nodeId = 0
            for i in range(len(word)):
                c = ord(word[i]) - ord('a')
                if trie[nodeId][c]:
                    nodeId = trie[nodeId][c]
                else:
                    if self.trieCount > trieSize:
                        trie.extend([[0] * charsetSize for _ in range(trieSize)])
                        trieSize << 1
                    self.trieCount += 1
                    trie[nodeId][c] = self.trieCount
                    nodeId = self.trieCount
            finishIds.add(nodeId)

        for word in wordDict:
            insert(word)
        # 贪婪模式匹配所有的终结点
        end = len(s)

        def searchAll(start):
            nodeId = 0
            matchIndexs = []
            while start < end:
                c = ord(s[start]) - ord('a')
                if trie[nodeId][c]:
                    nodeId = trie[nodeId][c]
                    if nodeId in finishIds:
                        matchIndexs.append(start + 1)
                    start += 1
                else:
                    break
            return matchIndexs

        # 回溯所有匹配点，能匹配s的所有字符
        ans = []
        comb = []

        def backtrack(index):
            indexs = searchAll(index)
            for i in range(len(indexs) - 1, -1, -1):
                comb.append(s[index:indexs[i]])
                if indexs[i] == end:  # 能匹配至终点
                    ans.append(' '.join(comb))
                backtrack(indexs[i])
                comb.pop()
            return False

        backtrack(0)
        return ans


s = Solution()
print(s.wordBreak(s="catsanddog", wordDict=["cat", "cats", "and", "sand", "dog"]))
print(s.wordBreak(s="pineapplepenapple", wordDict=["apple", "pen", "applepen", "pine", "pineapple"]))
print(s.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
