'''
用最少数量的箭引爆气球
在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。
由于它是水平的，所以纵坐标并不重要，因此只要知道开始和结束的横坐标就足够了。开始坐标总是小于结束坐标。

一支弓箭可以沿着 x 轴从不同点完全垂直地射出。在坐标 x 处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend，
且满足  xstart ≤ x ≤ xend，则该气球会被引爆。可以射出的弓箭的数量没有限制。
弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。

给你一个数组 points ，其中 points [i] = [xstart,xend] ，返回引爆所有气球所必须射出的最小弓箭数。

 
示例 1：

输入：points = [[10,16],[2,8],[1,6],[7,12]]
输出：2
解释：对于该样例，x = 6 可以射爆 [2,8],[1,6] 两个气球，以及 x = 11 射爆另外两个气球
示例 2：

输入：points = [[1,2],[3,4],[5,6],[7,8]]
输出：4
示例 3：

输入：points = [[1,2],[2,3],[3,4],[4,5]]
输出：2
示例 4：

输入：points = [[1,2]]
输出：1
示例 5：

输入：points = [[2,3],[2,3]]
输出：1
 

提示：

0 <= points.length <= 10^4
points[i].length == 2
-231 <= xstart < xend <= 231 - 1
'''
from typing import List
'''
思路：排序
1. 按照气球左边界排序
2. 遍历所有气球，
> 如果当前气球左边界在之前气球的边界范围内，当前气球可以与之前气球用同一根箭。同时更新之前边界为min(之前的边界，当前气球右边界)
> 如果当前气球左边界在之前气球的边界范围外，箭数需要+1，更新边界为当前气球的右边界。

时间复杂度：O(nlogn)，排序需要O(nlogn)
空间复杂度：O(1)
'''


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: p[0])  # 按照左边界排序
        ans = 0
        limit = float('-inf')
        for p in points:
            if p[0] > limit:
                ans += 1
                limit = p[1]
            else:
                limit = min(limit, p[1])
        return ans


s = Solution()
print(s.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
print(s.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]))
print(s.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))
print(s.findMinArrowShots([[1, 2]]))
print(s.findMinArrowShots([[2, 3], [2, 3]]))
