'''
剑指 Offer II 025. 链表中的两数相加
给定两个 非空链表 l1和 l2 来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

可以假设除了数字 0 之外，这两个数字都不会以零开头。

 

示例1：



输入：l1 = [7,2,4,3], l2 = [5,6,4]
输出：[7,8,0,7]
示例2：

输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[8,0,7]
示例3：

输入：l1 = [0], l2 = [0]
输出：[0]
 

提示：

链表的长度范围为 [1, 100]
0 <= node.val <= 9
输入数据保证链表代表的数字无前导 0
 

进阶：如果输入链表不能修改该如何处理？换句话说，不能对列表中的节点进行翻转。

 

注意：本题与主站 445 题相同：https://leetcode-cn.com/problems/add-two-numbers-ii/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lMSNwu
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
思路：栈
用栈先保存2个链表的数据，然后出栈相加、生成链表
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        s1 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        s2 = []
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        head = None
        carry = 0
        while s1 and s2:
            num = s1.pop() + s2.pop() + carry
            if num >= 10:
                num -= 10
                carry = 1
            else:
                carry = 0
            node = ListNode(num)
            node.next = head
            head = node
        s = s1 if len(s1) > 0 else s2
        while s:
            num = s.pop() + carry
            if num >= 10:
                num -= 10
                carry = 1
            else:
                carry = 0
            node = ListNode(num)
            node.next = head
            head = node
        if carry:
            node = ListNode(1)
            node.next = head
            head = node
        return head
