'''
积压订单中的订单总数

给你一个二维整数数组 orders ，其中每个 orders[i] = [pricei, amounti, orderTypei] 表示有 amounti 笔类型为 orderTypei 、
价格为 pricei 的订单。

订单类型 orderTypei 可以分为两种：

0 表示这是一批采购订单 buy
1 表示这是一批销售订单 sell
注意，orders[i] 表示一批共计 amounti 笔的独立订单，这些订单的价格和类型相同。对于所有有效的 i ，
由 orders[i] 表示的所有订单提交时间均早于 orders[i+1] 表示的所有订单。

存在由未执行订单组成的 积压订单 。积压订单最初是空的。提交订单时，会发生以下情况：

如果该订单是一笔采购订单 buy ，则可以查看积压订单中价格 最低 的销售订单 sell 。
如果该销售订单 sell 的价格 低于或等于 当前采购订单 buy 的价格，则匹配并执行这两笔订单，
并将销售订单 sell 从积压订单中删除。否则，采购订单 buy 将会添加到积压订单中。
反之亦然，如果该订单是一笔销售订单 sell ，则可以查看积压订单中价格 最高 的采购订单 buy 。
如果该采购订单 buy 的价格 高于或等于 当前销售订单 sell 的价格，则匹配并执行这两笔订单，并将采购订单 buy 从积压订单中删除。
否则，销售订单 sell 将会添加到积压订单中。
输入所有订单后，返回积压订单中的 订单总数 。由于数字可能很大，所以需要返回对 109 + 7 取余的结果。

1 <= orders.length <= 10^5
orders[i].length == 3
1 <= pricei, amounti <= 10^9
orderTypei 为 0 或 1
'''
from typing import List
'''
思路1、堆。构造采购订单的最大堆，销售订单的最小堆。
    遍历订单list
    1、遇到采购订单，先在销售订单堆里面查找，如果最小堆里没有满足需求的订单，将采购订单加入最大堆。
    2、遇到销售订单，先在采购订单堆里面查找，如果最大堆里没有满足需求的订单，将销售订单加入最小堆。
时间复杂度：最坏情况下O(nlogn)，这种情况下所有订单都入堆。10^6。
空间复杂度：最坏情况下O(n)
'''


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        pass
