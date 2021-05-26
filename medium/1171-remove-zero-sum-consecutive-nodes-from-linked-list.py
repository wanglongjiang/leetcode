'''
从链表中删去总和值为零的连续节点
给你一个链表的头节点 head，请你编写代码，反复删去链表中由 总和 值为 0 的连续节点组成的序列，直到不存在这样的序列为止。

删除完毕后，请你返回最终结果链表的头节点。

 

你可以返回任何满足题目要求的答案。

（注意，下面示例中的所有序列，都是对 ListNode 对象序列化的表示。）

示例 1：

输入：head = [1,2,-3,3,1]
输出：[3,1]
提示：答案 [1,2,1] 也是正确的。
示例 2：

输入：head = [1,2,3,-3,4]
输出：[1,2,4]
示例 3：

输入：head = [1,2,3,-3,-2]
输出：[1]
 

提示：

给你的链表中可能有 1 到 1000 个节点。
对于链表中的每个节点，节点的值：-1000 <= node.val <= 1000.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
思路：暴力遍历所有的子链表
暴力遍历所有的子链表，遍历的同时合计子链表之和，如果和为0，删除子链表

时间复杂度：O(n^2)
空间复杂度：O(1)

'''


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        newhead = ListNode(0)
        newhead.next = head
        start = head
        prev = newhead
        while start:
            total = start.val
            end = start.next
            while total != 0 and end:  # 遍历子链表，直至和为0或者遍历结束
                total += end.val
                end = end.next
            if total == 0:  # 如果链表和为0，删除子链表
                prev.next = end
                start = end
            else:  # 如果找不到和为0的子链表，start前进一步
                prev = start
                start = start.next
        return newhead.next
