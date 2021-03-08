'''
分隔链表
给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

你应当 保留 两个分区中每个节点的初始相对位置。
'''
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
思路：从头搜索，所有找到的小于x的节点，都从原链表删除，加入链表lessLi。
    遍历一次之后，所有小于x的节点都按照原顺序处于lessLi中，将lessLi与原链表连结起来
    时间复杂度：O(n)，只需要遍历一次链表
'''


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        lessHead = ListNode()  # 新的头，简化逻辑
        lessTail = lessHead
        pre, p = ListNode(), head
        pre.next = p
        head = pre  # head也指向新的头，简化逻辑
        while p:
            if p.val < x:  # 一次遍历后，将所有小于x的节点链接到lessHead后面
                pre.next = p.next
                lessTail.next = p
                lessTail = p
                p.next = None
                p = pre.next
            else:
                pre = p
                p = p.next
        lessTail.next = head.next  # 两个链表链接起来
        return lessHead.next


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
print(toList(s.partition(fromList([1, 4, 3, 2, 5, 2]), 3)))
print(toList(s.partition(fromList([2, 1]), 2)))
