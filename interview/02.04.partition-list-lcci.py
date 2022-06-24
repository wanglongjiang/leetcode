'''
面试题 02.04. 分割链表
编写程序以 x 为基准分割链表，使得所有小于 x 的节点排在大于或等于 x 的节点之前。如果链表中包含 x，
x 只需出现在小于 x 的元素之后(如下所示)。分割元素 x 只需处于“右半部分”即可，其不需要被置于左右两部分之间。

示例:

输入: head = 3->5->8->5->10->2->1, x = 5
输出: 3->1->2->10->5->5->8

'''

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
思路：链表
设置2个哨兵lessHead, greaterHead分别指向小于x和大于等于x的链表
遍历链表，将小于x的节点从原链表删除链接到lessHead后面，大于等于x链接到greaterHead后面

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        lessHead, greaterHead = ListNode(), ListNode()
        node = head
        while node:
            nextNode = node.next
            if node.val < x:
                node.next = lessHead.next
                lessHead.next = node
            else:
                node.next = greaterHead.next
                greaterHead.next = node
            node = nextNode
        node = lessHead
        while node.next:
            node = node.next
        node.next = greaterHead.next
        return lessHead.next


s = Solution()


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


print(toList(s.partition(fromList([1, 1]), 2)))
