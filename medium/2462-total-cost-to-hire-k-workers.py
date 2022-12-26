'''
2462. 雇佣 K 位工人的总代价

给你一个下标从 0 开始的整数数组 costs ，其中 costs[i] 是雇佣第 i 位工人的代价。

同时给你两个整数 k 和 candidates 。我们想根据以下规则恰好雇佣 k 位工人：

总共进行 k 轮雇佣，且每一轮恰好雇佣一位工人。
在每一轮雇佣中，从最前面 candidates 和最后面 candidates 人中选出代价最小的一位工人，如果有多位代价相同且最小的工人，选择下标更小的一位工人。
比方说，costs = [3,2,7,7,1,2] 且 candidates = 2 ，第一轮雇佣中，我们选择第 4 位工人，因为他的代价最小 [3,2,7,7,1,2] 。
第二轮雇佣，我们选择第 1 位工人，因为他们的代价与第 4 位工人一样都是最小代价，而且下标更小，[3,2,7,7,2] 。注意每一轮雇佣后，剩余工人的下标可能会发生变化。
如果剩余员工数目不足 candidates 人，那么下一轮雇佣他们中代价最小的一人，如果有多位代价相同且最小的工人，选择下标更小的一位工人。
一位工人只能被选择一次。
返回雇佣恰好 k 位工人的总代价。

 

示例 1：

输入：costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
输出：11
解释：我们总共雇佣 3 位工人。总代价一开始为 0 。
- 第一轮雇佣，我们从 [17,12,10,2,7,2,11,20,8] 中选择。最小代价是 2 ，有两位工人，我们选择下标更小的一位工人，即第 3 位工人。总代价是 0 + 2 = 2 。
- 第二轮雇佣，我们从 [17,12,10,7,2,11,20,8] 中选择。最小代价是 2 ，下标为 4 ，总代价是 2 + 2 = 4 。
- 第三轮雇佣，我们从 [17,12,10,7,11,20,8] 中选择，最小代价是 7 ，下标为 3 ，总代价是 4 + 7 = 11 。注意下标为 3 的工人同时在最前面和最后面 4 位工人中。
总雇佣代价是 11 。
示例 2：

输入：costs = [1,2,4,1], k = 3, candidates = 3
输出：4
解释：我们总共雇佣 3 位工人。总代价一开始为 0 。
- 第一轮雇佣，我们从 [1,2,4,1] 中选择。最小代价为 1 ，有两位工人，我们选择下标更小的一位工人，即第 0 位工人，总代价是 0 + 1 = 1 。注意，下标为 1 和 2 的工人同时在最前面和最后面 3 位工人中。
- 第二轮雇佣，我们从 [2,4,1] 中选择。最小代价为 1 ，下标为 2 ，总代价是 1 + 1 = 2 。
- 第三轮雇佣，少于 3 位工人，我们从剩余工人 [2,4] 中选择。最小代价是 2 ，下标为 0 。总代价为 2 + 2 = 4 。
总雇佣代价是 4 。
 

提示：

1 <= costs.length <= 105 
1 <= costs[i] <= 105
1 <= k, candidates <= costs.length
'''
import heapq
from typing import List
'''
[TOC]

# 思路
优先队列（堆）

# 解题方法
> 将costs两端大小分别为candidates子数组分别加入2个堆
> 循环k次，每次先对比2个堆的最小元素，取较小的那个堆中最小的，被取出一个数值的堆，需要用数组costs中的补充进去
> 需要注意的是，1、数组costs的大小有可能小于2*candidates，那么右边的堆大小就不是candidates了；
> 2、两个堆分别从2端向中间吞并costs，需要维护2个指针，指向下一个要被吞并的元素，吞并的时候要进行判定，避免重复吞并。

# 复杂度
- 时间复杂度: 
>  $O(k+candidates*log(candidates))$

- 空间复杂度: 
> $O(candidates)$
'''


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n, ans = len(costs), 0
        leftHeap, rightHeap = costs[:candidates], costs[-candidates if 2 * candidates <= n else (n if candidates >= n else -(n - candidates)):]  # 定义2个堆
        heapq.heapify(leftHeap)
        heapq.heapify(rightHeap)
        left, right = min(candidates, n), n - len(rightHeap) - 1  # 2个指针分别指向2个堆下一个要吞并的元素
        for _ in range(k):
            if leftHeap and rightHeap:  # 2个堆中都有元素，弹出最小的那个累计入结果，然后从costs中补充给堆
                if leftHeap[0] <= rightHeap[0]:
                    ans += heapq.heappop(leftHeap)
                    if left <= right:  # 2个指针未相遇，可以补充
                        heapq.heappush(leftHeap, costs[left])
                        left += 1
                else:
                    ans += heapq.heappop(rightHeap)
                    if left <= right:  # 2个指针未相遇，可以补充
                        heapq.heappush(rightHeap, costs[right])
                        right -= 1
            elif leftHeap:
                ans += heapq.heappop(leftHeap)
            elif rightHeap:
                ans += heapq.heappop(rightHeap)
        return ans


s = Solution()
assert s.totalCost(costs=[31, 25, 72, 79, 74, 65, 84, 91, 18, 59, 27, 9, 81, 33, 17, 58], k=11, candidates=2) == 423
assert s.totalCost(costs=[17, 12, 10, 2, 7, 2, 11, 20, 8], k=3, candidates=4) == 11
assert s.totalCost(costs=[1, 2, 4, 1], k=3, candidates=3) == 4
assert s.totalCost(costs=[1, 2, 1], k=3, candidates=3) == 4
assert s.totalCost(costs=[1, 2], k=3, candidates=3) == 3
