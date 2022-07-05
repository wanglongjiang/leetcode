'''
1642. 可以到达的最远建筑
给你一个整数数组 heights ，表示建筑物的高度。另有一些砖块 bricks 和梯子 ladders 。

你从建筑物 0 开始旅程，不断向后面的建筑物移动，期间可能会用到砖块或梯子。

当从建筑物 i 移动到建筑物 i+1（下标 从 0 开始 ）时：

如果当前建筑物的高度 大于或等于 下一建筑物的高度，则不需要梯子或砖块
如果当前建筑的高度 小于 下一个建筑的高度，您可以使用 一架梯子 或 (h[i+1] - h[i]) 个砖块
如果以最佳方式使用给定的梯子和砖块，返回你可以到达的最远建筑物的下标（下标 从 0 开始 ）。
 

示例 1：


输入：heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
输出：4
解释：从建筑物 0 出发，你可以按此方案完成旅程：
- 不使用砖块或梯子到达建筑物 1 ，因为 4 >= 2
- 使用 5 个砖块到达建筑物 2 。你必须使用砖块或梯子，因为 2 < 7
- 不使用砖块或梯子到达建筑物 3 ，因为 7 >= 6
- 使用唯一的梯子到达建筑物 4 。你必须使用砖块或梯子，因为 6 < 9
无法越过建筑物 4 ，因为没有更多砖块或梯子。
示例 2：

输入：heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
输出：7
示例 3：

输入：heights = [14,3,19,3], bricks = 17, ladders = 0
输出：3
 

提示：

1 <= heights.length <= 105
1 <= heights[i] <= 106
0 <= bricks <= 109
0 <= ladders <= heights.length
'''

from heapq import heappop, heappush
from typing import List
'''
思路：贪心 堆（优先队列）
1、优先使用砖块，直至所有的砖块都被用尽
2、因为梯子可以跨过任意高度的高度差，所以从已经过的所有楼间距离中挑选出最大的一个用梯子，释放出砖块
3、重复上述过程，直至所有梯子、砖块都被用掉，返回此时的坐标。

时间复杂度：O(nlogn)，需要用堆保存楼的高度差，最坏情况下所有高度差入堆
空间复杂度：O(n)
'''


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        i, n = 0, len(heights)
        heap = []
        while i < n - 1 and (ladders > 0 or bricks >= heights[i + 1] - heights[i]):
            while i < n - 1 and bricks >= heights[i + 1] - heights[i]:  # 用掉所有的砖块
                if heights[i + 1] - heights[i] > 0:
                    bricks -= heights[i + 1] - heights[i]
                    heappush(heap, -heights[i + 1] + heights[i])
                i += 1
            if i < n - 1 and ladders:
                if heap and -heap[0] > heights[i + 1] - heights[i]:  # 如果下一个高度差比之前的小，需要用梯子替换之前的砖块
                    bricks += -heappop(heap)  # 砖块变成可用的
                else:  # 如果下一个高度差更大，或者没有砖块，直接用掉梯子前进一步
                    i += 1
                ladders -= 1  # 用掉一个梯子
        return i


s = Solution()
assert s.furthestBuilding(heights=[4, 12, 2, 7, 3, 18, 20, 3, 19], bricks=10, ladders=2) == 7
assert s.furthestBuilding(heights=[4, 2, 7, 6, 9, 14, 12], bricks=5, ladders=1) == 4
assert s.furthestBuilding(heights=[14, 3, 19, 3], bricks=17, ladders=0) == 3
assert s.furthestBuilding([1, 5, 1, 2, 3, 4, 10000], 4, 1) == 5
