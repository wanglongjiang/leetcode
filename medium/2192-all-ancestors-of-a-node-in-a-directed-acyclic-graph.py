'''
2192. 有向无环图中一个节点的所有祖先
给你一个正整数 n ，它表示一个 有向无环图 中节点的数目，节点编号为 0 到 n - 1 （包括两者）。

给你一个二维整数数组 edges ，其中 edges[i] = [fromi, toi] 表示图中一条从 fromi 到 toi 的单向边。

请你返回一个数组 answer，其中 answer[i]是第 i 个节点的所有 祖先 ，这些祖先节点 升序 排序。

如果 u 通过一系列边，能够到达 v ，那么我们称节点 u 是节点 v 的 祖先 节点。

 

示例 1：



输入：n = 8, edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
输出：[[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]
解释：
上图为输入所对应的图。
- 节点 0 ，1 和 2 没有任何祖先。
- 节点 3 有 2 个祖先 0 和 1 。
- 节点 4 有 2 个祖先 0 和 2 。
- 节点 5 有 3 个祖先 0 ，1 和 3 。
- 节点 6 有 5 个祖先 0 ，1 ，2 ，3 和 4 。
- 节点 7 有 4 个祖先 0 ，1 ，2 和 3 。
示例 2：



输入：n = 5, edgeList = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
输出：[[],[0],[0,1],[0,1,2],[0,1,2,3]]
解释：
上图为输入所对应的图。
- 节点 0 没有任何祖先。
- 节点 1 有 1 个祖先 0 。
- 节点 2 有 2 个祖先 0 和 1 。
- 节点 3 有 3 个祖先 0 ，1 和 2 。
- 节点 4 有 4 个祖先 0 ，1 ，2 和 3 。
 

提示：

1 <= n <= 1000
0 <= edges.length <= min(2000, n * (n - 1) / 2)
edges[i].length == 2
0 <= fromi, toi <= n - 1
fromi != toi
图中不会有重边。
图是 有向 且 无环 的。
'''

from collections import deque
from typing import List
'''
思路：拓扑排序
对节点进行拓扑排序，排序过程中将本节点和本节点的上一节点加入下一节点的祖先中

时间复杂度：O(n^2)
空间复杂度：O(n^2)
'''


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indegree = [0] * n  # 拓扑排序用的入度数组
        g = [[] for _ in range(n)]  # 邻接表，记录下一节点
        ancestors = [set() for _ in range(n)]  # 祖先节点
        for e in edges:
            indegree[e[1]] += 1
            g[e[0]].append(e[1])
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            for next in g[node]:
                indegree[next] -= 1
                ancestors[next].add(node)  # 将当前节点添加到下一节点的祖先中
                ancestors[next].update(ancestors[node])  # 将当前节点的祖先添加给下一节点的祖先
                if indegree[next] == 0:
                    q.append(next)
        return [list(sorted(a)) for a in ancestors]  # 祖先节点排序后输出


s = Solution()
print(
    s.getAncestors(8, [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]) == [[], [], [], [0, 1], [0, 2], [0, 1, 3], [0, 1, 2, 3, 4],
                                                                                                    [0, 1, 2, 3]])
print(s.getAncestors(5, [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]) == [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]])
