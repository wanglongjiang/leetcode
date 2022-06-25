'''
1475. 商品折扣后的最终价格
给你一个数组 prices ，其中 prices[i] 是商店里第 i 件商品的价格。

商店里正在进行促销活动，如果你要买第 i 件商品，那么你可以得到与 prices[j] 相等的折扣，
其中 j 是满足 j > i 且 prices[j] <= prices[i] 的 最小下标 ，如果没有满足条件的 j ，你将没有任何折扣。

请你返回一个数组，数组中第 i 个元素是折扣后你购买商品 i 最终需要支付的价格。

 

示例 1：

输入：prices = [8,4,6,2,3]
输出：[4,2,4,2,3]
解释：
商品 0 的价格为 price[0]=8 ，你将得到 prices[1]=4 的折扣，所以最终价格为 8 - 4 = 4 。
商品 1 的价格为 price[1]=4 ，你将得到 prices[3]=2 的折扣，所以最终价格为 4 - 2 = 2 。
商品 2 的价格为 price[2]=6 ，你将得到 prices[3]=2 的折扣，所以最终价格为 6 - 2 = 4 。
商品 3 和 4 都没有折扣。
示例 2：

输入：prices = [1,2,3,4,5]
输出：[1,2,3,4,5]
解释：在这个例子中，所有商品都没有折扣。
示例 3：

输入：prices = [10,1,1,6]
输出：[9,0,1,6]
 

提示：

1 <= prices.length <= 500
1 <= prices[i] <= 10^3
'''
from typing import List
'''
思路：单调栈
遇到这种需要延期决定的问题，第一反应是用单调栈。
设一个栈stk，用于保存prices的下标。
遍历prices，对于当前元素prices[i]，
如果栈顶元素j指向的值prices[j]比prices[i]小，其不能为i提供折扣。
否则prices[j]的折扣能够计算，计算其折扣，然后将其出栈。重复这个过程，直至所有大于prices[i]的栈顶全部出栈


时间复杂度：O(n)，每个元素最多入栈一次
空间复杂度：O(n)
'''


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stk, ans = [], prices.copy()
        for i in range(len(prices)):
            while stk and prices[stk[-1]] >= prices[i]:
                ans[stk[-1]] -= prices[i]
                stk.pop()
            stk.append(i)
        return ans


s = Solution()
print(s.finalPrices([8, 4, 6, 2, 3]))
