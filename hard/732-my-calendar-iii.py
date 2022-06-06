'''
732. 我的日程安排表 III
当 k 个日程安排有一些时间上的交叉时（例如 k 个日程安排都在同一时间内），就会产生 k 次预订。

给你一些日程安排 [start, end) ，请你在每个日程安排添加后，返回一个整数 k ，表示所有先前日程安排会产生的最大 k 次预订。

实现一个 MyCalendarThree 类来存放你的日程安排，你可以一直添加新的日程安排。

MyCalendarThree() 初始化对象。
int book(int start, int end) 返回一个整数 k ，表示日历中存在的 k 次预订的最大值。


示例：

输入：
["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
输出：
[null, 1, 1, 2, 3, 3, 3]

解释：
MyCalendarThree myCalendarThree = new MyCalendarThree();
myCalendarThree.book(10, 20); // 返回 1 ，第一个日程安排可以预订并且不存在相交，所以最大 k 次预订是 1 次预订。
myCalendarThree.book(50, 60); // 返回 1 ，第二个日程安排可以预订并且不存在相交，所以最大 k 次预订是 1 次预订。
myCalendarThree.book(10, 40); // 返回 2 ，第三个日程安排 [10, 40) 与第一个日程安排相交，所以最大 k 次预订是 2 次预订。
myCalendarThree.book(5, 15); // 返回 3 ，剩下的日程安排的最大 k 次预订是 3 次预订。
myCalendarThree.book(5, 10); // 返回 3
myCalendarThree.book(25, 55); // 返回 3


提示：

0 <= start < end <= 10^9
每个测试用例，调用 book 函数最多不超过 400次
'''
'''
思路：线段树
利用线段树，假设我们开辟了数组 \textit{arr}[0,\cdots, 10^9]arr[0,⋯,10 
9
 ]，初始时每个元素的值都为 00，对于每次行程预定的区间 [\textit{start}, \textit{end})[start,end) ，则我们将区间中的元素 \textit{arr}[\textit{start},\cdots,\textit{end}-1]arr[start,⋯,end−1] 中的每个元素加 11，最终只需要求出数组 arrarr 的最大元素即可。实际我们不必实际开辟数组 \textit{arr}arr，可采用动态线段树，懒标记 \textit{lazy}lazy 标记区间 [l,r][l,r] 进行累加的次数，\textit{tree}tree 记录区间 [l,r][l,r] 的最大值，最终返回区间 [0,10^9][0,10 
9
 ] 中的最大元素即可。

时间复杂度：O(n \log C)O(nlogC)，其中 nn 为日程安排的数量。由于使用了线段树查询，线段树的最大深度为 \log ClogC, 每次最多会查询 \log ClogC 个节点，每次求最大的预定需的时间复杂度为 O(\log C + \log C)O(logC+logC)，因此时间复杂度为 O(n \log C)O(nlogC)，在此 CC 取固定值即为 10^910 
9
 。

空间复杂度：O(n \log C)O(nlogC)，其中 nn 为日程安排的数量。由于该解法采用的为动态线段树，线段树的最大深度为 \log ClogC，每次预定最多会在线段树上增加 \log ClogC 个节点，因此空间复杂度为 O(n \log C)O(nlogC)，在此 CC 取固定值即为 10^910 
9
 。

'''

from collections import defaultdict


class MyCalendarThree:
    def __init__(self):
        self.tree = defaultdict(int)
        self.lazy = defaultdict(int)

    def update(self, start: int, end: int, l: int, r: int, idx: int):
        if r < start or end < l:
            return
        if start <= l and r <= end:
            self.tree[idx] += 1
            self.lazy[idx] += 1
        else:
            mid = (l + r) // 2
            self.update(start, end, l, mid, idx * 2)
            self.update(start, end, mid + 1, r, idx * 2 + 1)
            self.tree[idx] = self.lazy[idx] + max(self.tree[idx * 2], self.tree[idx * 2 + 1])

    def book(self, start: int, end: int) -> int:
        self.update(start, end - 1, 0, 10**9, 1)
        return self.tree[1]
