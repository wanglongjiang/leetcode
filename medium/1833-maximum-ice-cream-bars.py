'''
雪糕的最大数量
夏日炎炎，小男孩 Tony 想买一些雪糕消消暑。

商店中新到 n 支雪糕，用长度为 n 的数组 costs 表示雪糕的定价，其中 costs[i] 表示第 i 支雪糕的现金价格。
Tony 一共有 coins 现金可以用于消费，他想要买尽可能多的雪糕。

给你价格数组 costs 和现金量 coins ，请你计算并返回 Tony 用 coins 现金能够买到的雪糕的 最大数量 。

注意：Tony 可以按任意顺序购买雪糕。
'''
from typing import List
'''
思路：贪心算法 排序
排序后从小到达减去现金，直至买不起或者买完

时间复杂度：O(nlogn)
空间复杂度：O(1)
'''


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        for i in range(len(costs)):
            if coins >= costs[i]:
                coins -= costs[i]
            else:
                return i
        return len(costs)


s = Solution()
print(s.maxIceCream(costs=[1, 3, 2, 4, 1], coins=7))
print(s.maxIceCream(costs=[10, 6, 8, 7, 7, 8], coins=5))
print(s.maxIceCream(costs=[1, 6, 3, 1, 2, 5], coins=20))
