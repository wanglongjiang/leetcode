'''
H 指数
给定一位研究者论文被引用次数的数组（被引用次数是非负整数）。编写一个方法，计算出研究者的 h 指数。

h 指数的定义：h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）
总共有 h 篇论文分别被引用了至少 h 次。且其余的 N - h 篇论文每篇被引用次数 不超过 h 次。

例如：某人的 h 指数是 20，这表示他已发表的论文中，每篇被引用了至少 20 次的论文总共有 20 篇。
'''
from typing import List
'''
思路，记忆表。
1、开辟1个长度为n的数组counter，遍历输入数组将其累计在对应的区间。
2、从右向左遍历counter，直至sum([i+1,end])>=i
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        counter = [0] * n
        for num in citations:
            if num == 0:
                pass
            elif num > n:
                counter[n - 1] += 1
            else:
                counter[num - 1] += 1
        if counter[n - 1] >= n:
            return n
        for i in range(n - 2, -1, -1):
            counter[i] += counter[i + 1]
            if counter[i] >= i + 1:
                return i + 1
        return 0
