'''
天际线问题
城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。给你所有建筑物的位置和高度，请返回由这些建筑物形成的 天际线 。

每个建筑物的几何信息由数组 buildings 表示，其中三元组 buildings[i] = [lefti, righti, heighti] 表示：

lefti 是第 i 座建筑物左边缘的 x 坐标。
righti 是第 i 座建筑物右边缘的 x 坐标。
heighti 是第 i 座建筑物的高度。
天际线 应该表示为由 “关键点” 组成的列表，格式 [[x1,y1],[x2,y2],...] ，并按 x 坐标 进行 排序 。
关键点是水平线段的左端点。列表中最后一个点是最右侧建筑物的终点，y 坐标始终为 0 ，仅用于标记天际线的终点。
此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。

注意：输出天际线中不得有连续的相同高度的水平线。例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...] 是不正确的答案；
三条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...]
'''
from typing import List
from sortedcontainers import SortedList
import heapq
'''
思路：扫描线 堆 有序集合
将左上角和右上角坐标加入最小堆排序。
依次从堆中取出最小的坐标：
> 如果是左上角，需要将高度加入有序集合
> 如果是右上角，需要从有序集合中删除高度
> 如果有序集合中的最大高度发生变化，说明天际线出现拐点，需要记录到结果中

时间复杂度：O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        allCorner = []
        for b in buildings:
            heapq.heappush(allCorner, (b[0], -b[2]))  # 左上角坐标
            heapq.heappush(allCorner, (b[1], b[2]))  # 右上角坐标,高度取负，以区分左上角
        lastHeight, heights = 0, SortedList([0])
        ans = []
        while allCorner:
            c = heapq.heappop(allCorner)
            if c[1] > 0:
                heights.remove(c[1])
            else:
                heights.add(-c[1])
            maxHeight = heights[-1]
            if lastHeight != maxHeight:
                ans.append([c[0], maxHeight])
                lastHeight = maxHeight

        return ans


s = Solution()
print(s.getSkyline([[4, 9, 10], [4, 9, 15], [4, 9, 12], [10, 12, 10], [10, 12, 8]]) == [[4, 15], [9, 0], [10, 10], [12, 0]])
print(s.getSkyline([[1, 2, 1], [1, 2, 2], [1, 2, 3], [2, 3, 1], [2, 3, 2], [2, 3, 3]]))
print(s.getSkyline([[1, 2, 1], [1, 2, 2], [1, 2, 3]]))
print(s.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
print(s.getSkyline([[0, 2, 3], [2, 5, 3]]))
