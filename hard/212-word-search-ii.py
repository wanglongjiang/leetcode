'''
单词搜索 II
给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母在一个单词中不允许被重复使用。
'''
from typing import List
'''
思路，深度优先搜索。
与79题单词查找类似，将矩阵转为图进行搜索。
1、将矩阵转为邻接表形式的图，时间复杂度O(m*n)。为了后续查找速度，可以将每个字母映射到的单元格list保存到哈希表heads中。
2、对于每个单词的，从heads中获取起点list，以其为起点进行路径搜索，如果存在与word相同的路径，则成功加入结果list中。
时间复杂度：O(m*n*l*3^c)，其中m*n为矩阵大小，l为字符串列表长度，c为单词长度。最坏情况下为该复杂度，实际情况远远小于。
'''


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        row, col = len(board), len(board[0])
        g = [[] for i in range(row * col)]
        heads = {}
        # 将输入矩阵转为邻接表形式的图
        for i in range(row):
            for j in range(col):
                nodeId = i * col + j
                if board[i][j] not in heads:
                    heads[board[i][j]] = []
                heads[board[i][j]].append(nodeId)
                # 添加边
                if i > 0:
                    g[nodeId].append((i - 1) * col + j)
                if j > 0:
                    g[nodeId].append(i * col + j - 1)
                if i < row - 1:
                    g[nodeId].append((i + 1) * col + j)
                if j < col - 1:
                    g[nodeId].append(i * col + j + 1)

        # nodeid转为字母
        def nodeId2char(nodeId):
            r, c = divmod(nodeId, col)
            return board[r][c]

        marked = [False] * row * col  # 标记是否已遍历过

        # 深度优先查找路径
        def dfs(nodeId, word, wordIndex):
            if wordIndex == len(word) - 1:
                return True
            marked[nodeId] = True
            nextIndex = wordIndex + 1
            result = False
            for nextNode in g[nodeId]:
                # 下一节点未遍历过，且字符相同，进入下一个字符进行匹配
                if not marked[nextNode] and nodeId2char(nextNode) == word[nextIndex]:
                    if dfs(nextNode, word, nextIndex):
                        result = True
                        break
            marked[nodeId] = False
            return result

        ans = []
        for word in words:
            # 根据首字母所在的单元格进行查找路径
            if word[0] not in heads:
                continue
            for nodeId in heads[word[0]]:
                if dfs(nodeId, word, 0):
                    ans.append(word)
                    break
        return ans


s = Solution()
print(s.findWords(board=[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]], words=["oath", "pea", "eat", "rain"]))
