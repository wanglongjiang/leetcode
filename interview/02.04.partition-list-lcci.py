'''
面试题 02.04. 分割链表
编写程序以 x 为基准分割链表，使得所有小于 x 的节点排在大于或等于 x 的节点之前。如果链表中包含 x，
x 只需出现在小于 x 的元素之后(如下所示)。分割元素 x 只需处于“右半部分”即可，其不需要被置于左右两部分之间。

示例:

输入: head = 3->5->8->5->10->2->1, x = 5
输出: 3->1->2->10->5->5->8

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
思路：链表
设置1个哨兵newHead指向原head节点
遍历链表，将小于x的节点从原链表删除链接到newHead后面

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        newHead = ListNode()
        newHead.next = head
        prev = newHead
        node = head
        while node:
            nextNode = node.next
            if node.val < x:  # 当前节点<x，需要移动到左边
                prev.next = nextNode
                node.next = newHead.next
                newHead.next = node
            else:
                prev = node
            node = nextNode
        return newHead.next
