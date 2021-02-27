'''
旋转链表

给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
'''
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
解决思路：首尾相连后，求得链表长度n，再前进n-(k%n)步，此时指向的节点为head
'''


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head
        tail = head
        n = 1
        while tail.next is not None:
            n += 1
            tail = tail.next
        tail.next = head
        for i in range(n - (k % n)):
            tail = head
            head = head.next
        tail.next = None
        return head


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
print(toList(s.rotateRight(fromList([]), 0)))
print(toList(s.rotateRight(fromList([1, 2, 3, 4, 5]), 2)))
print(toList(s.rotateRight(fromList([0, 1, 2]), 4)))
