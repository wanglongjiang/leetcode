'''
买卖股票的最佳时机
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

'''
from typing import List
'''
思路1，暴力搜索，对于每个元素，搜索其后面所有元素，找出差最大值
    时间复杂度：O(n^2)
    空间复杂度：O(1)
思路2，动态规划。
    遍历2次数组，第1次从后往前，对于每个元素prices[i]，将其从后往前遇到的最大值记录到辅助数组nums中
    第2次，从前往后，对于每个元素prices[i]，其与后面元素的最大差，可以与nums[i]相减得出
    时间复杂度：O(n)
    空间复杂度：O(n)
思路3，单调栈。
    从前往后遍历数据，遇到的元素与栈顶元素对比，如果大于栈顶元素，入栈；否则记下当前栈顶、栈底元素差，然后出栈直至小于栈顶元素，将当前元素入栈。
    时间复杂度：O(n)
    空间复杂度：O(n)，最坏情况下为O(n)，平均情况比上面的思路2好
思路4，数组一次遍历。上面的2、3想复杂了，可以找出当前最小价格，从左往右遍历的过程中更新最低价和最大价差。
    时间复杂度：O(n)
    空间复杂度：O(1)
'''


class Solution:
    # 思路4
    def maxProfit(self, prices: List[int]) -> int:
        profit, minPrice = 0, float('inf')
        for price in prices:
            if price < minPrice:
                minPrice = price
            else:
                profit = max(profit, price - minPrice)
        return profit

    # 思路3
    def maxProfit3(self, prices: List[int]) -> int:
        n = len(prices)
        stack = []
        ans = 0
        for i in range(n):
            if stack and stack[-1] > prices[i]:
                ans = max(ans, stack[-1] - stack[0])
                while stack and stack[-1] > prices[i]:
                    stack.pop()
            stack.append(prices[i])
        if stack:
            ans = max(ans, stack[-1] - stack[0])
        return ans

    # 思路2
    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)
        nums = [0] * n
        nums[n - 1] = prices[n - 1]
        for i in range(n - 2, -1, -1):
            nums[i] = max(prices[i], nums[i + 1])
        ans = 0
        for i in range(n):
            ans = max(ans, nums[i] - prices[i])
        return ans


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([7, 6, 4, 3, 1]))
