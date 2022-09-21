'''
2412. 完成所有交易的初始最少钱数
给你一个下标从 0 开始的二维整数数组 transactions，其中transactions[i] = [costi, cashbacki] 。

数组描述了若干笔交易。其中每笔交易必须以 某种顺序 恰好完成一次。在任意一个时刻，你有一定数目的钱 money ，为了完成交易 i ，money >= costi 这个条件必须为真。
执行交易后，你的钱数 money 变成 money - costi + cashbacki 。

请你返回 任意一种 交易顺序下，你都能完成所有交易的最少钱数 money 是多少。

 

示例 1：

输入：transactions = [[2,1],[5,0],[4,2]]
输出：10
解释：
刚开始 money = 10 ，交易可以以任意顺序进行。
可以证明如果 money < 10 ，那么某些交易无法进行。
示例 2：

输入：transactions = [[3,0],[0,3]]
输出：3
解释：
- 如果交易执行的顺序是 [[3,0],[0,3]] ，完成所有交易需要的最少钱数是 3 。
- 如果交易执行的顺序是 [[0,3],[3,0]] ，完成所有交易需要的最少钱数是 0 。
所以，刚开始钱数为 3 ，任意顺序下交易都可以全部完成。
 

提示：

1 <= transactions.length <= 105
transactions[i].length == 2
0 <= costi, cashbacki <= 109
'''

from typing import List
'''
思路：贪心
数组分为正收益（收益大于成本）和负收益（收益小于成本）的。
要使交易钱数最大化，首先考虑负收益：如何确保任意顺序下所有负收益都能完成？
如果想要达成某一次交易，设初始钱数为x，那么x>=callback+所有亏损，遍历这一过程，找到最大的callback即可。

处理完负收益，再考虑正收益，如果要完成所有正收益的，只需要找到正收益的交易中cost最大的即可，将其与经过负收益处理过的最小值进行对比，选取较大的即可。

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        maxIncomeCost, maxCallback, sumPay = 0, 0, 0  # 3个变量分别记录盈利项目中最大的成本、亏损项目中最大的callback、合计亏损的钱数
        for trans in transactions:
            if trans[0] <= trans[1]:  # 正收益
                maxIncomeCost = max(maxIncomeCost, trans[0])  # 找到正收益的交易里面成本最高的
            else:  # 负收益
                sumPay += trans[0] - trans[1]  # 累计亏损
                maxCallback = max(maxCallback, trans[1])  # 最大的遗留钱数
        return max(maxCallback, maxIncomeCost) + sumPay


s = Solution()
print(s.minimumMoney([[2, 1], [5, 0], [4, 2]]))
print(s.minimumMoney([[3, 0], [0, 3]]))
