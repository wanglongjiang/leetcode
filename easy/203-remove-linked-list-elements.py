'''
移除链表元素
给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
思路：链表一次遍历并删除
时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        newhead = ListNode()  # 头部增加1个哨兵简化算法
        newhead.next = head
        prev = newhead
        node = head
        while node:
            if node.val == val:
                prev.next = node.next
            else:
                prev = node
            node = node.next
        return newhead.next
