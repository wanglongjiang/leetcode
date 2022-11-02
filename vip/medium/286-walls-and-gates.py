'''
286. 墙与门
你被给定一个 m × n 的二维网格 rooms ，网格中有以下三种可能的初始化值：

-1 表示墙或是障碍物
0 表示一扇门
INF 无限表示一个空的房间。然后，我们用 23^1 - 1 = 2147483647 代表 INF。你可以认为通往门的距离总是小于 2147483647 的。
你要给每个空房间位上填上该房间到 最近门的距离 ，如果无法到达门，则填 INF 即可。



示例 1：


输入：rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],
[0,-1,2147483647,2147483647]]
输出：[[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
示例 2：

输入：rooms = [[-1]]
输出：[[-1]]
示例 3：

输入：rooms = [[2147483647]]
输出：[[2147483647]]
示例 4：

输入：rooms = [[0]]
输出：[[0]]


提示：

m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] 是 -1、0 或 23^1 - 1
'''
from collections import deque
from typing import List
'''
思路：BFS
使用BFS，从所有的门出发，遍历周边所有的空房间

时间复杂度：O(mn)
空间复杂度：O(mn)
'''


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        m, n = len(rooms), len(rooms[0])
        queue = deque()
        dis = 1  # 距离
        inf = 2147483647
        queue.extend((i, j) for i in range(m) for j in range(n) if rooms[i][j] == 0)  # 所有的门加入队列
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                for nexti, nextj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= nexti < m and 0 <= nextj < n and rooms[nexti][nextj] == inf:
                        rooms[nexti][nextj] = dis
                        queue.append((nexti, nextj))
            dis += 1
