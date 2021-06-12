'''
收集树上所有苹果的最少时间
给你一棵有 n 个节点的无向树，节点编号为 0 到 n-1 ，它们中有一些节点有苹果。通过树上的一条边，需要花费 1 秒钟。
你从 节点 0 出发，请你返回最少需要多少秒，可以收集到所有苹果，并回到节点 0 。

无向树的边由 edges 给出，其中 edges[i] = [fromi, toi] ，表示有一条边连接 from 和 toi 。除此以外，还有一个布尔数组 hasApple ，
其中 hasApple[i] = true 代表节点 i 有一个苹果，否则，节点 i 没有苹果。

 

示例 1：



输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
输出：8
解释：上图展示了给定的树，其中红色节点表示有苹果。一个能收集到所有苹果的最优方案由绿色箭头表示。
示例 2：



输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
输出：6
解释：上图展示了给定的树，其中红色节点表示有苹果。一个能收集到所有苹果的最优方案由绿色箭头表示。
示例 3：

输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
输出：0
 

提示：

1 <= n <= 10^5
edges.length == n-1
edges[i].length == 2
0 <= fromi, toi <= n-1
fromi < toi
hasApple.length == n

'''
from typing import List
'''
思路：树
根据edges，重建树
然后从0开始遍历树，对于当前节点i，
> 如果2个子节点返回值都大于0，返回2个子节点的和减去当前节点的深度。
> 如果只有1个子节点有返回值>0，返回子节点的值
> 如果子节点没有返回值>0，当前节点有苹果，返回当前节点的深度
> 如果子节点没有返回值>0，当前节点没有苹果，返回0
最终将返回值*2 即为最短路径

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        visted = [False] * n

        def dfs(nodeid, depth):
            pathLen = 0
            visted[nodeid] = True
            for nextid in g[nodeid]:
                if visted[nextid]:
                    continue
                nextLen = dfs(nextid, depth + 1)
                if nextLen > 0 and pathLen > 0:
                    pathLen += nextLen - depth
                elif nextLen > 0:
                    pathLen = nextLen
            if pathLen > 0:
                return pathLen
            if hasApple[nodeid]:
                return depth
            return 0

        return dfs(0, 0) * 2


s = Solution()
false, true = False, True
print(s.minTime(4, [[0, 2], [0, 3], [1, 2]], [false, true, false, false]))
print(s.minTime(8, [[0, 1], [1, 2], [2, 3], [1, 4], [2, 5], [2, 6], [4, 7]], [true, true, false, true, false, true, true, false]))
print(s.minTime(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], hasApple=[false, false, true, false, true, true, false]))
print(s.minTime(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], hasApple=[false, false, true, false, false, true, false]))
print(s.minTime(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], hasApple=[false, false, false, false, false, false, false]))
