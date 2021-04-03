'''
股票价格跨度
编写一个 StockSpanner 类，它收集某些股票的每日报价，并返回该股票当日价格的跨度。

今天股票价格的跨度被定义为股票价格小于或等于今天价格的最大连续日数（从今天开始往回数，包括今天）。

例如，如果未来7天股票的价格是 [100, 80, 60, 70, 60, 75, 85]，那么股票跨度将是 [1, 1, 1, 2, 1, 4, 6]。

提示：

调用 StockSpanner.next(int price) 时，将有 1 <= price <= 10^5。
每个测试用例最多可以调用  10000 次 StockSpanner.next。
在所有测试用例中，最多调用 150000 次 StockSpanner.next。
此问题的总时间限制减少了 50%。
'''
'''
思路1：如果每次都向前查找，遇到最坏情况（递增序列），每次next都会扫描整个数组，时间复杂度O(n^2)
可以将每次next结果记录下来，如果是递增序列，只向前搜索一步即可跨过整个递增序列，
最坏的一个情况是开始是递减序列，后来出现一个大于之前所有值的元素，会向前搜索所有元素，但只会搜索这一次，时间复杂度接近O(n)
思路2：单调栈。
栈中存放递减序列对(price,w)
时间复杂度：O(n)
'''


class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        w = 1
        while self.stack and price >= self.stack[-1][0]:
            p = self.stack.pop()
            w += p[1]
        self.stack.append((price, w))
        return w


class StockSpanner1:
    def __init__(self):
        self.stocks = [float('inf')]  # 设置1个哨兵，简化计算
        self.nexts = [1]

    def next(self, price: int) -> int:
        i = len(self.stocks) - 1
        curnext = 1
        while price >= self.stocks[i]:  # 向前搜索直至遇到大于当前价格
            curnext += self.nexts[i]
            i -= self.nexts[i]  # 跳过所有小于当前价格的区间
        self.nexts.append(curnext)
        self.stocks.append(price)
        return curnext
