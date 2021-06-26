'''
滑动谜题
在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示.

一次移动定义为选择 0 与一个相邻的数字（上下左右）进行交换.

最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。

给出一个谜板的初始状态，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。

示例：

输入：board = [[1,2,3],[4,0,5]]
输出：1
解释：交换 0 和 5 ，1 步完成
输入：board = [[1,2,3],[5,4,0]]
输出：-1
解释：没有办法完成谜板
输入：board = [[4,1,2],[5,0,3]]
输出：5
解释：
最少完成谜板的最少移动次数是 5 ，
一种移动路径:
尚未移动: [[4,1,2],[5,0,3]]
移动 1 次: [[4,1,2],[0,5,3]]
移动 2 次: [[0,1,2],[4,5,3]]
移动 3 次: [[1,0,2],[4,5,3]]
移动 4 次: [[1,2,0],[4,5,3]]
移动 5 次: [[1,2,3],[4,5,0]]
输入：board = [[3,2,4],[1,5,0]]
输出：14
提示：

board 是一个如上所述的 2 x 3 的数组.
board[i][j] 是一个 [0, 1, 2, 3, 4, 5] 的排列.
'''
from typing import List
from collections import defaultdict
'''
思路：BFS 位运算
每个board的布局是一个节点，2个布局之间如果可以变化，则2个布局之间有一条边。
每个布局是0-5这6个数的排列，每个数字可以用3bit表示，一个布局可以用18bit，一个整数来表示

时间复杂度：O(6!)
空间复杂度：O(6!)
'''


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        self.visited = defaultdict(bool)
        q, nextq = [], []
        ans = 0
        node = board[0][0] | (board[0][1] << 3) | (board[0][2] << 6) | (board[1][0] << 9) | (board[1][1] << 12) | (board[1][2] << 15)
        self.target = 1 | (2 << 3) | (3 << 6) | (4 << 9) | (5 << 12) | (0 << 15)
        if node == self.target:
            return 0
        self.visited[node] = True
        q.append(node)
        while q:
            node = q.pop()
            if self.addNextnodes(nextq, node):  # 将node的下一个布局加入q中，如果下一个布局中有target，返回
                return ans + 1
            if not q:
                q, nextq = nextq, q
                ans += 1
        return -1

    # 将node的下一个布局添加到队列q中，如果下一个布局中有target，返回true
    def addNextnodes(self, q, node):
        for i in range(6):
            if (7 << (i * 3)) & node == 0:
                for nextnode in self.getNextnodes(i, node):
                    if nextnode == self.target:
                        return True
                    if not self.visited[nextnode]:
                        q.append(nextnode)
                        self.visited[nextnode] = True
        return False

    # 取得node的下一个布局list
    def getNextnodes(self, i, node):
        nodes = []
        if i == 0:
            nodes.append(((node & (7 << 3)) >> 3) | (node & ~(7 << 3)))  # 0与坐标1交换
            nodes.append(((node & (7 << 9)) >> 9) | (node & ~(7 << 9)))  # 0与坐标3交换
        elif i == 1:
            nodes.append(((node & 7) << 3) | (node & ~7))  # 1与坐标0交换
            nodes.append(((node & (7 << 6)) >> 3) | (node & ~(7 << 6)))  # 1与坐标2交换
            nodes.append(((node & (7 << 12)) >> 9) | (node & ~(7 << 12)))  # 1与坐标4交换
        elif i == 2:
            nodes.append(((node & (7 << 3)) << 3) | (node & ~(7 << 3)))  # 2与坐标1交换
            nodes.append(((node & (7 << 15)) >> 9) | (node & ~(7 << 15)))  # 2与坐标5交换
        elif i == 3:
            nodes.append(((node & 7) << 9) | (node & ~7))  # 3与坐标0交换
            nodes.append(((node & (7 << 12)) >> 3) | (node & ~(7 << 12)))  # 3与坐标4交换
        elif i == 4:
            nodes.append(((node & (7 << 9)) << 3) | (node & ~(7 << 9)))  # 4与坐标3交换
            nodes.append(((node & (7 << 15)) >> 3) | (node & ~(7 << 15)))  # 4与坐标5交换
            nodes.append(((node & (7 << 3)) << 9) | (node & ~(7 << 3)))  # 4与坐标1交换
        else:
            nodes.append(((node & (7 << 6)) << 9) | (node & ~(7 << 6)))  # 5与坐标2交换
            nodes.append(((node & (7 << 12)) << 3) | (node & ~(7 << 12)))  # 5与坐标4交换
        return nodes


s = Solution()
print(s.slidingPuzzle([[4, 1, 2], [5, 0, 3]]))
print(s.slidingPuzzle([[1, 2, 3], [4, 0, 5]]))
print(s.slidingPuzzle([[1, 2, 3], [5, 4, 0]]))
print(s.slidingPuzzle([[3, 2, 4], [1, 5, 0]]))
