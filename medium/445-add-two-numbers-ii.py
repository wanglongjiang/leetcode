'''
两数相加 II
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

 

进阶：

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
思路：栈
用栈先保存2个链表的数据，然后出栈相加、生成链表
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        s1 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        s2 = []
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        head = None
        carry = 0
        while s1 and s2:
            num = s1.pop() + s2.pop() + carry
            if num >= 10:
                num -= 10
                carry = 1
            else:
                carry = 0
            node = ListNode(num)
            node.next = head
            head = node
        s = s1 if len(s1) > 0 else s2
        while s:
            num = s.pop() + carry
            if num >= 10:
                num -= 10
                carry = 1
            else:
                carry = 0
            node = ListNode(num)
            node.next = head
            head = node
        if carry:
            node = ListNode(1)
            node.next = head
            head = node
        return head
