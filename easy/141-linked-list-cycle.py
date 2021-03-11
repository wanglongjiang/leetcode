'''
环形链表
给定一个链表，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

如果链表中存在环，则返回 true 。 否则，返回 false 。
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
    def hasCycle(self, head: ListNode) -> bool:
        n1, n2 = pow(10, 7), pow(10, 6)
        p = head
        while p and p.val < n2:
            p.val += n1
            p = p.next
        return p is not None
