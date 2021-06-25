'''
剑指 Offer 41. 数据流中的中位数

如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例 1：

输入：
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
输出：[null,null,null,1.50000,null,2.00000]
示例 2：

输入：
["MedianFinder","addNum","findMedian","addNum","findMedian"]
[[],[2],[],[3],[]]
输出：[null,null,2.00000,null,2.50000]
 

限制：

最多会对 addNum、findMedian 进行 50000 次调用。
注意：本题与主站 295 题相同：https://leetcode-cn.com/problems/find-median-from-data-stream/
'''
'''
思路，链表
主要的想法就是0-100的元素直接存入1个大小为101的数组中，其他数字以链表的形式保存。
其他数字也可以用跳表进行优化，太复杂了，懒得写。
每个数字一个节点，每个节点里维护着这个数字出现次数，如果mid指针指向这个节点，节点内需要维护一个索引，指向mid指向的数字偏移量。
如果数据流中 99% 的整数都在 0 到 100 范围内，维护几个关键变量：
>    count   存放所有元素数量
>    nums    存放0-100元素的指针，100之后的元素因为较少，直接搜索链表进行插入
>    head    存放双向链表的表头，表尾
>    mid     存放中位数指针，如果count是偶数，mid存放left元素指针

当插入一条数据时，如果是0-100范围内，直接保存，如果是范围外的，需要顺序查找、创建/修改链表节点。
同时根据插入数据的大小，左右移动mid指针。

addNum()时间复杂度：如果是0-100的数据，时间复杂度为O(1)，如果是其他数据，时间复杂度为O(n)，如果链表改成跳表，能优化到O(logn)
findMedian()时间复杂度：O(1)
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.index = 0
        self.count = 1
        self.prev = None
        self.next = None


class MedianFinder:
    def __init__(self):
        self.nums = [None] * 101
        self.count = 0
        self.head = Node(float('-inf'))
        self.tail = Node(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head
        self.mid = None

    def addNum(self, num: int) -> None:
        if num >= 0 and num <= 100:
            if self.nums[num]:  # 节点存在，直接修改数量
                self.nums[num].count += 1
            else:  # 节点不存在，需要创建，并插入合适的位置
                node = Node(num)
                self.nums[num] = node
                if not self.mid:  # 链表为空，直接插入
                    self.head.next = node
                    self.tail.prev = node
                    node.prev = self.head
                    node.next = self.tail
                else:
                    if self.mid.val > num:  # 新节点的值大于中位数，插入中位数之前的某个位置
                        old = self.mid
                        while old.val > num:
                            old = old.prev
                        node.next = old.next
                        node.prev = old
                        old.next = node
                        node.next.prev = node
                    else:  # 新节点的值小于中位数，插入中位数之后的某个位置
                        old = self.mid
                        while old.val < num:
                            old = old.next
                        node.prev = old.prev
                        node.next = old
                        old.prev = node
                        node.prev.next = node
        else:  # 数值大于100，插入100之后的链表中
            old = self.tail
            while old.val > num:
                old = old.prev
            if old.val == num:  # 节点存在，直接修改数量
                old.count += 1
            else:  # 节点不存在，需要创建，并插入合适的位置
                node = Node(num)
                node.prev = old
                node.next = old.next
                old.next = node
                node.next.prev = node
        if not self.mid:
            self.mid = self.head.next
        else:  # 插入节点后，中位数发生变化，可能需要调整mid指针
            if self.count & 1:  # count原先是奇数，mid指向中间元素，如果num>=mid，不需要调整指针；如果num<mid，需要向左指针
                if num < self.mid.val:
                    if self.mid.index > 0:
                        self.mid.index -= 1
                    else:
                        self.mid = self.mid.prev
                        self.mid.index = self.mid.count - 1
            else:  # count原先是偶数，mid指向中间偏左元素上。如果num>=mid，需要向右调整指针；如果num<mid，不需要调整指针
                if num >= self.mid.val:
                    if self.mid.index + 1 < self.mid.count:
                        self.mid.index += 1
                    else:
                        self.mid = self.mid.next
                        self.mid.index = 0
        self.count += 1

    def findMedian(self) -> float:
        if self.count & 1:  # 奇数个元素，中位是正中间的数
            return self.mid.val
        else:
            if self.mid.index + 1 < self.mid.count:  # 中间的2个数都在mid的区间内
                return self.mid.val
            else:
                return (self.mid.val + self.mid.next.val) / 2  # 中间2个元素的平均值


s = MedianFinder()
s.addNum(12)
print(s.findMedian() == 12)
s.addNum(10)
print(s.findMedian() == 11)
s.addNum(13)
print(s.findMedian() == 12)
s.addNum(11)
print(s.findMedian() == 11.5)
s.addNum(5)
s.addNum(15)
s.addNum(1)
s.addNum(11)
s.addNum(6)
s.addNum(17)
s.addNum(14)
s.addNum(8)
s.addNum(17)
s.addNum(6)
s.addNum(4)
s.addNum(16)
s.addNum(8)
print(s.findMedian())  # 11
s.addNum(10)
print(s.findMedian())  # 10.5
s.addNum(2)
print(s.findMedian())  # 10
s.addNum(12)
print(s.findMedian())  # 10.5
s.addNum(0)
print(s.findMedian())  # 10

s = MedianFinder()
s.addNum(1)
s.addNum(2)
print(s.findMedian())
s.addNum(3)
print(s.findMedian())

s = MedianFinder()
s.addNum(-1)
print(s.findMedian())
s.addNum(-2)
print(s.findMedian())
s.addNum(-3)
print(s.findMedian())
s.addNum(-4)
print(s.findMedian())
s.addNum(-5)
print(s.findMedian())
