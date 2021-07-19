'''
剑指 Offer 12. 矩阵中的路径

给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 

例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。



 

示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
 

提示：

1 <= board.length <= 200
1 <= board[i].length <= 200
board 和 word 仅由大小写英文字母组成
 

注意：本题与主站 79 题相同：https://leetcode-cn.com/problems/word-search/
'''
from typing import List
'''
思路1：遍历矩阵每个位置，然后回溯搜索
时间复杂度：遍历矩阵m*n，回溯搜索3^k，总计m*n*3^k，超时了

思路2：将矩阵转为图进行搜索。
1、将矩阵转为邻接表形式的图，时间复杂度O(m*n)，同时将所有与首字母相同的顶点记录到headNodes中
2、遍历headNodes，以其为起点进行路径搜索，如果存在与word相同的路径，则成功返回true

时间复杂度：O(mnl)m,n为矩阵大小，l为word.length
空间复杂度：O(mn)
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
