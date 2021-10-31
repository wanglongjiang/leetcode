'''
335. 路径交叉
给你一个整数数组 distance 。

从 X-Y 平面上的点 (0,0) 开始，先向北移动 distance[0] 米，然后向西移动 distance[1] 米，向南移动 distance[2] 米，向东移动 distance[3] 米，持续移动。也就是说，每次移动后你的方位会发生逆时针变化。

判断你所经过的路径是否相交。如果相交，返回 true ；否则，返回 false 。



示例 1：


输入：distance = [2,1,1,2]
输出：true
示例 2：


输入：distance = [1,2,3,4]
输出：false
示例 3：


输入：distance = [1,1,1,1]
输出：true


提示：

1 <= distance.length <= 10^5
1 <= distance[i] <= 10^5
'''
from typing import List
'''
思路：几何

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        if len(distance) < 4:
            return False
        for i in range(3, len(distance)):
            if distance[i] >= distance[i - 2] and distance[i - 1] <= distance[i - 3]:
                return True
            if distance[i - 1] <= distance[i - 3] and distance[i - 2] <= distance[i]:
                return True
            if i > 3 and distance[i - 1] == distance[i - 3] and distance[i] + distance[i - 4] == distance[i - 2]:
                return True
            if i > 4 and distance[i] + distance[i - 4] >= distance[i - 2] and distance[i - 1] >= distance[i - 3] - distance[i - 5] and distance[
                    i - 1] <= distance[i - 3] and distance[i - 2] >= distance[i - 4] and distance[i - 3] >= distance[i - 5]:
                return True
        return False


s = Solution()
print(s.isSelfCrossing([3, 3, 4, 2, 2]))
