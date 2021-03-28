'''
相交链表
编写一个程序，找到两个单链表相交的起始节点。
如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
'''
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
思路：链表反转。将其中一个链表反转后，如果从另外一个链表出发，能到达另外反转后的的链表表尾（原表头），如果不能到达，则没有相交。
1、链表a遍历一次到最后，算出a的长度lenA
2、链表b进行反转，同时技术出b的长度lenB
3、然后从a再出发，算出新的长度lenC。
4、将b反转，恢复原状。
我们把相交点设为i，从相交点之后的长度2个链表相同均为c，
A相交点前面的长度为a，B相交点前面的长度为b，有下面的3元一次方程：
lenA=a+c，lenB=b+c，lenC=a+b+1
求解方程后得到
a=(lenc-lenb+lena-1)/2
5、从a出发，第a+1个元素即为相交点
时间复杂度：O(n)，4.X次遍历
空间复杂度：O(1)
'''


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB, lenC = 0, 0, 0
        # 1、遍历A求lenA
        node = headA
        while node:
            lenA += 1
            node = node.next
        # 2、翻转B，同时求lenB
        newHead = None
        next = headB
        while next:
            lenB += 1
            nextnext = next.next
            next.next = newHead
            newHead = next
            next = nextnext
        # 3、遍历A，求lenC，判断是否相交
        node = headA
        isIntersect = False
        while node:
            lenC += 1
            if node == headB:
                isIntersect = True
            node = node.next
        # 4、翻转B，恢复原状
        next = newHead
        newHead = None
        while next:
            nextnext = next.next
            next.next = newHead
            newHead = next
            next = nextnext
        if not isIntersect:  # 没有相交，返回null
            return None
        # 5、遍历A，取第a个节点，即为相交点
        a = (lenC - lenB + lenA - 1) // 2
        while headA:
            if a == 0:
                return headA
            a -= 1
            headA = headA.next


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


a = fromList([4, 1, 8, 4, 5])
b = a.next

s = Solution()
print(s.getIntersectionNode(a, b).val)
