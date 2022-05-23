'''
675. 为高尔夫比赛砍树
你被请来给一个要举办高尔夫比赛的树林砍树。树林由一个 m x n 的矩阵表示， 在这个矩阵中：

0 表示障碍，无法触碰
1 表示地面，可以行走
比 1 大的数 表示有树的单元格，可以行走，数值表示树的高度
每一步，你都可以向上、下、左、右四个方向之一移动一个单位，如果你站的地方有一棵树，那么你可以决定是否要砍倒它。

你需要按照树的高度从低向高砍掉所有的树，每砍过一颗树，该单元格的值变为 1（即变为地面）。

你将从 (0, 0) 点开始工作，返回你砍完所有树需要走的最小步数。 如果你无法砍完所有的树，返回 -1 。

可以保证的是，没有两棵树的高度是相同的，并且你至少需要砍倒一棵树。

 

示例 1：


输入：forest = [[1,2,3],[0,0,4],[7,6,5]]
输出：6
解释：沿着上面的路径，你可以用 6 步，按从最矮到最高的顺序砍掉这些树。
示例 2：


输入：forest = [[1,2,3],[0,0,0],[7,6,5]]
输出：-1
解释：由于中间一行被障碍阻塞，无法访问最下面一行中的树。
示例 3：

输入：forest = [[2,3,4],[0,0,5],[8,7,6]]
输出：6
解释：可以按与示例 1 相同的路径来砍掉所有的树。
(0,0) 位置的树，可以直接砍去，不用算步数。
 

提示：

m == forest.length
n == forest[i].length
1 <= m, n <= 50
0 <= forest[i][j] <= 109
'''

from heapq import heappop, heappush
from typing import List
'''
思路：DFS+优先队列+BFS
1、从0,0开始，用DFS遍历矩阵，将可以砍倒的树加入优先队列（按照树的高度排序）；
2、如果不是所有的树都能砍倒，返回-1
3、将最矮的树从堆中pop出来，然后从当前位置移动到该树的位置（使用BFS寻找最短路径）
4、重复过程3，直至堆为空。

时间复杂度：O(mn*mn)：双重BFS，需要矩阵单元格的二次方
空间复杂度：O(mn)
'''


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])

        def getShortestPath(src, target):  # 用BFS计算2个点之间的最短路径
            if src == target:
                return 0
            ans = 0
            mk = set()
            q1, q2 = [src], []
            while q1:
                p = q1.pop()
                for x, y in [(p[0] + 1, p[1]), (p[0] - 1, p[1]), (p[0], p[1] + 1), (p[0], p[1] - 1)]:
                    if (x, y) == target:
                        return ans + 1
                    if 0 <= x < m and 0 <= y < n and (x, y) not in mk and forest[x][y] >= 1:  # 下个单元格是地面或树才能行走
                        mk.add((x, y))
                        q2.append((x, y))
                if not q1:
                    q1, q2 = q2, q1
                    ans += 1

        # 从0,0开始用dfs遍历所有能到达的树，加入优先队列
        marked = set([(0, 0)])
        heap = [(forest[0][0], (0, 0))]  # 优先队列，保存可以砍倒的树的坐标

        def dfs(p):
            if forest[p[0]][p[1]] > 1:
                heappush(heap, (forest[p[0]][p[1]], (p[0], p[1])))
            for x, y in [(p[0] + 1, p[1]), (p[0] - 1, p[1]), (p[0], p[1] + 1), (p[0], p[1] - 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in marked and forest[x][y] >= 1:  # 下个单元格是树才可以通过
                    marked.add((x, y))
                    dfs((x, y))

        dfs((0, 0))

        # 检查是否还有到达的树
        for x in range(m):
            for y in range(n):
                if forest[x][y] > 1 and (x, y) not in marked:
                    return -1

        # 下面开始遍历所有能砍倒的树
        curPoint = (0, 0)  # 当前坐标
        step = 0  # 步数

        while heap:  # 遍历所有可以砍倒的树
            height, p = heappop(heap)
            step += getShortestPath(curPoint, p)  # 移动到要砍倒的树的单元格
            curPoint = p
        return step


s = Solution()
print(s.cutOffTree([[4, 2, 3], [0, 0, 1], [7, 6, 5]]))
print(
    s.cutOffTree([[54581641, 64080174, 24346381, 69107959], [86374198, 61363882, 68783324, 79706116], [668150, 92178815, 89819108, 94701471],
                  [83920491, 22724204, 46281641, 47531096], [89078499, 18904913, 25462145, 60813308]]))
print(s.cutOffTree([[1, 2, 3], [0, 0, 4], [7, 6, 5]]))
print(s.cutOffTree([[1, 2, 3], [0, 0, 0], [7, 6, 5]]))
print(s.cutOffTree([[2, 3, 4], [0, 0, 5], [8, 7, 6]]))
