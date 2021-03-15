'''
被围绕的区域
给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。
任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

'''
from typing import List
'''
思路，图的路径搜索。
把'O'认为图中的顶点，从边界处的'O'出发，能到达的'O'不可以替换，其他不可到达的'O'可以替换为'X'。
时间复杂度：O(mn)，建立图，图的遍历都需要O(mn)
空间复杂度：O(mn)，最坏情况下需要O(mn)空间建图
'''


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row, col = len(board), len(board[0])
        g = {}  # 图用哈希表和邻接表来表示。哈希表的key为节点id，value为边的list
        boundary = set()  # 边界顶点集合

        # 根据index取得顶点id
        def toId(i, j):
            return i * col + j

        # 根据顶点id，转换成坐标
        def toIndex(nodeid):
            return divmod(nodeid, col)

        # 建立图
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    nodeid = toId(i, j)
                    g[nodeid] = []
                    # 判断是否边界
                    if i == 0 or j == 0 or i == (row - 1) or j == (col - 1):
                        boundary.add(nodeid)
                    # 判断是否有到其他的'O'的路径，并添加到顶点的边
                    if i > 0 and board[i - 1][j] == 'O':
                        g[nodeid].append(toId(i - 1, j))
                    if i < (row - 1) and board[i + 1][j] == 'O':
                        g[nodeid].append(toId(i + 1, j))
                    if j > 0 and board[i][j - 1] == 'O':
                        g[nodeid].append(toId(i, j - 1))
                    if j < (col - 1) and board[i][j + 1] == 'O':
                        g[nodeid].append(toId(i, j + 1))
        # 从边界节点出发，遍历所有能到达的路径，并添加到不可覆盖顶点集合中
        noover = set()

        def dfs(id):
            noover.add(id)
            for nextId in g[id]:
                if nextId not in noover:
                    dfs(nextId)

        for nodeid in boundary:
            dfs(nodeid)
        # 对于可以覆盖的'O'进行覆盖
        for id in g:
            if id not in noover:
                i, j = toIndex(id)
                board[i][j] = 'X'


s = Solution()
b = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
print(b)
s.solve(b)
print(b)
b = [["X"]]
s.solve(b)
print(b)
