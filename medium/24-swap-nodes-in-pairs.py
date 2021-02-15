'''
两两交换链表中的节点
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

例如：
输入：head = [1,2,3,4]
输出：[2,1,4,3]
'''
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
思路：有3个指针，pLeft,pa,pb，执行如下操作后交换：
pLeft.next = pb
pa.next = pb.next
pb.next = pa
'''


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        pLeft = None
        pa = head
        pb = head.next
        while pa is not None and pb is not None:
            if pLeft is None:
                head = pb
            else:
                pLeft.next = pb
            pa.next = pb.next
            pb.next = pa
            # 指针向后移动2个节点
            pLeft = pa
            pa = pLeft.next
            if pa is None:
                break
            pb = pa.next
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
print(toList(s.swapPairs(fromList([1, 2, 3, 4]))))
print(toList(s.swapPairs(fromList([]))))
print(toList(s.swapPairs(fromList([1]))))
print(toList(s.swapPairs(fromList([1, 2, 3]))))
print(toList(s.swapPairs(fromList([1, 2, 3, 4, 5]))))
