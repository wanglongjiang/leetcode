'''
731. 我的日程安排表 II
实现一个 MyCalendar 类来存放你的日程安排。如果要添加的时间内不会导致三重预订时，则可以存储这个新的日程安排。

MyCalendar 有一个 book(int start, int end)方法。它意味着在 start 到 end 时间内增加一个日程安排，
注意，这里的时间是半开区间，即 [start, end), 实数 x 的范围为，  start <= x < end。

当三个日程安排有一些时间上的交叉时（例如三个日程安排都在同一时间内），就会产生三重预订。

每次调用 MyCalendar.book方法时，如果可以将日程安排成功添加到日历中而不会导致三重预订，返回 true。否则，返回 false 并且不要将该日程安排添加到日历中。

请按照以下步骤调用MyCalendar 类: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

 

示例：

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(50, 60); // returns true
MyCalendar.book(10, 40); // returns true
MyCalendar.book(5, 15); // returns false
MyCalendar.book(5, 10); // returns true
MyCalendar.book(25, 55); // returns true
解释： 
前两个日程安排可以添加至日历中。 第三个日程安排会导致双重预订，但可以添加至日历中。
第四个日程安排活动（5,15）不能添加至日历中，因为它会导致三重预订。
第五个日程安排（5,10）可以添加至日历中，因为它未使用已经双重预订的时间10。
第六个日程安排（25,55）可以添加至日历中，因为时间 [25,40] 将和第三个日程安排双重预订；
时间 [40,50] 将单独预订，时间 [50,55）将和第二个日程安排双重预订。
 

提示：

每个测试用例，调用 MyCalendar.book 函数最多不超过 1000次。
调用函数 MyCalendar.book(start, end)时， start 和 end 的取值范围为 [0, 10^9]。
'''
'''
思路：线段树
利用线段树，假设我们开辟了数组 \textit{arr}[0,\cdots, 10^9]arr[0,⋯,10 
9
 ]，初始时每个元素的值都为 00，对于每次行程预定的区间 [\textit{start}, \textit{end})[start,end) ，则我们将区间中的元素 \textit{arr}[\textit{start},\cdots,\textit{end}-1]arr[start,⋯,end−1] 中的每个元素加 11，如果数组 arrarr 的最大元素大于 22 时，此时则出现某个区间被安排了 22 次上，此时返回 \texttt{false}false，同时将数组区间 \textit{arr}[\textit{start},\cdots,\textit{end}-1]arr[start,⋯,end−1] 进行减 11 即可恢复。实际我们不必实际开辟数组 \textit{arr}arr，可采用动态线段树，懒标记 \textit{lazy}lazy 标记区间 [l,r][l,r] 进行累加的次数，\textit{tree}tree 记录区间 [l,r][l,r] 的最大值，每次动态更新线段树即可。

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/my-calendar-ii/solution/wo-de-ri-cheng-an-pai-biao-ii-by-leetcod-wo6n/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

'''


class MyCalendarTwo:
    def __init__(self):
        self.tree = {}

    def update(self, start: int, end: int, val: int, l: int, r: int, idx: int) -> None:
        if r < start or end < l:
            return
        if start <= l and r <= end:
            p = self.tree.get(idx, [0, 0])
            p[0] += val
            p[1] += val
            self.tree[idx] = p
            return
        mid = (l + r) // 2
        self.update(start, end, val, l, mid, 2 * idx)
        self.update(start, end, val, mid + 1, r, 2 * idx + 1)
        p = self.tree.get(idx, [0, 0])
        p[0] = p[1] + max(self.tree.get(2 * idx, (0, ))[0], self.tree.get(2 * idx + 1, (0, ))[0])
        self.tree[idx] = p

    def book(self, start: int, end: int) -> bool:
        self.update(start, end - 1, 1, 0, 10**9, 1)
        if self.tree[1][0] > 2:
            self.update(start, end - 1, -1, 0, 10**9, 1)
            return False
        return True
