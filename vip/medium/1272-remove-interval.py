'''
1272. 删除区间
实数集合可以表示为若干不相交区间的并集，其中每个区间的形式为 [a, b)（左闭右开），表示满足 a <= x < b 的所有实数  x 的集合。如果某个区间 [a, b) 中包含实数 x ，则称实数 x 在集合中。

给你一个 有序的 不相交区间列表 intervals 和一个要删除的区间 toBeRemoved 。intervals 表示一个实数集合，其中每一项 intervals[i] = [ai, bi] 都表示一个区间 [ai, bi) 。

请你 intervals 中任意区间与 toBeRemoved 有交集的部分都删除。返回删除所有交集区间后， intervals 剩余部分的 有序 列表。换句话说，返回实数集合，并满足集合中的每个实数 x 都在 intervals 中，但不在 toBeRemoved 中。

 

示例 1：


输入：intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
输出：[[0,1],[6,7]]
示例 2：


输入：intervals = [[0,5]], toBeRemoved = [2,3]
输出：[[0,2],[3,5]]
示例 3：

输入：intervals = [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]], toBeRemoved = [-1,4]
输出：[[-5,-4],[-3,-2],[4,5],[8,9]]
 

提示：

1 <= intervals.length <= 10^4
-10^9 <= ai < bi <= 10^9
'''
from typing import List
'''
思路：TODO
'''


class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        pass
