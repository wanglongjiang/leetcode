'''
到最近的人的最大距离
给你一个数组 seats 表示一排座位，其中 seats[i] = 1 代表有人坐在第 i 个座位上，
seats[i] = 0 代表座位 i 上是空的（下标从 0 开始）。

至少有一个空座位，且至少有一人已经坐在座位上。

亚历克斯希望坐在一个能够使他与离他最近的人之间的距离达到最大化的座位上。

返回他到离他最近的人的最大距离。

 

示例 1：


输入：seats = [1,0,0,0,1,0,1]
输出：2
解释：
如果亚历克斯坐在第二个空位（seats[2]）上，他到离他最近的人的距离为 2 。
如果亚历克斯坐在其它任何一个空位上，他到离他最近的人的距离为 1 。
因此，他到离他最近的人的最大距离是 2 。
示例 2：

输入：seats = [1,0,0,0]
输出：3
解释：
如果亚历克斯坐在最后一个座位上，他离最近的人有 3 个座位远。
这是可能的最大距离，所以答案是 3 。
示例 3：

输入：seats = [0,1]
输出：1
 

提示：

2 <= seats.length <= 2 * 10^4
seats[i] 为 0 或 1
至少有一个 空座位
至少有一个 座位上有人
'''
from typing import List
'''
思路：贪心算法
找到间隔最大的区间，返回区间距离除以2。如果是开头和末尾，距离不需要除以2。

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        maxRange = 0
        preOneIdx = -1
        n = len(seats)
        for i in range(n):
            if seats[i]:
                if (i - preOneIdx) // 2 > maxRange:
                    if preOneIdx == -1:  # 如果坐在第0个位置，距离不需要除以2
                        maxRange = i
                    else:
                        maxRange = (i - preOneIdx) // 2
                preOneIdx = i
        if n - 1 - preOneIdx > maxRange:
            maxRange = n - 1 - preOneIdx
        return maxRange


s = Solution()
print(s.maxDistToClosest(seats=[0, 0, 0, 1]))
print(s.maxDistToClosest(seats=[1, 0, 0, 0, 1, 0, 1]))
print(s.maxDistToClosest(seats=[1, 0, 0, 0]))
print(s.maxDistToClosest(seats=[0, 1]))
