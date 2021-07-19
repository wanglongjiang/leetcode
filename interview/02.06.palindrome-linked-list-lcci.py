'''
面试题 02.06. 回文链表
编写一个函数，检查输入的链表是否是回文的。

 

示例 1：

输入： 1->2
输出： false
示例 2：

输入： 1->2->2->1
输出： true
 

进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
'''
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
思路：翻转后半部链表
1. 遍历一次链表，计算出长度n
2. 移动到第n/2个链表处，开始翻转后半部链表
3. 对比2个链表是否相同

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        p = head
        n = 0
        while p:
            n += 1
            p = p.next
        if n == 0 or n == 1:
            return True
        if n == 2:
            return head.val == head.next.val
        # 移动到第n/2个节点处
        m = n // 2 + n % 2
        p = head
        while m:
            m -= 1
            p = p.next
        # 翻转后半部链表
        newhead = None
        while p:
            nxt = p.next
            p.next = newhead
            newhead = p
            p = nxt
        # 对比2个链表
        while newhead:
            if newhead.val != head.val:
                return False
            newhead = newhead.next
            head = head.next
        return True


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


s = Solution()
print(s.isPalindrome(fromList([1, 2])))
print(s.isPalindrome(fromList([1, 2, 2, 1])))
