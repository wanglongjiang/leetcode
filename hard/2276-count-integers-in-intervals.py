'''
2276. 统计区间中的整数数目
给你区间的 空 集，请你设计并实现满足要求的数据结构：

新增：添加一个区间到这个区间集合中。
统计：计算出现在 至少一个 区间中的整数个数。
实现 CountIntervals 类：

CountIntervals() 使用区间的空集初始化对象
void add(int left, int right) 添加区间 [left, right] 到区间集合之中。
int count() 返回出现在 至少一个 区间中的整数个数。
注意：区间 [left, right] 表示满足 left <= x <= right 的所有整数 x 。

 

示例 1：

输入
["CountIntervals", "add", "add", "count", "add", "count"]
[[], [2, 3], [7, 10], [], [5, 8], []]
输出
[null, null, null, 6, null, 8]

解释
CountIntervals countIntervals = new CountIntervals(); // 用一个区间空集初始化对象
countIntervals.add(2, 3);  // 将 [2, 3] 添加到区间集合中
countIntervals.add(7, 10); // 将 [7, 10] 添加到区间集合中
countIntervals.count();    // 返回 6
                           // 整数 2 和 3 出现在区间 [2, 3] 中
                           // 整数 7、8、9、10 出现在区间 [7, 10] 中
countIntervals.add(5, 8);  // 将 [5, 8] 添加到区间集合中
countIntervals.count();    // 返回 8
                           // 整数 2 和 3 出现在区间 [2, 3] 中
                           // 整数 5 和 6 出现在区间 [5, 8] 中
                           // 整数 7 和 8 出现在区间 [5, 8] 和区间 [7, 10] 中
                           // 整数 9 和 10 出现在区间 [7, 10] 中
 

提示：

1 <= left <= right <= 109
最多调用  add 和 count 方法 总计 105 次
调用 count 方法至少一次
'''
from sortedcontainers import SortedList
'''
思路：有序集合
这道题用线段树或有序集合都可以解决
这里用有序集合（红黑树）
设一个有序集合
当执行add，查询新区间覆盖的区间，将覆盖的这些全部删除，如果与左右邻居有重叠，将区间进行合并
count，返回所有区间的和，在执行上面add时候就计算好

时间复杂度：add为O(nlogn)，count为1
空间复杂度：O(n)
'''


class CountIntervals:
    def __init__(self):
        self.tree = SortedList()
        self.countnum = 0

    def add(self, left: int, right: int) -> None:
        leftIndex = self.tree.bisect_left((left, left))
        rightIndex = self.tree.bisect_right((right, right))
        oldWidth = 0
        for i in range(leftIndex, rightIndex):  # 遍历当前区间覆盖的所有区间，统计他们的范围
            r = self.tree[i]
            oldWidth += r[1] - r[0] + 1
            if r[1] > right:  # 该区间超过了当前区间的范围，需要扩展当前区间
                right = r[1]
        if rightIndex < len(self.tree):
            rightRange = self.tree[rightIndex]
            if rightRange[0] <= right:  # 右边的区间与当前区间有交集，扩展当前区间
                oldWidth += rightRange[1] - rightRange[0] + 1
                right = rightRange[1]
        self.countnum = self.countnum - oldWidth + right - left + 1  # 减掉去掉的区间，增加当前区间
        del self.tree[leftIndex:rightIndex]  # 删掉被覆盖的区间
        if leftIndex > 0:
            leftRange = self.tree[leftIndex - 1]
            if leftRange[1] >= left:  #左侧的区间与当前区间有交集
                if leftRange[1] >= right:  # 左侧的区间完全覆盖了当前区间，当前区间直接抛弃
                    self.countnum -= right - left + 1
                    return
                self.countnum -= leftRange[1] - left + 1  # 去掉重叠部分
                left = leftRange[0]
                del self.tree[leftIndex - 1]
        self.tree.add((left, right))

    def count(self) -> int:
        return self.countnum


s = CountIntervals()
s.add(5, 10)
s.add(3, 5)
print(s.count())

s = CountIntervals()
s.add(8, 43)
s.add(13, 16)
s.add(26, 33)
s.add(28, 36)
s.add(29, 37)
print(s.count())
