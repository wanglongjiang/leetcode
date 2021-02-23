'''
爱生气的书店老板

今天，书店老板有一家店打算试营业 customers.length 分钟。每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分钟结束后离开。

在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。 当书店老板生气时，那一分钟的顾客就会不满意，不生气则他们是满意的。

书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 X 分钟不生气，但却只能使用一次。

请你返回这一天营业下来，最多有多少客户能够感到满意的数量。

'''

from typing import List
'''
思路：滑动窗口
通过2个数组可以得到如果老板不控制脾气每分钟会使顾客生气的数组unhappys，问题可以转化为数组unhappys窗口X范围内的最大值，求得最大值之后
答案=sum(customers)-sum(unhappys)+maxHappyNums
时间复杂度：O(n)
空间复杂度：O(n)
优化：unhappys可以通过实时计算得到，这样空间复杂度可以优化为O(1)
'''


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int],
                     X: int) -> int:
        maxHappyNums, happyNums = 0, 0
        sumCustomers, sumUnhappy = 0, 0
        left, right = 0, 0
        for right in range(len(customers)):
            if right - left == X:
                happyNums -= grumpy[left] * customers[left]  # 移动滑动窗口
                left += 1
            unhappy = grumpy[right] * customers[right]
            happyNums += unhappy
            maxHappyNums = max(maxHappyNums, happyNums)
            sumCustomers += customers[right]
            sumUnhappy += unhappy
        return sumCustomers - sumUnhappy + maxHappyNums


s = Solution()
print(
    s.maxSatisfied(customers=[1, 0, 1, 2, 1, 1, 7, 5],
                   grumpy=[0, 1, 0, 1, 0, 1, 0, 1],
                   X=3))
