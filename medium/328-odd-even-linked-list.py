'''
奇偶链表
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。

请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

说明:

应当保持奇数节点和偶数节点的相对顺序。
链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。
'''
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
思路：1次遍历，分成2个链表，然后连结。
时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        i = 0
        oddHead, evenHead = ListNode(), ListNode()  # 设置两个哨兵
        oddTail, evenTail = oddHead, evenHead
        while head:
            i += 1
            if i & 1:  # 根据节点的奇偶性，分别链接到2个链表中
                oddTail.next = head
                oddTail = oddTail.next
            else:
                evenTail.next = head
                evenTail = evenTail.next
            head = head.next
        oddTail.next = evenHead.next  # 连结2个链表
        evenTail.next = None
        return oddHead.next


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
print(toList(s.oddEvenList(fromList([]))))
print(toList(s.oddEvenList(fromList([1, 2, 3, 4, 5]))))
print(toList(s.oddEvenList(fromList([2, 1, 3, 5, 6, 4, 7]))))
