'''
将数据流变为多个不相交区间
给定一个非负整数的数据流输入 a1，a2，…，an，…，将到目前为止看到的数字总结为不相交的区间列表。

例如，假设数据流中的整数为 1，3，7，2，6，…，每次的总结为：

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]
 

进阶：
如果有很多合并，并且与数据流的大小相比，不相交区间的数量很小，该怎么办?
'''
from typing import List
from sortedcontainers import SortedList
'''
思路：有序集合
使用有序集合存储区间。
当执行addNum时，用[val,val]搜索在左右集合中的索引i，如果i和i-1处的区间可以合并，则需要将其合并。

时间复杂度：addNum时间为O(logn)，getIntervals为O(n)
'''


class SummaryRanges:
    def __init__(self):
        self.li = SortedList(key=lambda r: r[0])

    def addNum(self, val: int) -> None:
        i = self.li.bisect_left([val, val])
        left, right = None, None
        added = False
        if i < len(self.li):
            right = self.li[i]
            if right[0] == val + 1:  # 与右区间相邻，进行扩展
                right[0] = val
                added = True
            elif right[0] == val:  # 在右边区间范围内，不需要添加新的区间，将已添加标识设置为True
                added = True
        if i > 0:
            left = self.li[i - 1]
            if left[1] == val - 1:  # 与左区间相邻，进行扩展
                left[1] = val
                added = True
            elif left[1] >= val:  # 在左边区间范围内，不需要添加新的区间，将已添加标识设置为True
                added = True
        if not added:  # 与2边的区间都不相邻或相交，添加一个独立的区间
            self.li.add([val, val])
        elif left and right:
            if left[1] == right[0]:
                left[1] = right[1]  # 扩展left的大小
                del self.li[i]  # 删除right

    def getIntervals(self) -> List[List[int]]:
        return list(self.li)


s = SummaryRanges()
s.addNum(1)
print(s.getIntervals())
s.addNum(3)
print(s.getIntervals())
s.addNum(7)
print(s.getIntervals())
s.addNum(2)
print(s.getIntervals())
s.addNum(6)
print(s.getIntervals())
