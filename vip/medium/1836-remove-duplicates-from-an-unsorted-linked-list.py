'''
1836. 从未排序的链表中移除重复元素
给定一个链表的第一个节点 head ，找到链表中所有出现多于一次的元素，并删除这些元素所在的节点。

返回删除后的链表。



示例 1:


输入: head = [1,2,3,2]
输出: [1,3]
解释: 2 在链表中出现了两次，所以所有的 2 都需要被删除。删除了所有的 2 之后，我们还剩下 [1,3] 。
示例 2:


输入: head = [2,1,1,2]
输出: []
解释: 2 和 1 都出现了两次。所有元素都需要被删除。
示例 3:


输入: head = [3,2,2,1,3,2,4]
输出: [1,4]
解释: 3 出现了两次，且 2 出现了三次。移除了所有的 3 和 2 后，我们还剩下 [1,4] 。


提示：

链表中节点个数的范围是 [1, 10^5]
1 <= Node.val <= 10^5
'''
from collections import defaultdict


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
思路：哈希
2次遍历链表，
第1次遍历对所有元素计数，
第2次遍历将出现次数>=2的元素从链表中删除

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        counter = defaultdict(int)
        node = head
        while node:
            counter[node.val] += 1
            node = node.next
        head = ListNode(0, head)  # 添加一个头部哨兵方便计算
        prev = head
        while prev.next:
            if counter[prev.next.val] > 1:  # 超过1个的，需要从链表中删除
                prev.next = prev.next.next
            else:
                prev = prev.next
        return head.next
