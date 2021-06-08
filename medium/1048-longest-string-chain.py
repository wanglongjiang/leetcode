'''
最长字符串链

给出一个单词列表，其中每个单词都由小写英文字母组成。

如果我们可以在 word1 的任何地方添加一个字母使其变成 word2，那么我们认为 word1 是 word2 的前身。例如，"abc" 是 "abac" 的前身。

词链是单词 [word_1, word_2, ..., word_k] 组成的序列，k >= 1，其中 word_1 是 word_2 的前身，word_2 是 word_3 的前身，依此类推。

从给定单词列表 words 中选择单词组成词链，返回词链的最长可能长度。
 

示例：

输入：["a","b","ba","bca","bda","bdca"]
输出：4
解释：最长单词链之一为 "a","ba","bda","bdca"。
 

提示：

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] 仅由小写英文字母组成。
'''
from typing import List
from collections import defaultdict
'''
思路：图的深度优先遍历
1. 将words按照长度进行分组
2. 遍历长度相差1的2组之间是否有前身关系，如果有，从前身到单词之间有条路径，将该路径加入有向图中
3. 遍历图，找到最长的路径

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)

        lenGroup = defaultdict(list)
        minlen, maxlen = 20, 0
        for i in range(n):
            lenGroup[len(words[i])].append(i)  # 将words按照长度进行分组
            minlen = min(minlen, len(words[i]))
            maxlen = max(maxlen, len(words[i]))
        # 遍历长度相差1的2组之间是否有前身关系，如果有，加入有向图中
        g = [[] for _ in range(n)]  # 有向图为邻接表
        for length in range(minlen, maxlen):
            sgroup = lenGroup[length]
            lgroup = lenGroup[length + 1]
            for shortIdx in sgroup:
                for longIdx in lgroup:
                    sstr, lstr = words[shortIdx], words[longIdx]
                    i, j = 0, 0
                    while i < len(sstr) and j < len(lstr):  # 依次对比每个字符
                        if sstr[i] != lstr[j]:  # 如果遇到不同的字符，长字符串尝试跳过
                            j += 1
                            if j - i > 1:  # 如果不同字符超过1个，肯定不是前身关系
                                break
                        else:
                            j += 1
                            i += 1
                    if (i == len(sstr) and j == len(lstr)) or (i == j):  # 两个字符串全部对比完，说明是前身关系
                        g[shortIdx].append(longIdx)
        # 遍历有向图，找到最长的路径
        maxLens = [0] * n

        def dfs(node):
            if maxLens[node]:
                return maxLens[node]
            maxSublen = 0
            for nextnode in g[node]:
                maxSublen = max(maxSublen, dfs(nextnode))
            maxLens[node] = maxSublen + 1
            return maxLens[node]

        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i))
        return ans


s = Solution()
print(s.longestStrChain(["abcd", "dbqca"]))
print(s.longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]))
