'''
2249. 统计圆内格点数目
给你一个二维整数数组 circles ，其中 circles[i] = [xi, yi, ri] 表示网格上圆心为 (xi, yi) 且半径为 ri 的第 i 个圆，
返回出现在 至少一个 圆内的 格点数目 。

注意：

格点 是指整数坐标对应的点。
圆周上的点 也被视为出现在圆内的点。
 

示例 1：



输入：circles = [[2,2,1]]
输出：5
解释：
给定的圆如上图所示。
出现在圆内的格点为 (1, 2)、(2, 1)、(2, 2)、(2, 3) 和 (3, 2)，在图中用绿色标识。
像 (1, 1) 和 (1, 3) 这样用红色标识的点，并未出现在圆内。
因此，出现在至少一个圆内的格点数目是 5 。
示例 2：



输入：circles = [[2,2,2],[3,4,1]]
输出：16
解释：
给定的圆如上图所示。
共有 16 个格点出现在至少一个圆内。
其中部分点的坐标是 (0, 2)、(2, 0)、(2, 4)、(3, 2) 和 (4, 4) 。
 

提示：

1 <= circles.length <= 200
circles[i].length == 3
1 <= xi, yi <= 100
1 <= ri <= min(xi, yi)
'''
from typing import List
'''
思路：枚举 哈希
枚举每个圆所有可能的格点，将其坐标加入哈希集合，最后返回哈希集合大小

时间复杂度：O(n*r^2),r为圆的直径
空间复杂度：O(n*r^2)
'''


class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        posHash = set()
        for c in circles:
            for x in range(c[0] - c[2], c[0] + c[2] + 1):
                for y in range(c[1] - c[2], c[1] + c[2] + 1):
                    if abs(x - c[0])**2 + abs(y - c[1])**2 > c[2]**2:
                        continue
                    posHash.add((x, y))
        return len(posHash)


s = Solution()
assert s.countLatticePoints([[2, 2, 1]]) == 5
assert s.countLatticePoints([[2, 2, 2], [3, 4, 1]]) == 16
