'''
有向图中最大颜色值
给你一个 有向图 ，它含有 n 个节点和 m 条边。节点编号从 0 到 n - 1 。

给你一个字符串 colors ，其中 colors[i] 是小写英文字母，表示图中第 i 个节点的 颜色 （下标从 0 开始）。
同时给你一个二维数组 edges ，其中 edges[j] = [aj, bj] 表示从节点 aj 到节点 bj 有一条 有向边 。

图中一条有效 路径 是一个点序列 x1 -> x2 -> x3 -> ... -> xk ，对于所有 1 <= i < k ，从 xi 到 xi+1 在图中有一条有向边。
路径的 颜色值 是路径中 出现次数最多 颜色的节点数目。

请你返回给定图中有效路径里面的 最大颜色值 。如果图中含有环，请返回 -1 。

 

示例 1：
输入：colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
输出：3
解释：路径 0 -> 2 -> 3 -> 4 含有 3 个颜色为 "a" 的节点（上图中的红色节点）。

示例 2：
输入：colors = "a", edges = [[0,0]]
输出：-1
解释：从 0 到 0 有一个环。
 

提示：

n == colors.length
m == edges.length
1 <= n <= 10^5
0 <= m <= 10^5
colors 只含有小写英文字母。
0 <= aj, bj < n
'''
from typing import List
'''
思路：DFS遍历
1. 遍历edges构造邻接表形式的图
2. 遍历所有节点i，从i出发遍历图，当前节点的最大颜色值要存储到大小为26的数组中
> 数组中每一项为对应颜色的颜色值，当前节点颜色值数组各项需要设置为下级各个颜色最大的
> 遍历过程中需要用一个set保存当前路径，如果路径中出现环路，则不需要继续遍历了，最大颜色值为-1

时间复杂度：O(n)，精确点需要O(26n)
空间复杂度：O(n)，也是需要O(26n)
'''


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        g = [[] for _ in range(n)]  # 图
        colorCount = [[0] * 26 for _ in range(n)]  # 每个节点上最大颜色值上的路径上所有颜色值
        maxColorNum = 0
        colorbase = ord('a')
        # 1. 构造邻接表形式的图
        for e in edges:
            g[e[0]].append(e[1])
        # 2. dfs遍历图
        visted = [False] * n

        def dfs(i, pathNodes: set):
            nonlocal maxColorNum
            visted[i] = True
            pathNodes.add(i)
            for nexti in g[i]:
                if nexti in pathNodes:  # 如果下一个节点已经在路径中，有环路需要退出
                    maxColorNum = -1
                    return
                if not visted[nexti]:
                    dfs(nexti, pathNodes)
                    if maxColorNum < 0:  # 有环路
                        return
                for j in range(26):  # 各颜色都选择最大的一个
                    colorCount[i][j] = max(colorCount[i][j], colorCount[nexti][j])
            color = ord(colors[i]) - colorbase
            colorCount[i][color] += 1  # 加上当前颜色的计数
            maxColorNum = max(maxColorNum, colorCount[i][color])
            pathNodes.remove(i)

        for i in range(n):
            if not visted[i]:
                dfs(i, set())
            if maxColorNum < 0:
                break
        return maxColorNum


s = Solution()
print(s.largestPathValue(colors="abaca", edges=[[0, 1], [0, 2], [2, 3], [3, 4]]))
print(s.largestPathValue("xxbgbgxgbx", [[0, 1], [1, 2], [0, 3], [2, 4], [4, 5], [5, 6], [5, 7], [4, 8], [4, 9]]))
print(s.largestPathValue(colors="a", edges=[[0, 0]]))
