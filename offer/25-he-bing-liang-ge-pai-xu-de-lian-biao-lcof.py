'''
剑指 Offer 25. 合并两个排序的链表

输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
限制：

0 <= 链表长度 <= 1000

注意：本题与主站 21 题相同：https://leetcode-cn.com/problems/merge-two-sorted-lists/
'''
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
思路：链表
迭代2个链表，如果l1>l2，则将l2插入新的链表，否则将l1插入新的链表，直至2个链表之一为空
最后将l1或l2剩余部分连结到新链表末尾

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        tail = head
        while l1 and l2:
            if l1.val > l2.val:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next
            tail = tail.next
        if l1:  # l1的剩余部分连结到新链表
            tail.next = l1
        if l2:  # l2的剩余部分连结到新链表
            tail.next = l2
        return head.next


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
print(toList(s.mergeTwoLists(fromList([1, 2, 4]), fromList([1, 3, 5]))))
print(toList(s.mergeTwoLists(fromList([2, 4, 6]), fromList([1, 3, 5]))))
print(toList(s.mergeTwoLists(fromList([]), fromList([]))))
print(toList(s.mergeTwoLists(fromList([]), fromList([0]))))
