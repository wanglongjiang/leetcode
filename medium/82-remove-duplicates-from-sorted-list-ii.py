'''
删除排序链表中的重复元素 II
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
'''
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
思路：相比83题，需要多2个变量保存最后一次不重复的节点
'''


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        lastVal = None
        prepre, pre, p = None, None, head
        preDeleted = False
        while p:
            if p.val == lastVal:
                preDeleted = True
                if head == pre:
                    head = None
                if prepre:
                    if head is None:
                        head = prepre
                    prepre.next = p.next
            else:
                lastVal = p.val
                if head is None:
                    head = p
                if pre and not preDeleted:
                    prepre = pre
                preDeleted = False
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
print(toList(s.deleteDuplicates(fromList([1, 1, 1, 2, 3]))))
print(toList(s.deleteDuplicates(fromList([1, 2, 3, 3, 4, 4, 5]))))
print(toList(s.deleteDuplicates(fromList([1, 1, 1, 2, 2, 3, 3]))))
print(toList(s.deleteDuplicates(fromList([1]))))
print(toList(s.deleteDuplicates(fromList([1, 2, 3]))))
print(toList(s.deleteDuplicates(fromList([1, 2, 3, 3]))))
print(toList(s.deleteDuplicates(fromList([]))))
