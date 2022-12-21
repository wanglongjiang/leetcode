'''
买卖股票的最佳时机 III
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
'''
from typing import List
'''
思路1，暴力计算。最多可以买2次，可以将数组从下标i将数组分成2部分，分别计算1..i和i+1..n的最大利润，找到利润和最大值
    计算数组的最大利润可以调用121的O(n)算法，切分数组共有n种切分方法
    时间复杂度：O(n^2)，按数据规模来看，达到10^10，可能会超时
    空间复杂度：O(1)
思路2，动态规划。
    1..i的最大利润和1..i+1的最大利润具有最优子结构，状态转移方程为：f(i+1)=max(prices[i+1]-minPrices(prices[i+1], minPrices(i)))
    经过一次遍历，可以计算出从第1个元素开始到右的最大利润结果数组leftProfit
    同样，i..n和i+1..n的数组最大利润，也具有最优子结构，可以计算出rightProfit
    遍历leftProfit[i]+rightProfit之和，得到的最大和即为结果
    时间复杂度：O(n)，需要遍历3次数组
    空间复杂度：O(n)，需要2个辅助数组
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0
        for i in range(1, n):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return sell2


s = Solution()
print(s.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
print(s.maxProfit([1, 2, 3, 4, 5]))
print(s.maxProfit([7, 6, 4, 3, 1]))
print(s.maxProfit([1]))
print(s.maxProfit([0, 1, 4, 2, 5, 2, 7]))
