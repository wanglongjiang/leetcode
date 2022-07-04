'''
1882. 使用服务器处理任务
给你两个 下标从 0 开始 的整数数组 servers 和 tasks ，长度分别为 n​​​​​​ 和 m​​​​​​ 。
servers[i] 是第 i​​​​​​​​​​ 台服务器的 权重 ，而 tasks[j] 是处理第 j​​​​​​ 项任务 所需要的时间（单位：秒）。

你正在运行一个仿真系统，在处理完所有任务后，该系统将会关闭。每台服务器只能同时处理一项任务。
第 0 项任务在第 0 秒可以开始处理，相应地，第 j 项任务在第 j 秒可以开始处理。
处理第 j 项任务时，你需要为它分配一台 权重最小 的空闲服务器。
如果存在多台相同权重的空闲服务器，请选择 下标最小 的服务器。
如果一台空闲服务器在第 t 秒分配到第 j 项任务，那么在 t + tasks[j] 时它将恢复空闲状态。

如果没有空闲服务器，则必须等待，直到出现一台空闲服务器，并 尽可能早 地处理剩余任务。 
如果有多项任务等待分配，则按照 下标递增 的顺序完成分配。

如果同一时刻存在多台空闲服务器，可以同时将多项任务分别分配给它们。

构建长度为 m 的答案数组 ans ，其中 ans[j] 是第 j 项任务分配的服务器的下标。

返回答案数组 ans​​​​ 。

 

示例 1：

输入：servers = [3,3,2], tasks = [1,2,3,2,1,2]
输出：[2,2,0,2,1,2]
解释：事件按时间顺序如下：
- 0 秒时，第 0 项任务加入到任务队列，使用第 2 台服务器处理到 1 秒。
- 1 秒时，第 2 台服务器空闲，第 1 项任务加入到任务队列，使用第 2 台服务器处理到 3 秒。
- 2 秒时，第 2 项任务加入到任务队列，使用第 0 台服务器处理到 5 秒。
- 3 秒时，第 2 台服务器空闲，第 3 项任务加入到任务队列，使用第 2 台服务器处理到 5 秒。
- 4 秒时，第 4 项任务加入到任务队列，使用第 1 台服务器处理到 5 秒。
- 5 秒时，所有服务器都空闲，第 5 项任务加入到任务队列，使用第 2 台服务器处理到 7 秒。
示例 2：

输入：servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]
输出：[1,4,1,4,1,3,2]
解释：事件按时间顺序如下：
- 0 秒时，第 0 项任务加入到任务队列，使用第 1 台服务器处理到 2 秒。
- 1 秒时，第 1 项任务加入到任务队列，使用第 4 台服务器处理到 2 秒。
- 2 秒时，第 1 台和第 4 台服务器空闲，第 2 项任务加入到任务队列，使用第 1 台服务器处理到 4 秒。
- 3 秒时，第 3 项任务加入到任务队列，使用第 4 台服务器处理到 7 秒。
- 4 秒时，第 1 台服务器空闲，第 4 项任务加入到任务队列，使用第 1 台服务器处理到 9 秒。
- 5 秒时，第 5 项任务加入到任务队列，使用第 3 台服务器处理到 7 秒。
- 6 秒时，第 6 项任务加入到任务队列，使用第 2 台服务器处理到 7 秒。
 

提示：

servers.length == n
tasks.length == m
1 <= n, m <= 2 * 105
1 <= servers[i], tasks[j] <= 2 * 105
'''

from heapq import heapify, heappop, heappush
from typing import List
'''
思路：堆（优先队列）
设最小堆idle，保存当前空闲的服务器（权重，编号）
设最小堆running，保存当前正在运行的服务器（运行截止时间，编号）
首先遍历servers，将所有服务器加入idle。
然后遍历tasks，
- 首先检查截止时间i，是否有运行完毕的服务器，如果有，将其从running中弹出，加入idle
- 然后检查idle是否有空闲的服务器，如果有，将其运行当前任务，加入running；否则将最近时刻要停止运行的服务器加入idle，再挑选一个运行当前任务

时间复杂度：O(mlogn+nlogn)
空间复杂度：O(n)
'''


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        running, idle = [], [(w, i) for i, w in enumerate(servers)]
        heapify(idle)
        ans = []
        releaseTime = 0  # 记录运行服务器的释放时间。
        for time, task in enumerate(tasks):
            while running and time >= running[0][0]:  # 已运行结束的服务器加入idle
                _, i = heappop(running)
                heappush(idle, (servers[i], i))
            if not idle:  # 没有空闲服务器，将最近运行完成的服务器加入idle
                releaseTime = running[0][0]  # 当发生任务延迟运行时，需要记录服务器的释放时间，从释放时间起运行任务
                while running and releaseTime == running[0][0]:
                    heappush(idle, (servers[running[0][1]], running[0][1]))
                    heappop(running)
            _, i = heappop(idle)
            heappush(running, (max(time, releaseTime) + task, i))  # 服务器变为正在运行
            ans.append(i)
        return ans


s = Solution()
print(s.assignTasks(servers=[3, 3, 2], tasks=[1, 2, 3, 2, 1, 2]) == [2, 2, 0, 2, 1, 2])
print(s.assignTasks(servers=[5, 1, 4, 3, 2], tasks=[2, 1, 2, 4, 5, 2, 1]) == [1, 4, 1, 4, 1, 3, 2])
