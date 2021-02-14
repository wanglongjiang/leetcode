'''
删除链表的倒数第 N 个结点
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

进阶：你能尝试使用一趟扫描实现吗？
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
解题思路：设置2个指针，第1个指针p1指向当前最后1个节点，第2个指针p2在p1后面间隔n，
当p1指向末尾时，p2指向倒数第n个节点
'''


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p1 = head
        pNth = head
        prePNth = None
        width = 0
        while p1 is not None:
            p1 = p1.next
            width += 1
            if n == width:
                if p1 is not None:
                    prePNth = pNth
                    pNth = pNth.next
                    width -= 1
                else:
                    if prePNth is not None:
                        prePNth.next = pNth.next
                    else:
                        # 这种情况下head为要删除的节点
                        head = head.next
        return head


def fromList(li):
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
print(toList(s.removeNthFromEnd(fromList([1, 2, 3, 4, 5]), 2)))
print(toList(s.removeNthFromEnd(fromList([1]), 1)))
print(toList(s.removeNthFromEnd(fromList([1, 2]), 1)))
