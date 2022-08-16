'''
369. 给单链表加一
用一个 非空 单链表来表示一个非负整数，然后将这个整数加一。

你可以假设这个整数除了 0 本身，没有任何前导的 0。

这个整数的各个数位按照 高位在链表头部、低位在链表尾部 的顺序排列。

示例:

输入: [1,2,3]
输出: [1,2,4]
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
思路：栈
遍历所有节点，一次入栈。
然后从栈顶开始，加上1，如果有进位，再弹出一个节点加1，依次递推。
如果栈为空，还有进位，需要增加1个头节点。

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        stk = []
        while head:
            stk.append(head)
            head = head.next
        carry = 1
        while stk:
            head = stk.pop()
            if carry:
                if head.val == 9:
                    head.val = 0
                else:
                    head.val += 1
                    carry = 0
        if carry:
            head = ListNode(1, head)
        return head
