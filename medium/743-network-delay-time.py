'''
网络延迟时间

有 n 个网络节点，标记为 1 到 n。

给你一个列表 times，表示信号经过 有向 边的传递时间。 times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点，
 wi 是一个信号从源节点传递到目标节点的时间。

现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。

 

示例 1：
输入：times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
输出：2

示例 2：
输入：times = [[1,2,1]], n = 2, k = 1
输出：1

示例 3：
输入：times = [[1,2,1]], n = 2, k = 2
输出：-1
 

提示：

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
所有 (ui, vi) 对都 互不相同（即，不含重复边）
'''
from typing import List
'''
思路：DFS遍历有向图
首先将边转化为邻接表
然后从k节点出发遍历节点，每遍历一个节点，将其到达时间进行更新。
因图中节点可能有多条路径到达，或者有环路，只有到达时间比之前记录的时间小才重复遍历

时间复杂度：O(m+n)
空间复杂度：O(m+n)
'''


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 输入转为邻接表
        graph = [[] for _ in range(n + 1)]
        for time in times:
            graph[time[0]].append((time[1], time[2]))
        arrivalTimes = [float('inf')] * (n + 1)

        # 遍历节点
        def dfs(nodeid, time):
            if arrivalTimes[nodeid] <= time:
                return
            arrivalTimes[nodeid] = time
            for nextid, nexttime in graph[nodeid]:
                dfs(nextid, time + nexttime)

        dfs(k, 0)
        # 找到最大的到达时间
        ans = float('-inf')
        for time in arrivalTimes[1:]:
            if time == float('inf'):
                return -1
            if ans < time:
                ans = time
        return ans


s = Solution()
print(s.networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))
print(s.networkDelayTime(times=[[1, 2, 1]], n=2, k=1))
print(s.networkDelayTime(times=[[1, 2, 1]], n=2, k=2))
