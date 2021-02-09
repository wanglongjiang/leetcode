'''
合并两个有序链表
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        tail = None
        while l1 is not None and l2 is not None:
            if l1.val > l2.val:
                if head is None:
                    head = l2
                    tail = l2
                else:
                    tail.next = l2
                    tail = l2
                l2 = l2.next
            else:
                if head is None:
                    head = l1
                    tail = l1
                else:
                    tail.next = l1
                    tail = l1
                l1 = l1.next

        if l1 is not None:
            if tail is None:
                return l1
            else:
                tail.next = l1
                return head
        if l2 is not None:
            if tail is None:
                return l2
            else:
                tail.next = l2
                return head
        return head


s = Solution()
print(s.mergeTwoLists([1, 2, 4], [1, 3, 4]))
print(s.mergeTwoLists([], []))
print(s.mergeTwoLists([], [0]))
