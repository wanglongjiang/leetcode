'''
面试题 02.02. 返回倒数第 k 个节点

实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。

注意：本题相对原题稍作改动

示例：

输入： 1->2->3->4->5 和 k = 2
输出： 4
说明：

给定的 k 保证是有效的。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
思路：双指针
利用快慢指针的思路，fast指针先前进k步，然后slow和fast指针同时前进，当fast指针到达末尾时，slow指针指向的就是倒数第k个指针

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        fast, slow = head, head
        for i in range(k):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow.val
