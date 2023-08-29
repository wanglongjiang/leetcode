from math import gcd
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        while p.next:
            next = p.next
            p.next = ListNode(gcd(p.val, next.val), next)
            p = next
        return head
