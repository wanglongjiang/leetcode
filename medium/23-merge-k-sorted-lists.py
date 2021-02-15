'''
合并K个升序链表

给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。
'''
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
思路：递归归并
'''


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge(start, end) -> ListNode:
            if end - start == 0:
                return None
            elif end - start == 1:
                return lists[start]
            else:
                mid = (start + end) // 2
                li1 = merge(start, mid)
                li2 = merge(mid, end)
                newlist = None
                tail = None
                while li1 is not None and li2 is not None:
                    if li1.val <= li2.val:
                        smallNode = li1
                        li1 = li1.next
                    else:
                        smallNode = li2
                        li2 = li2.next
                    if newlist is None:
                        newlist = ListNode(smallNode.val)
                        tail = newlist
                    else:
                        tail.next = ListNode(smallNode.val)
                        tail = tail.next
                if newlist is None:
                    newlist = li1 if li2 is None else li2
                else:
                    tail.next = li1 if li2 is None else li2
                return newlist

        return merge(0, len(lists))


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
print(
    toList(
        s.mergeKLists(
            [fromList([1, 4, 5]),
             fromList([1, 3, 4]),
             fromList([2, 6])])))
print(toList(s.mergeKLists([])))
print(toList(s.mergeKLists([None])))
