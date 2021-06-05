'''
合并两个链表
给你两个链表 list1 和 list2 ，它们包含的元素分别为 n 个和 m 个。

请你将 list1 中第 a 个节点到第 b 个节点删除，并将list2 接在被删除节点的位置。

下图中蓝色边和节点展示了操作后的结果：

提示：

3 <= list1.length <= 10^4
1 <= a <= b < list1.length - 1
1 <= list2.length <= 10^4
'''
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
思路：没啥说的
list11次遍历找到a、b2个节点
list2遍历1次找到末尾
把a的前面的节点a_pre.next=list2.head
把b的后面的节点list2.tail.next = b_next
时间复杂度：O(m+n)
空间复杂度：O(1)
'''


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        i = 0
        a_pre, b_next = None, None
        node = list1
        while i < a:
            a_pre = node
            node = node.next
            i += 1
        while i < b:
            node = node.next
            i += 1
        b_next = node.next
        a_pre.next = list2
        b_tail = None
        node = list2
        while node:
            b_tail = node
            node = node.next
        b_tail.next = b_next
        return list1


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
print(toList(s.mergeInBetween(list1=fromList([0, 1, 2, 3, 4, 5]), a=3, b=4, list2=fromList([1000000, 1000001, 1000002]))))
print(toList(s.mergeInBetween(list1=fromList([0, 1, 2, 3, 4, 5, 6]), a=2, b=5, list2=fromList([1000000, 1000001, 1000002, 1000003, 1000004]))))
