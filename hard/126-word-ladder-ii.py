'''
单词接龙 II
给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：

每次转换只能改变一个字母。
转换后得到的单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回一个空列表。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
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

    # 求所有最短路径
    def shortestPaths(self, start: str, end: str):
        q = []
        startNode, endNode = self.nodes[start], self.nodes[end]
        q.append(startNode)
        q.append(None)  # 放置1个哨兵，标志着1层节点的结束
        pathTree = {}
        paths = []
        while q:
            node = q.pop(0)
            if node is None:
                if paths:  # 已经找到所有的最短路径，不再处理剩下的路径
                    break
                if q:
                    q.append(None)  # 一层所有节点已经遍历完，再放置下一层的哨兵
                continue
            if node == endNode:
                prekey = node.s
                path = []
                while prekey in pathTree:
                    path.append(prekey)
                    prekey = pathTree[prekey]
                path.append(prekey)
                path.reverse()
                paths.append(path)
            node.traversed = True
            if not paths:  # 已找到最短路径，不再处理更远的路径
                nextNodes = list(filter(lambda node: not node.traversed, node.edges))
                for nextNode in nextNodes:  # 记录经过的路径
                    pathTree[nextNode.s] = node.s
                q.extend(nextNodes)
        return paths


class Node:
    def __init__(self, s: str):
        self.s = s
        self.edges = []
        self.traversed = False


class PathNode:
    def __init__(self, s: str):
        self.s = s


'''
思路：图的最短路径
    将每个word视为节点，2个只有1个字母不同的word之间视为有边，这道题就是求最短路径。
    1、首先需要将输入的beginWord、wordList转化为无权无向图。
        要确认任意两个单词是否可以转换，可以将长度为m的单词每次去掉同列字符，形成m个新单词subword，具备相同subword的2个单词可以转化
    2、搜索从节点beginWord到endWord的最短路径。采用广度优先搜索算法。
    时间复杂度：O(m*m*n)，转化为无权无向图，需要将每个word切分成m个subword，需要O(m*m*n)的时间，然后搜索最短路径搜索需要O(n)
    空间复杂度：O(m*m*n)，转化过程中需要m*m*n的辅助数组保存subword，无向图需要空间n
'''


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
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
            return []
        # 广度优先搜索最短路径
        return graph.shortestPaths(beginWord, endWord)


s = Solution()
print(s.findLadders(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
print(s.findLadders(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log"]))
