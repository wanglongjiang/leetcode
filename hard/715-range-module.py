'''
Range 模块
Range 模块是跟踪数字范围的模块。你的任务是以一种有效的方式设计和实现以下接口。

addRange(int left, int right) 添加半开区间 [left, right)，跟踪该区间中的每个实数。添加与当前跟踪的数字部分重叠的区间时，
应当添加在区间 [left, right) 中尚未跟踪的任何数字到该区间中。
queryRange(int left, int right) 只有在当前正在跟踪区间 [left, right) 中的每一个实数时，才返回 true。
removeRange(int left, int right) 停止跟踪区间 [left, right) 中当前正在跟踪的每个实数。
 

示例：

addRange(10, 20): null
removeRange(14, 16): null
queryRange(10, 14): true （区间 [10, 14) 中的每个数都正在被跟踪）
queryRange(13, 15): false （未跟踪区间 [13, 15) 中像 14, 14.03, 14.17 这样的数字）
queryRange(16, 17): true （尽管执行了删除操作，区间 [16, 17) 中的数字 16 仍然会被跟踪）
 

提示：

半开区间 [left, right) 表示所有满足 left <= x < right 的实数。
对 addRange, queryRange, removeRange 的所有调用中 0 < left < right < 10^9。
在单个测试用例中，对 addRange 的调用总数不超过 1000 次。
在单个测试用例中，对  queryRange 的调用总数不超过 5000 次。
在单个测试用例中，对 removeRange 的调用总数不超过 1000 次。
'''
from sortedcontainers import SortedDict
'''
思路：有序集合
设有序集合treeList
addRange，首先查询有没有重叠的区间，如果有进行合并。有可能不合并，合并合并左边、右边，或者合并2边。
queryRange，查询当前是否完全在某个区间范围内
removeRange，首先查询有没有重叠的区间，如果有进行裁剪。有可能不裁剪，裁剪左边、右边，或者裁剪2边。


时间复杂度：3个函数平均都是O(logn)，最坏情况下是O(n)：当addRange和removeRange的范围特别大，覆盖很多区间时。
'''


class RangeModule:
    def __init__(self):
        self.intervals = SortedDict()

    def addRange(self, left: int, right: int) -> None:
        itvs_ = self.intervals

        x = itvs_.bisect_right(left)
        if x != 0:
            start = x - 1
            if itvs_.values()[start] >= right:
                return
            if itvs_.values()[start] >= left:
                left = itvs_.keys()[start]
                itvs_.popitem(start)
                x -= 1

        while x < len(itvs_) and itvs_.keys()[x] <= right:
            right = max(right, itvs_.values()[x])
            itvs_.popitem(x)

        itvs_[left] = right

    def queryRange(self, left: int, right: int) -> bool:
        itvs_ = self.intervals

        x = itvs_.bisect_right(left)
        if x == 0:
            return False

        return right <= itvs_.values()[x - 1]

    def removeRange(self, left: int, right: int) -> None:
        itvs_ = self.intervals

        x = itvs_.bisect_right(left)
        if x != 0:
            start = x - 1
            if (ri := itvs_.values()[start]) >= right:
                if (li := itvs_.keys()[start]) == left:
                    itvs_.popitem(start)
                else:
                    itvs_[li] = left
                if right != ri:
                    itvs_[right] = ri
                return
            elif ri > left:
                itvs_[itvs_.keys()[start]] = left

        while x < len(itvs_) and itvs_.keys()[x] < right:
            if itvs_.values()[x] <= right:
                itvs_.popitem(x)
            else:
                itvs_[right] = itvs_.values()[x]
                itvs_.popitem(x)
                break
