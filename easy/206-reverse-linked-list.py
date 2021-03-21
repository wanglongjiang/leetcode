'''
反转链表
反转一个单链表。
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
思路1，迭代法。通过2个临时变量，一次将原链表的节点插入到新链表表头
思路2，递归法。
'''


class Solution:
    # 迭代模式
    def reverseList(self, head: ListNode) -> ListNode:
        newHead = None
        while head:
            next = head.next
            head.next = newHead
            newHead = head
            head = next
        return newHead

    # 递归模式
    def reverseList2(self, head: ListNode) -> ListNode:
        def recursion(old, new):
            if old is None:
                return new
            else:
                next = old.next
                old.next = new
                return recursion(next, old)

        return recursion(head, None)
