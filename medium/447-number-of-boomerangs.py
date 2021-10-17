'''
447. 回旋镖的数量
给定平面上 n 对 互不相同 的点 points ，其中 points[i] = [xi, yi] 。回旋镖 是由点 (i, j, k) 表示的元组 ，
其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。

返回平面上所有回旋镖的数量。


示例 1：

输入：points = [[0,0],[1,0],[2,0]]
输出：2
解释：两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]

示例 2：

输入：points = [[1,1],[2,2],[3,3]]
输出：2

示例 3：

输入：points = [[1,1]]
输出：0


提示：

n == points.length
1 <= n <= 500
points[i].length == 2
-10^4 <= xi, yi <= 10^4
所有点都 互不相同
'''
from typing import List
from collections import defaultdict
import math
'''
思路：几何 数学
暴力计算某点到其他所有点的距离，并记录到哈希表中。
对于同一个距离c，如果>=2个点，那么任意2条边都可以构成回旋镖也就是排列：
$A^{m}_{n}$= $\frac{n!}{(n-m)!}$

时间复杂度：O(n^2)
空间复杂度：O(n)
'''


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for p1 in points:
            counter = defaultdict(int)
            for p2 in points:
                counter[(p1[0] - p2[0])**2 + (p1[1] - p2[1])**2] += 1  # 统计与p1所有的距离
            counts = filter(lambda cnt: cnt > 1, counter.values())  # 过滤出过一点，边长相同，>=2的
            ans += sum(map(lambda cnt: math.factorial(cnt) // (math.factorial(cnt - 2)), counts))  # 用排列公式计算数量
        return ans


s = Solution()
print(s.numberOfBoomerangs([[0, 0], [1, 0], [2, 0]]))
print(s.numberOfBoomerangs([[1, 1], [2, 2], [3, 3]]))
print(s.numberOfBoomerangs([[1, 1]]))
