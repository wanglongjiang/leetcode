'''
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode()
        tail = head
        while l1 is not None or l2 is not None:
            sum = carry
            if l1 is not None:
                sum += l1.val
                l1 = l1.next
            if l2 is not None:
                sum += l2.val
                l2 = l2.next
            tail.next = ListNode()
            tail = tail.next
            if sum >= 10:
                tail.val = sum % 10
                carry = 1
            else:
                tail.val = sum
                carry = 0
        if carry > 0:
            tail.next = ListNode()
            tail = tail.next
            tail.val = carry
        return head.next


s = Solution()


def transArr2LinkedList(arr):
    if len(arr) == 0:
        return None
    head = ListNode(arr[0], None)
    tail = head
    for i in range(1, len(arr)):
        tail.next = ListNode(arr[i], None)
        tail = tail.next
    return head


print(
    s.addTwoNumbers(transArr2LinkedList([2, 4, 3]),
                    transArr2LinkedList([5, 6, 4])))
