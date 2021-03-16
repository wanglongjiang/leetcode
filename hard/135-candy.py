'''
分发糖果
老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。

你需要按照以下要求，帮助老师给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
评分更高的孩子必须比他两侧的邻位孩子获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？
'''
from typing import List
'''
思路：单调栈。
如果第i个孩子得分比后面的i+1孩子得分低，第i个孩子得多少糖只与i-1相关。
    如果得分与i+1个孩子相同，第i个孩子得多少糖只与i-1相关。
    如果得分比i+1个孩子高，不能确定第i个孩子能拿到多少糖，只能暂时保存起来。
经过上面的分析，可以采用单调栈的算法。
默认最低糖果数是1，从第0个孩子开始遍历。
    1、如果第i个孩子比i+1个孩子得分高，第i个孩子糖果数入栈，下一个孩子的默认糖果数改为1
    2、如果第i个孩子比i+1个孩子得分低，给他糖果数，下一个孩子的糖果数+1
    3、如果第i个孩子比i+1个孩子得分相同，给他糖果数，下一个孩子的默认糖果数变成1.
        如果上面2、3种情况下，栈中不为空，可以确定栈中的孩子糖果数，栈顶元素为当前孩子糖果数+1，栈顶第2个为当前孩子糖果数+2，
        例外的是栈底的孩子，他要取max(自身入栈的糖果数，第i个孩子倒推的糖果数)
时间复杂度：O(n)，每个孩子迭代一次，每个孩子最多入栈出栈1次
空间复杂度：O(n)，最坏情况下n-1个孩子入栈
'''


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n < 2:
            return n
        total, candyNum = 0, 1
        stack = []
        for i in range(n - 1):
            if ratings[i] > ratings[i + 1]:  # 第i个孩子糖果数入栈，下一个孩子的默认糖果数改为1
                stack.append(candyNum)
                candyNum = 1
                continue
            if ratings[i] == ratings[i + 1]:  # 得分相同，给他糖果，下一个孩子的默认糖果数变成1.
                total += candyNum
                candyNum = 1
            else:  # 下个孩子得分高，给他糖果，下一个孩子的默认糖果数+1
                total += candyNum
                candyNum += 1
            if len(stack) > 0:  # 有入栈的孩子，最低从2个开始，依次升高
                num = 2
                while len(stack) > 1:
                    total += num
                    num += 1
                    stack.pop()
                total += max(stack.pop(), num)
        total += candyNum  # 加上最后1个孩子应得得糖果
        if len(stack) > 0:  # 有入栈的孩子，最低从2个开始，依次升高
            num = 2
            while len(stack) > 1:
                total += num
                num += 1
                stack.pop()
            total += max(stack.pop(), num)
        return total


s = Solution()
print(s.candy([1, 0, 2]))
print(s.candy([1, 2, 2]))
print(s.candy([]))
print(s.candy([100]))
print(s.candy([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(s.candy([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(s.candy([8, 8, 8, 8]))
