'''
删除排序链表中的重复元素
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
'''
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
思路：问题很好解决，用1个变量保存最后一次遍历过的值，如果重复删除。
'''


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        lastVal = None
        pre, p = None, head
        while p:
            if p.val == lastVal:
                pre.next = p.next
            else:
                lastVal = p.val
                pre = p
            p = p.next
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
print(toList(s.deleteDuplicates(fromList([1, 1, 2]))))
print(toList(s.deleteDuplicates(fromList([1, 1, 2, 3, 3]))))
print(toList(s.deleteDuplicates(fromList([1, 2, 3, 3, 4, 4, 5]))))
print(toList(s.deleteDuplicates(fromList([1, 1, 1, 2, 3]))))
