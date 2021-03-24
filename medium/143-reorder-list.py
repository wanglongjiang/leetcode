'''
重排链表
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
'''
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
思路1，栈。
    遍历2次链表。
        第1次设置2个指针mid，right，right每前进2个节点，mid前进1个节点。当right到达末尾时，mid为中点。将mid之后的节点入栈。
        第2次，将入栈的节点依次出栈，插入前半部分
    时间复杂度：O(n)
    空间复杂度：O(n)
思路2，反转链表。
    遍历2次链表。
        第1次设置2个指针mid，right，right每前进2个节点，mid前进1个节点。当right到达末尾时，mid为中点。从mid开始，反转链表。
        第2次，将反转后的链表插入前半部分。
    时间复杂度：O(n)
    空间复杂度：O(1)
'''


class Solution:
    def reorderList(self, head: ListNode) -> None:
        # 得到右半部分
        mid, right = head, head
        length = 0
        while right:
            right = right.next
            if length % 2 == 1:
                mid = mid.next
            length += 1
        if mid:
            right = mid.next
            mid.next = None
        # 将右半部分翻转
        rightHead = None
        while right:
            next = right.next
            right.next = rightHead
            rightHead = right
            right = next
        # 将右半部分交替插入左半部分
        while head and rightHead:
            next = head.next
            rightNext = rightHead.next
            head.next = rightHead
            head.next.next = next
            head = next
            rightHead = rightNext

    def reorderList1(self, head: ListNode) -> None:
        # 得到右半部分
        mid, right = head, head
        length = 0
        while right:
            right = right.next
            if length % 2 == 1:
                mid = mid.next
            length += 1
        stack = []
        # 右半部分入栈
        tail = mid
        while mid and mid.next:
            stack.append(mid.next)
            mid = mid.next
        if tail:
            tail.next = None
        # 右半部分交替插入左半部分
        while head and stack:
            next = head.next
            head.next = stack.pop()
            head.next.next = next
            head = next


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
li = fromList([])
s.reorderList(li)
print(toList(li))
li = fromList([1, 2, 3, 4, 5])
s.reorderList(li)
print(toList(li))
li = fromList([1, 2, 3, 4, 5, 6])
s.reorderList(li)
print(toList(li))
