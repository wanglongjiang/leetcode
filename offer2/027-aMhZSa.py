'''
剑指 Offer II 027. 回文链表
给定一个链表的 头节点 head ，请判断其是否为回文链表。

如果一个链表是回文，那么链表节点序列从前往后看和从后往前看是相同的。

 

示例 1：



输入: head = [1,2,3,3,2,1]
输出: true
示例 2：



输入: head = [1,2]
输出: fasle
 

提示：

链表 L 的长度范围为 [1, 10^5]
0 <= node.val <= 9
 

进阶：能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

 

注意：本题与主站 234 题相同：https://leetcode-cn.com/problems/palindrome-linked-list/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/aMhZSa
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
思路：栈，双指针
将链表元素加入栈中，然后将栈视为数组，用双指针从2端向中间对比
时间复杂度：O(n)
空间复杂度：O(n)

如果要优化到空间复杂度为O(1)，可以先找到中点，然后翻转中点之后的链表，再进行对比
'''


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stk = []
        while head:
            stk.append(head.val)
            head = head.next
        n = len(stk)
        for i in range(n // 2):
            if stk[i] != stk[n - i - 1]:
                return False
        return True
