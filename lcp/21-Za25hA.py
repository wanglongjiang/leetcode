'''
LCP 21. 追逐游戏
秋游中的小力和小扣设计了一个追逐游戏。他们选了秋日市集景区中的 N 个景点，景点编号为 1~N。
此外，他们还选择了 N 条小路，满足任意两个景点之间都可以通过小路互相到达，且不存在两条连接景点相同的小路。
整个游戏场景可视作一个无向连通图，记作二维数组 edges，数组中以 [a,b] 形式表示景点 a 与景点 b 之间有一条小路连通。

小力和小扣只能沿景点间的小路移动。小力的目标是在最快时间内追到小扣，小扣的目标是尽可能延后被小力追到的时间。
游戏开始前，两人分别站在两个不同的景点 startA 和 startB。每一回合，小力先行动，小扣观察到小力的行动后再行动。
小力和小扣在每回合可选择以下行动之一：

移动至相邻景点
留在原地
如果小力追到小扣（即两人于某一时刻出现在同一位置），则游戏结束。
若小力可以追到小扣，请返回最少需要多少回合；若小力无法追到小扣，请返回 -1。

注意：小力和小扣一定会采取最优移动策略。
edges 的长度等于图中节点个数
3 <= edges.length <= 10^5
1 <= edges[i][0], edges[i][1] <= edges.length 且 edges[i][0] != edges[i][1]
1 <= startA, startB <= edges.length 且 startA != startB
'''
from typing import List
'''
思路：无向图的路径搜索。
如果图中没有回路，一定能够追上，小扣会选择远离小力的最远路径。
如果图中有回路，如果小扣在回路中，小力追不上；如果小扣能够在小力之前进入回路，也追不上；如果不能在小力之前进入回路，会选择远离小力的最远路径。
算法：
1、从startA出发，BFS遍历到达其他顶点的所有最短路径（记录到数组d里面），并将环路中的顶点记录到集合c中。
2、如果没有环路，从startA出发经过startB的最长路径长度即为计算结果
    如果有环路，分3种清空：
        a、startB在环路中，肯定追不上
        b、startB不在环路中，BFS计算statrB出发去往环路中所有节点的最短距离，找到距离最短的节点k。
        如果追击者距离k更远，追不上
        如果追击者距离k更近，可以追上，逃跑者需要向远离的方向移动，最终追上的距离为从startA出发经过startB的最长路径长度。
时间复杂度：O(n)，有n个节点和n条边，需要遍历所有节点和边
空间复杂度：O(n)
'''


class Solution:
    def chaseGame(self, edges: List[List[int]], startA: int, startB: int) -> int:
        # 采用邻接表表示图，因为节点数最高是10^5，采用矩阵浪费空间比较多。
        n = len(edges)
        g = [[] for _ in range(n + 1)]
        for edge in edges:
            g[edge[0]].append(edge[1])
            g[edge[1]].append(edge[0])
        # 检测startA和startB是否相邻
        for node in g[startA]:
            if node == startB:
                return 1
        # 搜索从startA出发的所有最短路径，使用bfs算法
        d = [0] * (n + 1)  # d数组记录从startA出发的最短路径
        ringNodes = set()  # 环路中的节点

        def bfs():
            queue, qi = [startA, 0], 0  # 删除list头部性能较差，直接改变队列索引qi
            distance = 0
            white, gray, black = 0, 1, 2
            marked = [white] * (n + 1)
            while qi < len(queue):
                node = queue[qi]
                qi += 1
                if not node:  # 遇到哨兵节点，距离+1
                    if queue[-1] == 0:
                        return
                    distance += 1
                    queue.append(0)
                    continue
                d[node] = distance  # 修改最短距离

                marked[node] = black
                for next in g[node]:  # 遍历所有的边
                    if marked[next] == white:
                        marked[next] = gray
                        queue.append(next)
                    elif marked[next] == gray:  # 有环
                        ringNodes.add(next)

        bfs()
        # 如果有环，从已知的环中的顶点出发，找出图中所有的环（使用DFS算法）
        allRingNodes = set()
        if len(ringNodes) > 0:
            marked = [False] * (n + 1)
            path = []

            def dfs(node):
                marked[node] = True
                path.append(node)
                for next in g[node]:
                    if marked[next]:  # 如果遍历过，判断是否为环路
                        if len(path) > 1 and path[0] == next:  # 如果是环路，将环路中的所有节点加入ringNodes
                            allRingNodes.update(path)
                            if startB in allRingNodes:  # 如果startB在环路中，直接退出
                                return False
                    else:
                        if not dfs(next):  # 如果startB在环路中，直接退出
                            return False
                path.pop()
                return True

            for node in ringNodes:  # 从已知的环中的顶点出发，找出所有环的顶点
                if not dfs(node):  # 如果startB在环中，直接退出
                    return -1

        # 从startB出发如果找到环中的顶点k，如果路径小于startA到k的距离说明可以逃跑
        d2 = [0] * (n + 1)

        def canRunAway():
            marked = [False] * (n + 1)
            q, i = [startB, 0], 0
            distance = 0
            while i < len(q):
                node = q[i]
                i += 1
                if not node:
                    if q[-1] == 0:
                        return False
                    distance += 1
                    q.append(0)
                    continue
                marked[node] = True
                d2[node] = distance
                for next in g[node]:
                    if not marked[next]:
                        if next in allRingNodes:
                            allRingNodes.remove(next)  # 一个顶点判断一次就可以
                            ringDistance = distance + 1
                            if d[next] > ringDistance:  # startA到该点的距离大于startB到该点的距离，说明可以逃跑
                                return True
                        q.append(next)
            return False

        if canRunAway():
            return -1
        # 如果没有环，或者有环但逃不掉，需要查找从startA出发，经过startB的最远路径。如果有不经过b的路径说明有环路，这是不可能的。
        ans = 0
        for i in range(1, n + 1):
            if d[i] > d2[i] and d[i] == d2[i] + d[startB]:
                ans = max(ans, d[i])
        return ans


s = Solution()
print(s.chaseGame(edges=[[1, 2], [2, 3], [3, 4], [4, 1], [2, 5], [5, 6]], startA=3, startB=5))
print(s.chaseGame(edges=[[1, 2], [2, 3], [3, 4], [4, 1]], startA=1, startB=3))
