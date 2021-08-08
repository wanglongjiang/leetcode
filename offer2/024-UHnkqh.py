'''
剑指 Offer II 024. 反转链表

给定单链表的头节点 head ，请反转链表，并返回反转后的链表的头节点。

 

示例 1：


输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
示例 2：


输入：head = [1,2]
输出：[2,1]
示例 3：

输入：head = []
输出：[]
 

提示：

链表中节点的数目范围是 [0, 5000]
-5000 <= Node.val <= 5000
 

进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？

 

注意：本题与主站 206 题相同： https://leetcode-cn.com/problems/reverse-linked-list/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/UHnkqh
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
