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
import bisect
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


class ExamRoom(object):
    def __init__(self, N):
        self.N = N
        self.students = []

    def seat(self):
        # Let's determine student, the position of the next
        # student to sit down.
        if not self.students:
            student = 0
        else:
            # Tenatively, dist is the distance to the closest student,
            # which is achieved by sitting in the position 'student'.
            # We start by considering the left-most seat.
            dist, student = self.students[0], 0
            for i, s in enumerate(self.students):
                if i:
                    prev = self.students[i - 1]
                    # For each pair of adjacent students in positions (prev, s),
                    # d is the distance to the closest student;
                    # achieved at position prev + d.
                    d = (s - prev) // 2
                    if d > dist:
                        dist, student = d, prev + d

            # Considering the right-most seat.
            d = self.N - 1 - self.students[-1]
            if d > dist:
                student = self.N - 1

        # Add the student to our sorted list of positions.
        bisect.insort(self.students, student)
        return student

    def leave(self, p):
        self.students.remove(p)


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
