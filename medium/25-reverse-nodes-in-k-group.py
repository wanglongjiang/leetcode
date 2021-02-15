'''
 K 个一组翻转链表

给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例：
给你这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
'''
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
思路：3个指针，groupLeft,groupHead,groupTail
1、每前进k步，截取子链表
2、翻转子链表
   groupHead.next = groupTail
3、groupLeft.next = groupTail

'''


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        pass


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
print(toList(s.reverseKGroup(fromList([1, 2, 3, 4], 2))))
print(toList(s.reverseKGroup(fromList([1, 2, 3, 4], 3))))
print(toList(s.reverseKGroup(fromList([]))))
print(toList(s.reverseKGroup(fromList([1]))))
print(toList(s.reverseKGroup(fromList([1, 2, 3]))))
print(toList(s.reverseKGroup(fromList([1, 2, 3, 4, 5, 6, 7], 2))))
print(toList(s.reverseKGroup(fromList([1, 2, 3, 4, 5, 6, 7], 3))))
print(toList(s.reverseKGroup(fromList([1, 2, 3, 4, 5, 6, 7], 4))))
