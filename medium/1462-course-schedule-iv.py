'''
课程表 IV
你总共需要上 n 门课，课程编号依次为 0 到 n-1 。

有的课会有直接的先修课程，比如如果想上课程 0 ，你必须先上课程 1 ，那么会以 [1,0] 数对的形式给出先修课程数对。

给你课程总数 n 和一个直接先修课程数对列表 prerequisite 和一个查询对列表 queries 。

对于每个查询对 queries[i] ，请判断 queries[i][0] 是否是 queries[i][1] 的先修课程。

请返回一个布尔值列表，列表中每个元素依次分别对应 queries 每个查询对的判断结果。

注意：如果课程 a 是课程 b 的先修课程且课程 b 是课程 c 的先修课程，那么课程 a 也是课程 c 的先修课程。

提示：

2 <= n <= 100
0 <= prerequisite.length <= (n * (n - 1) / 2)
0 <= prerequisite[i][0], prerequisite[i][1] < n
prerequisite[i][0] != prerequisite[i][1]
先修课程图中没有环。
先修课程图中没有重复的边。
1 <= queries.length <= 10^4
queries[i][0] != queries[i][1]
'''
from typing import List
'''
思路：DFS搜索
有向图的搜索，从queries[i][1]开始，向上搜索其先修课程，如果能找到，则结果为True,否则为false
时间复杂度：O(mn)，m=queries.length,n=课程总数
空间复杂度：O(n)
'''


class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        before = [set() for _ in range(n)]  # 先修课程构成邻接表
        for prereq in prerequisites:  # 初始化先修课程邻接表
            before[prereq[1]].add(prereq[0])
        ans = []

        # dfs遍历图，查询是否是先修课程
        def dfs(c1, c2):
            if c1 in before[c2]:
                return True
            for pre in before[c2]:
                if dfs(c1, pre):
                    return True
            return False

        # 遍历querie，判断是否为先修课程对
        for q in queries:
            ans.append(dfs(q[0], q[1]))
        return ans


s = Solution()
print(s.checkIfPrerequisite(n=2, prerequisites=[[1, 0]], queries=[[0, 1], [1, 0]]))
print(s.checkIfPrerequisite(n=2, prerequisites=[], queries=[[1, 0], [0, 1]]))
print(s.checkIfPrerequisite(n=3, prerequisites=[[1, 2], [1, 0], [2, 0]], queries=[[1, 0], [1, 2]]))
print(s.checkIfPrerequisite(n=3, prerequisites=[[1, 0], [2, 0]], queries=[[0, 1], [2, 0]]))
print(s.checkIfPrerequisite(n=5, prerequisites=[[0, 1], [1, 2], [2, 3], [3, 4]], queries=[[0, 4], [4, 0], [1, 3], [3, 0]]))
