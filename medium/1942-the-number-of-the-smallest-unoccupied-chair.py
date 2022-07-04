'''
1942. 最小未被占据椅子的编号
有 n 个朋友在举办一个派对，这些朋友从 0 到 n - 1 编号。派对里有 无数 张椅子，编号为 0 到 infinity 。
当一个朋友到达派对时，他会占据 编号最小 且未被占据的椅子。

比方说，当一个朋友到达时，如果椅子 0 ，1 和 5 被占据了，那么他会占据 2 号椅子。
当一个朋友离开派对时，他的椅子会立刻变成未占据状态。如果同一时刻有另一个朋友到达，可以立即占据这张椅子。

给你一个下标从 0 开始的二维整数数组 times ，其中 times[i] = [arrivali, leavingi] 表示第 i 个朋友到达和离开的时刻，
同时给你一个整数 targetFriend 。所有到达时间 互不相同 。

请你返回编号为 targetFriend 的朋友占据的 椅子编号 。

 

示例 1：

输入：times = [[1,4],[2,3],[4,6]], targetFriend = 1
输出：1
解释：
- 朋友 0 时刻 1 到达，占据椅子 0 。
- 朋友 1 时刻 2 到达，占据椅子 1 。
- 朋友 1 时刻 3 离开，椅子 1 变成未占据。
- 朋友 0 时刻 4 离开，椅子 0 变成未占据。
- 朋友 2 时刻 4 到达，占据椅子 0 。
朋友 1 占据椅子 1 ，所以返回 1 。
示例 2：

输入：times = [[3,10],[1,5],[2,6]], targetFriend = 0
输出：2
解释：
- 朋友 1 时刻 1 到达，占据椅子 0 。
- 朋友 2 时刻 2 到达，占据椅子 1 。
- 朋友 0 时刻 3 到达，占据椅子 2 。
- 朋友 1 时刻 5 离开，椅子 0 变成未占据。
- 朋友 2 时刻 6 离开，椅子 1 变成未占据。
- 朋友 0 时刻 10 离开，椅子 2 变成未占据。
朋友 0 占据椅子 2 ，所以返回 2 。
 

提示：

n == times.length
2 <= n <= 104
times[i].length == 2
1 <= arrivali < leavingi <= 105
0 <= targetFriend <= n - 1
每个 arrivali 时刻 互不相同 。
'''
from heapq import heappop, heappush
from typing import List
'''
思路：优先队列（堆）
设最小堆friends，保存当前在场的朋友，以离开时间排序
设最小堆chairs，保存当前空闲的椅子
设变量unuseNo，保存未使用过的最近椅子号，初始值为0

将times按照入场时间排序，然后遍历
对于times[i]，首先检查friends中是否有在其到达前立场的人，如果有将其出场，同时离场的人的椅子加入chairs。
然后检查chairs是否为空，如果不为空，从中取出一个椅子给这个人，否则将unuseNo给这个人。
遍历过程中，如果找到了targetFriend，则返回其使用的椅子号

时间复杂度：O(nlogn)，需要1次排序，最坏情况下每个元素还会出入堆一次
空间复杂度：O(n)
'''


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        friends, chairs, unuseNo = [], [], 0
        for i in range(len(times)):  # 为每个朋友添加编号
            times[i].append(i)
        times.sort(key=lambda t: t[0])
        for t in times:
            while friends and friends[0][0] <= t[0]:  # 将在t之前出场的人的椅子进行回收
                heappush(chairs, heappop(friends)[1])
            if chairs:  # 如果有之前被释放的椅子，将编号最小的一个重复利用
                if t[2] == targetFriend:
                    return chairs[0]
                heappush(friends, (t[1], heappop(chairs)))
            else:
                if t[2] == targetFriend:
                    return unuseNo
                heappush(friends, (t[1], unuseNo))
                unuseNo += 1
