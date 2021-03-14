'''
课程表
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，
表示如果要学习课程 ai 则 必须 先学习课程  bi 。

例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
'''
from typing import List
'''
思路，检查有向图中是否有回路
每个课程看成图中的顶点，对于课程对[ai,bi]，表示有从b到a的边
算法需要从每个顶点出发，检查所有的路径是否有回路。
时间复杂度：O(n+m)，n为顶点数，m为课程对
空间复杂度：O(n+m)，n为顶点数，m为课程对
'''


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 图用邻接表表示
        g = [[] for i in range(numCourses)]
        for edge in prerequisites:
            g[edge[1]].append(edge[0])
        # 标记是否已遍历过
        marked = [False] * numCourses
        # 当前路径经过哪些顶点
        path = set()

        # 深度优先遍历node开始的路径
        def dfs(node):
            path.add(node)
            marked[node] = True
            for nextNode in g[node]:
                if nextNode in path:  # 如果顶点在路径中出现过，说明有环路，课程无法完成
                    return False
                if not marked[nextNode]:  # 下一个节点已经遍历过，说明该顶点出发的路径没有环路，可以跳过
                    if not dfs(nextNode):
                        return False
            path.remove(node)
            return True

        # 遍历所有顶点
        for node in range(numCourses):
            if not dfs(node):
                return False
        return True


s = Solution()
print(s.canFinish(numCourses=2, prerequisites=[[1, 0]]))
print(s.canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]))
