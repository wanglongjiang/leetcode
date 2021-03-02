'''
反转链表 II
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。
'''
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        i = 1
        p = head
        pre, subHead, subTail = None, None, None
        while p is not None:
            if i == left:
                subTail = p
                subHead = p
                p = p.next
            elif i == right:
                t = subHead
                subHead = p
                if pre is not None:
                    pre.next = subHead
                next = p.next
                subHead.next = t
                subTail.next = next
                break
            elif i < left:
                pre = p
                p = p.next
            elif i > left and i < right:
                t = subHead
                subHead = p
                p = p.next
                subHead.next = t
            i += 1
        if left == 1:
            return subHead
        else:
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
print(toList(s.reverseBetween(fromList([1, 2, 3, 4, 5]), 2, 4)))
print(toList(s.reverseBetween(fromList([1, 2, 3, 4, 5]), 1, 5)))
print(toList(s.reverseBetween(fromList([1, 2, 3, 4, 5]), 1, 3)))
print(toList(s.reverseBetween(fromList([1, 2, 3, 4, 5]), 4, 5)))
print(toList(s.reverseBetween(fromList([1]), 1, 1)))
