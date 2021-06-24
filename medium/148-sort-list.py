'''
排序链表

给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

进阶：

你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
'''

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
题目中没有指出O(nlogn)是在平均情况下还是最坏情况下，最坏情况下能达到O(nlogn)的排序算法有归并排序。
平均情况下达到O(nlogn)的是快排。
选择、冒泡、插入时间上达不到要求。
基数、希尔、堆排序不合适。

思路1，自底向上的归并排序，最坏、最好、平均时间复杂度一样，都是O(nlogn)
常规归并排序的空间复杂度是O(n)，想了1个自底向上的归并排序算法：
第1次遍历，每2个元素为1组，进行组内排序。
第2次遍历，每4个元素为1组，它的左右2部分已经排序完成，2个部分依次比较、交换
第3次遍历，每8个元素为1组，它的左右2部分已经排序完成，。。。
经过logn次遍历，链表变为有序。

时间复杂度：O(nlogn)，需要经过logn次遍历
空间复杂度：O(1)

思路2，快速排序，平均情况下时间复杂度为O(nlogn)，最坏情况下O(n^2)
1、遍历链表，以表头元素为pivot，将小于表头的插入表头前面。
2、针对新链表的head..pivot及pivot..tail，分别执行上面第1步，直至子链表长度为1
空间复杂度：O(1)
'''


class Solution:
    # 自底向上的归并排序
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        head = ListNode(0, head)
        # 计算链表长度
        p = head.next
        n = 0
        while p:
            p = p.next
            n += 1
        sublen = 1

        def merge(pre1, pre2, length):  # 合并2个链表，返回第2个链表的末尾
            i1, i2 = 0, 0
            while pre1.next and pre2.next and (i1 < length and i2 < length):
                if pre1.next.val > pre2.next.val:  # 第1个链表节点大于第2个链表节点，将第2个链表节点移动到第1个链表中
                    p1next = pre1.next
                    pre1.next = pre2.next
                    pre2.next = pre2.next.next
                    pre1.next.next = p1next
                    pre1 = pre1.next
                    i2 += 1
                else:
                    i1 += 1
                    pre1 = pre1.next
            while pre2.next and i2 < length:
                i2 += 1
                pre2 = pre2.next
            return pre2

        while sublen < n:  # 一直归并到子数组长度达到n
            pre1, pre2 = head, None  # 子链表的前一个节点
            p = pre1
            while p:  # 一次完整的归并需要遍历整个链表
                i = 0
                # 遍历第1个子数组
                while p and i < sublen:
                    p = p.next
                    i += 1
                if not p or p.next is None:  # 后面没有节点，不需要归并
                    break
                pre2 = p
                pre1 = merge(pre1, pre2, sublen)  # 归并2个子数组
                p = pre1
            sublen *= 2  # 子数组长度*2
        return head.next

    # 快速排序
    def sortList2(self, head: ListNode) -> ListNode:
        head = ListNode(0, head)  # 头部设置1个哨兵

        def parttiion(headPrev, head, tail):
            if head == tail:
                return
            pivot = head
            leftTail = headPrev  # 该变量为左边链表的尾部
            prev = pivot  # 该变量为当前元素的前一个
            p = head.next
            # 这个循环把大于pivot的移动到pivot的左边
            while p != tail:
                if pivot.val > p.val:
                    prev.next = p.next  # 将当前元素的上一节点与下一个连结起来
                    leftTail.next = p  # 将p移动到左边
                    leftTail = p
                    leftTail.next = pivot
                    p = prev.next
                else:
                    prev = p
                    p = p.next
            # 继续分区
            if leftTail != headPrev:
                parttiion(headPrev, headPrev.next, pivot)
            if pivot.next:
                parttiion(pivot, pivot.next, tail)

        parttiion(head, head.next, None)
        return head.next


def fromList(li: List[int]):
    head = None
    tail = head
    for item in li:
        if head is None:
            head = ListNode(item)
            tail = head
        else:
            tail.next = ListNode(item)
            tail = tail.next
    return head


def toList(listNode: ListNode):
    if listNode is None:
        return []
    else:
        li = []
        while listNode is not None:
            li.append(listNode.val)
            listNode = listNode.next
        return li


s = Solution()
print(
    toList(
        s.sortList(
            fromList([
                1, 3, 3, 1, 3, 1, 3, 3, 2, 3, 2, 2, 1, 1, 1, 3, 2, 2, 1, 1, 2, 2, 2, 3, 3, 1, 1, 2, 2, 2, 1, 2, 1, 1, 2, 3, 3, 2, 2, 3, 2, 3, 2, 2, 2, 1, 1, 3,
                2, 3, 3, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 3, 1, 3, 1, 1, 1, 2, 1, 2, 2, 2, 1, 3, 2, 2, 2, 3, 3, 2, 3, 3, 1, 1, 2, 2, 1, 2, 1, 3, 2, 1
            ]))))
print(toList(s.sortList(fromList([]))))
print(toList(s.sortList(fromList([1]))))
print(toList(s.sortList(fromList([2, 1]))))
print(toList(s.sortList(fromList([3, 2, 1]))))
print(toList(s.sortList(fromList([4, 2, 1, 3]))))
print(toList(s.sortList(fromList([-1, 5, 3, 4, 0]))))
