'''
1606. 找到处理最多请求的服务器
你有 k 个服务器，编号为 0 到 k-1 ，它们可以同时处理多个请求组。每个服务器有无穷的计算能力但是 不能同时处理超过一个请求 。
请求分配到服务器的规则如下：

第 i （序号从 0 开始）个请求到达。
如果所有服务器都已被占据，那么该请求被舍弃（完全不处理）。
如果第 (i % k) 个服务器空闲，那么对应服务器会处理该请求。
否则，将请求安排给下一个空闲的服务器（服务器构成一个环，必要的话可能从第 0 个服务器开始继续找下一个空闲的服务器）。
比方说，如果第 i 个服务器在忙，那么会查看第 (i+1) 个服务器，第 (i+2) 个服务器等等。
给你一个 严格递增 的正整数数组 arrival ，表示第 i 个任务的到达时间，和另一个数组 load ，
其中 load[i] 表示第 i 个请求的工作量（也就是服务器完成它所需要的时间）。你的任务是找到 最繁忙的服务器 。
最繁忙定义为一个服务器处理的请求数是所有服务器里最多的。

请你返回包含所有 最繁忙服务器 序号的列表，你可以以任意顺序返回这个列表。

 

示例 1：



输入：k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3] 
输出：[1] 
解释：
所有服务器一开始都是空闲的。
前 3 个请求分别由前 3 台服务器依次处理。
请求 3 进来的时候，服务器 0 被占据，所以它呗安排到下一台空闲的服务器，也就是服务器 1 。
请求 4 进来的时候，由于所有服务器都被占据，该请求被舍弃。
服务器 0 和 2 分别都处理了一个请求，服务器 1 处理了两个请求。所以服务器 1 是最忙的服务器。
示例 2：

输入：k = 3, arrival = [1,2,3,4], load = [1,2,1,2]
输出：[0]
解释：
前 3 个请求分别被前 3 个服务器处理。
请求 3 进来，由于服务器 0 空闲，它被服务器 0 处理。
服务器 0 处理了两个请求，服务器 1 和 2 分别处理了一个请求。所以服务器 0 是最忙的服务器。
示例 3：

输入：k = 3, arrival = [1,2,3], load = [10,12,11]
输出：[0,1,2]
解释：每个服务器分别处理了一个请求，所以它们都是最忙的服务器。
示例 4：

输入：k = 3, arrival = [1,2,3,4,8,9,10], load = [5,2,10,3,1,2,2]
输出：[1]
示例 5：

输入：k = 1, arrival = [1], load = [1]
输出：[0]
 

提示：

1 <= k <= 10^5
1 <= arrival.length, load.length <= 10^5
arrival.length == load.length
1 <= arrival[i], load[i] <= 109
arrival 保证 严格递增 。

'''
from sortedcontainers import SortedList
from typing import List
import heapq
'''
思路：堆（优先队列） 有序列表
设一个堆h和有序列表li
h中保存二元组(完成请求时间，服务器编号)
li中保存空闲的服务器编号

遍历arrival，对于当前元素arrival[i]:
> 将h中完成时间<=arrival[i]的从堆中删除，并将空闲服务器编号加入li
> li中查找元素i，将>=i的第1个元素从列表中删除并返回，如果没有将最小的元素从列表中删除，如果li为空，该请求放弃
> 上面找到的服务器编号no，与任务完成时间time = arrival[i]+load[i] 构成二元组(time,no)加入h
在迭代过程中记录每个服务器的完成任务数

时间复杂度：O(klogk)
空间复杂度：O(k)
'''


class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        li = SortedList(range(k))  # 空闲服务器列表
        h = []  # 正处理请求的服务器队列
        count = [0] * k  # 每个服务器完成任务计数
        for i in range(len(arrival)):
            while h and h[0][0] <= arrival[i]:  # 将已完成任务的服务器加入空闲队列
                t, no = heapq.heappop(h)
                li.add(no)
                count[no] += 1
            if len(li) == 0:  # 没有空闲服务器，扔掉当前请求
                continue
            j = li.bisect_left(i % k)  # 从i%k开始查找空闲服务器编号
            if j == len(li):
                j = 0
            no = li.pop(j)
            heapq.heappush(h, (arrival[i] + load[i], no))  # 空闲服务器进入已处理请求的队列
        for t, no in h:
            count[no] += 1
        maxval = max(count)
        return [i for i in range(k) if count[i] == maxval]  # 得到完成任务最多的服务器list


s = Solution()
print(s.busiestServers(k=3, arrival=[1, 2, 3, 4, 5], load=[5, 2, 3, 3, 3]))
print(s.busiestServers(k=3, arrival=[1, 2, 3, 4], load=[1, 2, 1, 2]))
print(s.busiestServers(k=3, arrival=[1, 2, 3], load=[10, 12, 11]))
print(s.busiestServers(k=3, arrival=[1, 2, 3, 4, 8, 9, 10], load=[5, 2, 10, 3, 1, 2, 2]))
print(s.busiestServers(k=1, arrival=[1], load=[1]))
