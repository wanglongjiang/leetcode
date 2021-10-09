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
当执行addNum时，用[val,val]搜索在有序集合中的索引i，如果当前区间[val,val]与左右两边的区间，也就是i和i-1处的区间可以合并，则需要将其合并。
如果不能合并，将区间[val,val]保存到有序集合中。

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
            elif right[0] <= val and right[1] >= val:  # 在右边区间范围内，不需要添加新的区间，将已添加标识设置为True
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


'''
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
'''
s = SummaryRanges()
s.addNum(49)
print(s.getIntervals())
s.addNum(97)
print(s.getIntervals())
s.addNum(53)
print(s.getIntervals())
s.addNum(5)
print(s.getIntervals())
s.addNum(33)
print(s.getIntervals())
s.addNum(65)
print(s.getIntervals())
s.addNum(62)
print(s.getIntervals())
s.addNum(51)
print(s.getIntervals())
s.addNum(100)
print(s.getIntervals())
s.addNum(38)
print(s.getIntervals())
s.addNum(61)
print(s.getIntervals())
s.addNum(45)
print(s.getIntervals())
s.addNum(74)
print(s.getIntervals())
s.addNum(27)
print(s.getIntervals())
s.addNum(64)
print(s.getIntervals())
s.addNum(17)
print(s.getIntervals())
s.addNum(36)
print(s.getIntervals())
s.addNum(17)
print(s.getIntervals())
s.addNum(96)
print(s.getIntervals())
s.addNum(12)
print(s.getIntervals())
s.addNum(79)
print(s.getIntervals())
s.addNum(32)
print(s.getIntervals())
s.addNum(68)
print(s.getIntervals())
s.addNum(90)
print(s.getIntervals())
s.addNum(77)
print(s.getIntervals())
s.addNum(18)
print(s.getIntervals())
s.addNum(39)
print(s.getIntervals())
s.addNum(12)
print(s.getIntervals())
s.addNum(93)
print(s.getIntervals())
s.addNum(9)
print(s.getIntervals())
s.addNum(87)
print(s.getIntervals())
s.addNum(42)
print(s.getIntervals())
s.addNum(60)
print(s.getIntervals())
s.addNum(71)
print(s.getIntervals())
s.addNum(12)
print(s.getIntervals())
s.addNum(45)
print(s.getIntervals())
s.addNum(55)
print(s.getIntervals())
s.addNum(40)
print(s.getIntervals())
s.addNum(78)
print(s.getIntervals())
s.addNum(81)
print(s.getIntervals())
s.addNum(26)
print(s.getIntervals())
s.addNum(70)
print(s.getIntervals())
s.addNum(61)
print(s.getIntervals())
s.addNum(56)
print(s.getIntervals())
s.addNum(66)
print(s.getIntervals())
s.addNum(33)
print(s.getIntervals())
s.addNum(7)
print(s.getIntervals())
s.addNum(70)
print(s.getIntervals())
s.addNum(1)
print(s.getIntervals())
s.addNum(11)
print(s.getIntervals())
s.addNum(92)
print(s.getIntervals())
s.addNum(51)
print(s.getIntervals())
s.addNum(90)
print(s.getIntervals())
s.addNum(100)
print(s.getIntervals())
s.addNum(85)
print(s.getIntervals())
s.addNum(80)
print(s.getIntervals())
s.addNum(0)
print(s.getIntervals())
s.addNum(78)
print(s.getIntervals())
s.addNum(63)
print(s.getIntervals())
s.addNum(42)
print(s.getIntervals())
s.addNum(31)
print(s.getIntervals())
s.addNum(93)
print(s.getIntervals())
s.addNum(41)
print(s.getIntervals())
s.addNum(90)
print(s.getIntervals())
s.addNum(8)
print(s.getIntervals())
s.addNum(24)
print(s.getIntervals())
s.addNum(72)
print(s.getIntervals())
s.addNum(28)
print(s.getIntervals())
s.addNum(30)
print(s.getIntervals())
s.addNum(18)
print(s.getIntervals())
s.addNum(69)
print(s.getIntervals())
s.addNum(57)
print(s.getIntervals())
s.addNum(11)
print(s.getIntervals())
s.addNum(10)
print(s.getIntervals())
s.addNum(40)
print(s.getIntervals())
s.addNum(65)
print(s.getIntervals())
s.addNum(62)
print(s.getIntervals())
s.addNum(13)
print(s.getIntervals())
s.addNum(38)
print(s.getIntervals())
s.addNum(70)
print(s.getIntervals())
s.addNum(37)
print(s.getIntervals())
s.addNum(90)
print(s.getIntervals())
s.addNum(15)
print(s.getIntervals())
s.addNum(70)
print(s.getIntervals())
s.addNum(42)
print(s.getIntervals())
s.addNum(69)
print(s.getIntervals())
s.addNum(26)
print(s.getIntervals())
s.addNum(77)
print(s.getIntervals())
s.addNum(70)
print(s.getIntervals())
s.addNum(75)
print(s.getIntervals())
s.addNum(36)
print(s.getIntervals())
s.addNum(56)
print(s.getIntervals())
s.addNum(11)
print(s.getIntervals())
s.addNum(76)
print(s.getIntervals())
s.addNum(49)
print(s.getIntervals())
s.addNum(40)
print(s.getIntervals())
s.addNum(73)
print(s.getIntervals())
s.addNum(30)
print(s.getIntervals())
s.addNum(37)
print(s.getIntervals())
s.addNum(23)
print(s.getIntervals())
