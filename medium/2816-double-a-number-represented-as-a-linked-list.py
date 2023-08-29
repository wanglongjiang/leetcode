from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stk = []
        p = head
        while p:
            stk.append(p.val)
            p = p.next
        p = None
        carry = 0
        while stk:
            carry, val = divmod(2 * stk.pop() + carry, 10)
            p = ListNode(val, p)
        if carry > 0:
            p = ListNode(carry, p)
        return p
