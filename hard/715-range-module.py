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
from sortedcontainers import SortedList
'''
思路：有序集合
设有序集合treeList
addRange，首先查询有没有重叠的区间，如果有进行合并。有可能不合并，合并合并左边、右边，或者合并2边。
queryRange，查询当前是否完全在某个区间范围内
removeRange，首先查询有没有重叠的区间，如果有进行裁剪。有可能不裁剪，裁剪左边、右边，或者裁剪2边。

TODO 还没写完

时间复杂度：3个函数平均都是O(logn)，最坏情况下是O(n)：当addRange和removeRange的范围特别大，覆盖很多区间时。
'''


class RangeModule:
    def __init__(self):
        self.treelist = SortedList(key=lambda r: r[0])

    def addRange(self, left: int, right: int) -> None:
        lefti = self.treelist.bisect_left([left, left])
        leftRange, rightRange = None, None
        added = False
        if lefti > 0:
            leftRange = self.treelist[lefti - 1]
            if leftRange[1] >= left:  # 左边区间与当前区间有重叠，2个区间进行合并
                leftRange[1] = max(right, leftRange[1])
                added = True
        righti = self.treelist.bisect_right([right, right])
        if righti - 1 > 0:
            rightRange = self.treelist[righti - 1]
            if rightRange[0] <= right <= rightRange[1]:
                rightRange[0] = min(rightRange[0], left)
                rightRange[1] = max(rightRange[1], right)
                added = True
        for i in range(lefti, righti - 1):  # 删除左右边界内的区间
            del self.treelist[lefti]
        if not added:
            self.treelist.add([left, right])

    def queryRange(self, left: int, right: int) -> bool:
        index = self.treelist.bisect_left([left, right])
        if index < len(self.treelist):
            leftRange = self.treelist[index]
            if leftRange[0] <= left and leftRange[1] >= right:
                return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        pass
