'''
1466. 重新规划路线
n 座城市，从 0 到 n-1 编号，其间共有 n-1 条路线。因此，要想在两座不同城市之间旅行只有唯一一条路线可供选择（路线网形成一颗树）。
去年，交通运输部决定重新规划路线，以改变交通拥堵的状况。

路线用 connections 表示，其中 connections[i] = [a, b] 表示从城市 a 到 b 的一条有向路线。

今年，城市 0 将会举办一场大型比赛，很多游客都想前往城市 0 。

请你帮助重新规划路线方向，使每个城市都可以访问城市 0 。返回需要变更方向的最小路线数。

题目数据 保证 每个城市在重新规划路线方向后都能到达城市 0 。

 

示例 1：



输入：n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
输出：3
解释：更改以红色显示的路线的方向，使每个城市都可以到达城市 0 。
示例 2：



输入：n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
输出：2
解释：更改以红色显示的路线的方向，使每个城市都可以到达城市 0 。
示例 3：

输入：n = 3, connections = [[1,0],[2,0]]
输出：0
 

提示：

2 <= n <= 5 * 10^4
connections.length == n-1
connections[i].length == 2
0 <= connections[i][0], connections[i][1] <= n-1
connections[i][0] != connections[i][1]
'''

from collections import deque
from typing import List
'''
思路：BFS
简单的BFS，详细思路见代码和注释

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        nextpath, prevpath = [[] for _ in range(n)], [[] for _ in range(n)]  # 两个邻接数组分别保存下个节点和上一个节点
        # 首先遍历一次输入，将其记录到正向和反向路径里面
        for conn in connections:
            nextpath[conn[0]].append(conn[1])
            prevpath[conn[1]].append(conn[0])
        # BFS 遍历
        q = deque()
        marked = [False] * n
        marked[0] = True
        ans = 0
        q.append(0)
        while q:
            i = q.popleft()
            for nexti in nextpath[i]:  # 添加正向路径
                if not marked[nexti]:
                    marked[nexti] = True
                    q.append(nexti)
                    ans += 1  # 正向路径需要修改方向
            for nexti in prevpath[i]:  # 添加反向路径
                if not marked[nexti]:
                    marked[nexti] = True
                    q.append(nexti)
        return ans
