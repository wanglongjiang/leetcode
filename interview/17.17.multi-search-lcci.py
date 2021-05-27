'''
面试题 17.17. 多次搜索
给定一个较长字符串big和一个包含较短字符串的数组smalls，设计一个方法，根据smalls中的每一个较短字符串，
对big进行搜索。输出smalls中的字符串在big里出现的所有位置positions，其中positions[i]为smalls[i]出现的所有位置。

示例：

输入：
big = "mississippi"
smalls = ["is","ppi","hi","sis","i","ssippi"]
输出： [[1,4],[8],[],[3],[1,4,7,10],[5]]
提示：

0 <= len(big) <= 1000
0 <= len(smalls[i]) <= 1000
smalls的总字符数不会超过 100000。
你可以认为smalls中没有重复字符串。
所有出现的字符均为英文小写字母。
'''
from typing import List
'''
思路：字典树
将smalls加入字典树，然后对于big的每个位置，查询在字典树中出现的单词，将其加入结果

时间复杂度：O(nm)，n为big长度，m为small中平均长度
空间复杂度：O(26ml)，m为small中单词平均长度，l为small.length
'''


class Solution:
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        trieCount, trieSize, charsetSize = 0, len(smalls) * 1000, 26
        trie = [[0] * charsetSize for _ in range(trieSize)]
        finishIds = {}
        base = ord('a')

        # 添加单词到字典树
        def add(word, index):
            nonlocal trieCount
            nodeId = 0
            for i in range(len(word)):
                c = ord(word[i]) - base
                if trie[nodeId][c]:
                    nodeId = trie[nodeId][c]
                else:
                    trieCount += 1
                    trie[nodeId][c] = trieCount
                    nodeId = trieCount
            finishIds[nodeId] = index

        for i in range(len(smalls)):
            add(smalls[i], i)
        # 查找big每个位置是否有出现在字典树中的单词
        n = len(big)
        ans = [[] for _ in range(len(smalls))]

        def search(start):
            index = start
            nodeId = 0
            while index < n:
                c = ord(big[index]) - base
                if trie[nodeId][c]:
                    nodeId = trie[nodeId][c]
                    if nodeId in finishIds:  # 如果截止该字符是个出现在small中的单词，加入结果
                        ans[finishIds[nodeId]].append(start)
                    index += 1
                else:
                    return

        for start in range(n):
            search(start)
        return ans


s = Solution()
print(s.multiSearch(big="mississippi", smalls=["is", "ppi", "hi", "sis", "i", "ssippi"]))
