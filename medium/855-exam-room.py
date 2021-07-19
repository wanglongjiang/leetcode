'''
考场就座
在考场里，一排有 N 个座位，分别编号为 0, 1, 2, ..., N-1 。

当学生进入考场后，他必须坐在能够使他与离他最近的人之间的距离达到最大化的座位上。如果有多个这样的座位，
他会坐在编号最小的座位上。(另外，如果考场里没有人，那么学生就坐在 0 号座位上。)

返回 ExamRoom(int N) 类，它有两个公开的函数：其中，函数 ExamRoom.seat() 会返回一个 int （整型数据），
代表学生坐的位置；函数 ExamRoom.leave(int p) 代表坐在座位 p 上的学生现在离开了考场。
每次调用 ExamRoom.leave(p) 时都保证有学生坐在座位 p 上。

 

示例：

输入：["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
输出：[null,0,9,4,2,null,5]
解释：
ExamRoom(10) -> null
seat() -> 0，没有人在考场里，那么学生坐在 0 号座位上。
seat() -> 9，学生最后坐在 9 号座位上。
seat() -> 4，学生最后坐在 4 号座位上。
seat() -> 2，学生最后坐在 2 号座位上。
leave(4) -> null
seat() -> 5，学生最后坐在 5 号座位上。
 

提示：

1 <= N <= 10^9
在所有的测试样例中 ExamRoom.seat() 和 ExamRoom.leave() 最多被调用 10^4 次。
保证在调用 ExamRoom.leave(p) 时有学生正坐在座位 p 上。
'''
from sortedcontainers import SortedList
'''
思路：有序集合
将2个有人的座位之间的空座视为一个区间，将所有区间放入treemap排序
1. 初始化
> 将区间[0,n-1]加入treemap
> 时间复杂度：O(1)
2. seat函数
> 从treemap中找到最大的区间(start,end)，将其从treemap中删除，设p=(end-start+1)//2 然后将(start, p-1), (p+1,end)加入treemap
> 特殊处理：如果start=0，则只插入(1,end)；如果end=n-1,则只插入(start,n-1)
> 时间复杂度：O(logn)
3. leave函数：
> 根据p定位其相邻的区间，如果2个区间能合并，将2个区间进行合并
> 时间复杂度：O(logn)
'''


class ExamRoom:
    def __init__(self, n: int):
        self.treemap1 = SortedList()  # 每个元素为(区间大小，start,end)，因为区间大小为偶数时与减少一时相同，所以要减少1
        self.treemap2 = SortedList()  # 每个元素为(start,end)，主要目的是在leave时，定位p所在的区间
        self.n = n
        self.treemap1.add((self.distance(0, n - 1), 0, n - 1))
        self.treemap2.add((0, n - 1))

    def distance(self, start, end):
        d = end - start + 1
        if d % 2 == 0:
            d -= 1
        return d

    def seat(self) -> int:
        r = self.treemap1.pop()  # 弹出最大的区间
        size, start, end = r
        start = -start
        self.treemap2.remove((start, end))
        if start == 0:  # 左边界
            p = 0
            if end >= 1:
                rr = (self.distance(1, end), -1, end)
                self.treemap1.add(rr)
                self.treemap2.add((1, end))
        elif end == self.n - 1:  # 右边界
            p = self.n - 1
            if p - 1 >= start:
                lr = (self.distance(start, p - 1), -start, p - 1)
                self.treemap1.add(lr)
                self.treemap2.add((start, p - 1))
        else:  # 选中了中间的区间，区间可以拆分成2个
            p = (start + end) // 2
            if p > start:
                lr = (self.distance(start, p - 1), -start, p - 1)
                self.treemap1.add(lr)
                self.treemap2.add((start, p - 1))
            if p < end:
                rr = (self.distance(p + 1, end), -(p + 1), end)
                self.treemap1.add(rr)
                self.treemap2.add((p + 1, end))
        return p

    def leave(self, p: int) -> None:
        midRange = (p, p)
        idx = self.treemap2.bisect_left(midRange)
        if idx > 0:
            leftRange = self.treemap2[idx - 1]
            if leftRange[1] == p - 1:  # 左侧区间与p相邻，进行合并
                self.treemap2.remove(leftRange)
                self.treemap1.remove((self.distance(leftRange[0], leftRange[1]), -leftRange[0], leftRange[1]))
                midRange = (leftRange[0], p)
                idx -= 1
        if idx < len(self.treemap2):
            rightRange = self.treemap2[idx]
            if rightRange[0] == p + 1:  # 右侧区间与p相邻，进行合并
                self.treemap2.remove(rightRange)
                self.treemap1.remove((self.distance(rightRange[0], rightRange[1]), -rightRange[0], rightRange[1]))
                midRange = (midRange[0], rightRange[1])
        self.treemap2.add(midRange)
        self.treemap1.add((self.distance(midRange[0], midRange[1]), -midRange[0], midRange[1]))


s = ExamRoom(10)
print(s.seat())
print(s.seat())
print(s.seat())
print(s.seat())
s.leave(4)
print(s.seat())
'''
输出：[null,0,7,3,null,null,0,7,5,1,2,4,6]
预期：[null,0,7,3,null,null,7,0,5,1,2,4,6]
'''
