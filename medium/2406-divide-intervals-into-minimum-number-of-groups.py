'''
2406. 将区间分为最少组数
给你一个二维整数数组 intervals ，其中 intervals[i] = [lefti, righti] 表示 闭 区间 [lefti, righti] 。

你需要将 intervals 划分为一个或者多个区间 组 ，每个区间 只 属于一个组，且同一个组中任意两个区间 不相交 。

请你返回 最少 需要划分成多少个组。

如果两个区间覆盖的范围有重叠（即至少有一个公共数字），那么我们称这两个区间是 相交 的。比方说区间 [1, 5] 和 [5, 8] 相交。

 

示例 1：

输入：intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
输出：3
解释：我们可以将区间划分为如下的区间组：
- 第 1 组：[1, 5] ，[6, 8] 。
- 第 2 组：[2, 3] ，[5, 10] 。
- 第 3 组：[1, 10] 。
可以证明无法将区间划分为少于 3 个组。
示例 2：

输入：intervals = [[1,3],[5,6],[8,10],[11,13]]
输出：1
解释：所有区间互不相交，所以我们可以把它们全部放在一个组内。
 

提示：

1 <= intervals.length <= 105
intervals[i].length == 2
1 <= lefti <= righti <= 106
'''
import heapq
from typing import List
'''
思路：排序 优先队列（堆）
题目要求同一组内的区间不能相交，可以用贪心的方式，找到一个区间后，将下一个最近的与其不相交的放入同一组。

设一个优先队列，用于保存每个组的最后一个区间的right。
首先按照left排序intervals。
然后遍历intervals，对于当前区间intervals[i]，
    如果它的left与优先队列中的第1个组没有重叠，可以将它加入第1个组，然后更新第1个组的right；
    如果与优先队列中的第1个组没有重叠，它必须创建一个新的组，加入优先队列。
最后返回优先队列的长度，即为答案。

时间复杂度：O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[0])
        h = [intervals[0][1]]
        for interval in intervals[1:]:
            if interval[0] > h[0]:
                heapq.heapreplace(h, interval[1])
            else:
                heapq.heappush(h, interval[1])
        return len(h)
