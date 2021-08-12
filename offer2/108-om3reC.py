'''
剑指 Offer II 108. 单词演变
在字典（单词列表） wordList 中，从单词 beginWord 和 endWord 的 转换序列 是一个按下述规格形成的序列：

序列中第一个单词是 beginWord 。
序列中最后一个单词是 endWord 。
每次转换只能改变一个字母。
转换过程中的中间单词必须是字典 wordList 中的单词。
给定两个长度相同但内容不同的单词 beginWord 和 endWord 和一个字典 wordList ，找到从 beginWord 到 endWord 的 最短转换序列 中的 单词数目 。如果不存在这样的转换序列，返回 0。

 

示例 1：

输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
输出：5
解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。
示例 2：

输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
输出：0
解释：endWord "cog" 不在字典中，所以无法进行转换。
 

提示：

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord、endWord 和 wordList[i] 由小写英文字母组成
beginWord != endWord
wordList 中的所有字符串 互不相同
 

注意：本题与主站 127 题相同： https://leetcode-cn.com/problems/word-ladder/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/om3reC
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from typing import List


class Graph:
    def __init__(self):
        self.nodes = {}

    def addNode(self, s: str):
        self.nodes[s] = Node(s)

    def addEdge(self, s1: str, s2: str):
        self.nodes[s1].edges.append(self.nodes[s2])
        self.nodes[s2].edges.append(self.nodes[s1])

    def isNode(self, s: str):
        return s in self.nodes

    # 求最短路径长度
    def shortestPathLen(self, start: str, end: str):
        q, nextq = [], []
        startNode, endNode = self.nodes[start], self.nodes[end]
        q.append(startNode)
        startNode.marked = True
        pathLen = 1
        while q:
            node = q.pop(0)
            if node == endNode:
                return pathLen
            for nextnode in node.edges:
                if not nextnode.marked:
                    nextnode.marked = True
                    nextq.append(nextnode)
            if not q:
                pathLen += 1
                nextq, q = q, nextq
        return 0


class Node:
    def __init__(self, s: str):
        self.s = s
        self.edges = []
        self.marked = False


'''
思路：图的最短路径
    将每个word视为节点，2个只有1个字母不同的word之间视为有边，这道题就是求最短路径的长度。
    1、首先需要将输入的beginWord、wordList转化为无权无向图。
        要确认任意两个单词是否可以转换，可以将长度为m的单词每次去掉同列字符，形成m个新单词subword，具备相同subword的2个单词可以转化
    2、搜索从节点beginWord到endWord的最短路径。采用广度优先搜索算法。
    时间复杂度：O(m*m*n)，转化为无权无向图，需要将每个word切分成m个subword，需要O(m*m*n)的时间，然后搜索最短路径搜索需要O(n)
    空间复杂度：O(m*m*n)，转化过程中需要m*m*n的辅助数组保存subword，无向图需要空间n
'''


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        import datetime
        starttime = datetime.datetime.now()

        graph = Graph()
        m = len(beginWord)
        # 1、转为无向图
        subwords = [{} for i in range(m)]  # 用这个数组保存去掉不同位置后形成的subword

        def cutWord(word: str):
            for i in range(m):
                subwordMap = subwords[i]
                subword = word[:i] + word[i + 1:]
                if subword not in subwordMap:
                    subwordMap[subword] = []
                else:
                    for other in subwordMap[subword]:  # 具有相同子串的word之间有边
                        graph.addEdge(word, other)
                subwordMap[subword].append(word)

        graph.addNode(beginWord)
        cutWord(beginWord)
        for word in wordList:
            graph.addNode(word)
            cutWord(word)
        # 判断endWord是否在字典中
        if not graph.isNode(endWord):
            return 0
        # 广度优先搜索最短路径长度
        ans = graph.shortestPathLen(beginWord, endWord)
        endtime = datetime.datetime.now()
        print((endtime - starttime).microseconds)
        return ans
