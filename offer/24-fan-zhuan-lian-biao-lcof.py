'''
剑指 Offer 24. 反转链表

定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

 

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
 

限制：

0 <= 节点个数 <= 5000

 

注意：本题与主站 206 题相同：https://leetcode-cn.com/problems/reverse-linked-list/
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
思路1，迭代法。通过2个临时变量，一次将原链表的节点插入到新链表表头
思路2，递归法。
'''


class Solution:
    # 迭代模式
    def reverseList(self, head: ListNode) -> ListNode:
        newHead = None
        while head:
            next = head.next
            head.next = newHead
            newHead = head
            head = next
        return newHead

    # 递归模式
    def reverseList2(self, head: ListNode) -> ListNode:
        def recursion(old, new):
            if old is None:
                return new
            else:
                next = old.next
                old.next = new
                return recursion(next, old)

        return recursion(head, None)
