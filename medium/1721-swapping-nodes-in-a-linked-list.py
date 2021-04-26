'''
交换链表中的节点
给你链表的头节点 head 和一个整数 k 。

交换 链表正数第 k 个节点和倒数第 k 个节点的值后，返回链表的头节点（链表 从 1 开始索引）。
提示：

链表中节点的数目是 n
1 <= k <= n <= 105
0 <= Node.val <= 100
'''
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
思路：2次遍历并交换
设置1个哨兵，从0开始计数先找到第k个节点，然后继续遍历计算出链表长度n
然后计算出倒数第k个节点的坐标rk = n-k+1，然后找到第rk个节点与第k个节点交换
时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        head = ListNode(0, head)
        i = 1
        k_pre, k_node = head, head.next
        while i < k:  # 找到第k个节点
            k_pre = k_node
            k_node = k_node.next
            i += 1
        node = k_node
        while node:  # 计算链表长度
            node = node.next
            i += 1
        n = i - 1
        i = 1
        rk = n - k + 1
        if k == rk:  # 正数倒数都一样，直接返回
            return head.next
        rk_pre, rk_node = head, head.next
        while i < rk:  # 找到第rk个节点
            rk_pre = rk_node
            rk_node = rk_node.next
            i += 1
        # 交换2个节点
        k_pre.next, rk_pre.next = rk_pre.next, k_pre.next
        k_node.next, rk_node.next = rk_node.next, k_node.next
        return head.next


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
print(toList(s.swapNodes(fromList([1, 2, 3, 4, 5]), 2)))
print(toList(s.swapNodes(fromList([7, 9, 6, 6, 7, 8, 3, 0, 9, 5]), 5)))
print(toList(s.swapNodes(fromList([1]), 1)))
print(toList(s.swapNodes(fromList([1, 2]), 1)))
print(toList(s.swapNodes(fromList([1, 2, 3]), 2)))
