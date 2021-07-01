'''
面试题 17.20. 连续中值
随机产生数字并传递给一个方法。你能否完成这个方法，在每次产生新值时，寻找当前所有值的中间值（中位数）并保存。

中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例：

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2
'''
import heapq
'''
思路：对顶堆
用2个堆：lo保存低位的数，用最大堆
hi保存高位的数，用最小堆
1. 添加数据num时，
> 如果num>hi[0]，则需要将其加入hi
> 否则需要将其加入lo
执行上述添加动作，需要对比2个堆的大小，
如果hi.length-lo.length<0，则需要将lo的最大值转移到hi里面
如果hi.length-lo.length>1，则需要将hi的最小值转移到lo里面

2. 查找中位数时，如果2个堆大小相同，则取2个堆的第0个元素的平均值，否则取hi的第0个元素


时间复杂度：所有操作都是O(logn)
'''


class MedianFinder:
    def __init__(self):
        self.lo = []  # 数据流的低位一半数据，使用最大堆
        self.hi = []  # 数据流的高位一半数据，使用最小堆

    def addNum(self, num: int) -> None:
        if not self.hi or self.hi[0] < num:
            heapq.heappush(self.hi, num)
        else:
            heapq.heappush(self.lo, -num)
        if len(self.lo) > len(self.hi):
            t = heapq.heappop(self.lo)
            heapq.heappush(self.hi, -t)
        if len(self.hi) - len(self.lo) > 1:
            t = heapq.heappop(self.hi)
            heapq.heappush(self.lo, -t)

    def findMedian(self) -> float:
        if len(self.hi) > len(self.lo):
            return self.hi[0]
        return (self.hi[0] - self.lo[0]) / 2
