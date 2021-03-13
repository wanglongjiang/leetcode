'''
对链表进行插入排序
插入排序算法：

插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。
'''
from typing import List
'''
思路：按照题目里的插入排序算法，创建1个已排序表（初始为空），将输入的链表的节点依次插入到已排序链表里面
    时间复杂度：最坏情况下O(n^2)
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        sortedHead = ListNode(float('-inf'))
        while head:
            node = head
            head = head.next
            p = sortedHead
            while p.next and p.next.val < node.val:
                p = p.next
            nextNode = p.next
            p.next = node
            node.next = nextNode
        return sortedHead.next


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
print(toList(s.insertionSortList(fromList([4, 2, 1, 3]))))
print(toList(s.insertionSortList(fromList([-1, 5, 3, 4, 0]))))
