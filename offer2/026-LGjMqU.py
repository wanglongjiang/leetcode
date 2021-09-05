'''
剑指 Offer II 026. 重排链表
给定一个单链表 L 的头节点 head ，单链表 L 表示为：

 L0 → L1 → … → Ln-1 → Ln 
请将其重新排列后变为：

L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例 1:



输入: head = [1,2,3,4]
输出: [1,4,2,3]
示例 2:



输入: head = [1,2,3,4,5]
输出: [1,5,2,4,3]
 

提示：

链表的长度范围为 [1, 5 * 104]
1 <= node.val <= 1000
 

注意：本题与主站 143 题相同：https://leetcode-cn.com/problems/reorder-list/ 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/LGjMqU
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
思路1，栈。
    遍历2次链表。
        第1次设置2个指针mid，right，right每前进2个节点，mid前进1个节点。当right到达末尾时，mid为中点。将mid之后的节点入栈。
        第2次，将入栈的节点依次出栈，插入前半部分
    时间复杂度：O(n)
    空间复杂度：O(n)
思路2，反转链表。
    遍历2次链表。
        第1次设置2个指针mid，right，right每前进2个节点，mid前进1个节点。当right到达末尾时，mid为中点。从mid开始，反转链表。
        第2次，将反转后的链表插入前半部分。
    时间复杂度：O(n)
    空间复杂度：O(1)
'''


class Solution:
    # 思路2 翻转链表
    def reorderList(self, head: ListNode) -> None:
        # 得到右半部分
        mid, right = head, head
        length = 0
        while right:
            right = right.next
            if length % 2 == 1:
                mid = mid.next
            length += 1
        if mid:
            right = mid.next
            mid.next = None
        # 将右半部分翻转
        rightHead = None
        while right:
            next = right.next
            right.next = rightHead
            rightHead = right
            right = next
        # 将右半部分交替插入左半部分
        while head and rightHead:
            next = head.next
            rightNext = rightHead.next
            head.next = rightHead
            head.next.next = next
            head = next
            rightHead = rightNext

    # 思路1，栈
    def reorderList1(self, head: ListNode) -> None:
        # 得到右半部分
        mid, right = head, head
        length = 0
        while right:
            right = right.next
            if length % 2 == 1:
                mid = mid.next
            length += 1
        stack = []
        # 右半部分入栈
        tail = mid
        while mid and mid.next:
            stack.append(mid.next)
            mid = mid.next
        if tail:
            tail.next = None
        # 右半部分交替插入左半部分
        while head and stack:
            next = head.next
            head.next = stack.pop()
            head.next.next = next
            head = next
