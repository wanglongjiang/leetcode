'''
合并两个有序链表
'''
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
思路：链表
迭代2个链表，如果l1>l2，则将l2插入新的链表，否则将l1插入新的链表，直至2个链表都为空

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        tail = head
        while l1 and l2:
            if l1.val > l2.val:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
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
print(toList(s.mergeTwoLists(fromList([1, 2, 4]), fromList([1, 3, 5]))))
print(toList(s.mergeTwoLists(fromList([2, 4, 6]), fromList([1, 3, 5]))))
print(toList(s.mergeTwoLists(fromList([]), fromList([]))))
print(toList(s.mergeTwoLists(fromList([]), fromList([0]))))
