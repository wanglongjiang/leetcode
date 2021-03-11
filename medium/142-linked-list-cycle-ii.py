'''
环形链表 II
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。

说明：不允许修改给定的链表。

进阶：

你是否可以使用 O(1) 空间解决此题？
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
思路1，遍历链表，遍历过的节点放入set中，如果遍历过程中发现节点在set中存在，有环；如果完成后未发现set中有重复遍历的节点，则没有环。
    时间复杂度：O(n)，遍历1次
    空间复杂度：O(n)
思路2，要求常量空间，提示中说明：-10^5 <= Node.val <= 10^5，可以将遍历过的节点值+10^7，如果遍历过程中没有遇到>10^6的值，说明没有环。
    时间复杂度：O(n)，如果有要求可以遍历第2次将值恢复
    空间复杂度：O(1)
'''


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        n1, n2 = pow(10, 7), pow(10, 6)
        p = head
        while p and p.val < n2:
            p.val += n1
            p = p.next
        return p
