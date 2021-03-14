'''
单词搜索
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母不允许被重复使用。
'''
from typing import List
'''
思路1：遍历矩阵每个位置，然后回溯搜索
时间复杂度：遍历矩阵m*n，回溯搜索3^k，总计m*n*3^k，超时了

思路2：将矩阵转为图进行搜索。
1、将矩阵转为邻接表形式的图，时间复杂度O(m*n)，同时将所有与首字母相同的顶点记录到headNodes中
2、遍历headNodes，以其为起点进行路径搜索，如果存在与word相同的路径，则成功返回true

'''


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        g = [[] for i in range(row * col)]
        headNodes, headChar = [], word[0]
        # 将输入矩阵转为邻接表形式的图
        for i in range(row):
            for j in range(col):
                nodeId = i * col + j
                if board[i][j] == headChar:
                    headNodes.append(nodeId)
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

        lastIndex = len(word) - 1
        marked = [False] * row * col  # 标记是否已遍历过

        # 深度优先查找路径
        def dfs(nodeId, wordIndex):
            if wordIndex == lastIndex:
                return True
            marked[nodeId] = True
            nextIndex = wordIndex + 1
            for nextNode in g[nodeId]:
                # 下一节点未遍历过，且字符相同，进入下一个字符进行匹配
                if not marked[nextNode] and nodeId2char(nextNode) == word[nextIndex]:
                    if dfs(nextNode, nextIndex):
                        return True
            marked[nodeId] = False
            return False

        # 根据首字母所在的单元格进行查找路径
        for nodeId in headNodes:
            if dfs(nodeId, 0):
                return True
        return False


s = Solution()
print(s.exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], "ABCCED"))
print(s.exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], "SEE"))
print(s.exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], "ABCB"))
