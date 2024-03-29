'''
剑指 Offer 63. 股票的最大利润
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

 

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
 

限制：

0 <= 数组长度 <= 10^5

 

注意：本题与主站 121 题相同：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
'''
from typing import List
'''
思路：贪心算法
因为只买卖1次，所以设一个最低价格minPrice，初始值为MaxInt，利润profit = 0
然后遍历数组，
> 如果当前元素prices[i]<minPrice，则更新minPrice
> 如果当前元素prices[i]>minPrice，则尝试更新最大利润，即profit = max(profit, prices[i]-minPrice)

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, minPrice = 0, float('inf')
        for price in prices:
            if price < minPrice:
                minPrice = price
            else:
                profit = max(profit, price - minPrice)
        return profit
