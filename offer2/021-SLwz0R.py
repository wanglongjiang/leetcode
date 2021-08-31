'''
剑指 Offer II 021. 删除链表的倒数第 n 个结点
给定一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

 

示例 1：



输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
示例 2：

输入：head = [1], n = 1
输出：[]
示例 3：

输入：head = [1,2], n = 1
输出：[1]
 

提示：

链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

进阶：能尝试使用一趟扫描实现吗？

 

注意：本题与主站 19 题相同： https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/SLwz0R
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
解题思路：双指针
设置2个指针，第1个指针p1指向当前最后1个节点，第2个指针p2在p1后面间隔n，
当p1指向末尾时，p2指向倒数第n个节点

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p1 = head
        pNth = head
        prePNth = None
        width = 0
        while p1 is not None:
            p1 = p1.next
            width += 1
            if n == width:
                if p1 is not None:
                    prePNth = pNth
                    pNth = pNth.next
                    width -= 1
                else:
                    if prePNth is not None:
                        prePNth.next = pNth.next
                    else:
                        # 这种情况下head为要删除的节点
                        head = head.next
        return head
