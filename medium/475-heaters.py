'''
供暖器
冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。

在加热器的加热半径范围内的每个房屋都可以获得供暖。

现在，给出位于一条水平线上的房屋 houses 和供暖器 heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。

说明：所有供暖器都遵循你的半径标准，加热的半径也一样。

 

示例 1:

输入: houses = [1,2,3], heaters = [2]
输出: 1
解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。
示例 2:

输入: houses = [1,2,3,4], heaters = [1,4]
输出: 1
解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
示例 3：

输入：houses = [1,5], heaters = [2]
输出：3
 

提示：

1 <= houses.length, heaters.length <= 3 * 10^4
1 <= houses[i], heaters[i] <= 10^9
'''
from typing import List
import bisect
'''
思路：二分查找
遍历所有热水器，将任意2个热水器之间的距离除以2即为这2个热水器的最小半径，
然后在半径范围内查找最接近边界的房屋，边界处房屋距离热水器的距离即为该热水器的最小半径。
更详细的算法说明见代码注释

时间复杂度：O(m*logn)，m为热水器数量，n为房屋数量
空间复杂度：O(1)
'''


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        m, n = len(heaters), len(houses)
        if m == 1:
            return max(abs(heaters[0] - houses[0]), abs(heaters[0] - houses[-1]))
        ans = 0
        # 第1个房间首先判断第1个热水器左侧的房间
        if heaters[0] > houses[0]:
            ans = heaters[0] - houses[0]
        for i in range(m - 1):
            maxR = (heaters[i + 1] - heaters[i]) / 2  # 计算最大半径，热水器最大半径是2个热水器之间的距离除以2
            pos = bisect.bisect_right(houses, heaters[i] + maxR)  # 找到第i个热水器右侧半径内最远的房间位置
            if pos > 0 and houses[pos - 1] > heaters[i]:  # 确保确实是第i个热水器右侧房间
                ans = max(ans, houses[pos - 1] - heaters[i])  # 确保热水器半径大于等于边界处房屋距离
            pos = bisect.bisect_left(houses, heaters[i + 1] - maxR)  # 找到第i+1个热水器左侧半径内最远的房间位置
            if pos < n and houses[pos] < heaters[i + 1]:  # 确保确实是第i+1个热水器左侧房间
                ans = max(ans, heaters[i + 1] - houses[pos])  # 确保热水器半径大于等于边界处房屋距离
        # 最后一个热水器需要再确认一下右边的房间
        if heaters[-1] < houses[-1]:
            ans = max(ans, houses[-1] - heaters[-1])
        return ans


s = Solution()
print(s.findRadius(houses=[1, 2, 3], heaters=[2]))
print(s.findRadius(houses=[1, 2, 3, 4], heaters=[1, 4]))
print(s.findRadius(houses=[1, 5], heaters=[2]))
