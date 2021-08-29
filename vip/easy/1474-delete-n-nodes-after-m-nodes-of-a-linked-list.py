'''
1474. 删除链表 M 个节点之后的 N 个节点
给定链表 head 和两个整数 m 和 n. 遍历该链表并按照如下方式删除节点:

开始时以头节点作为当前节点.
保留以当前节点开始的前 m 个节点.
删除接下来的 n 个节点.
重复步骤 2 和 3, 直到到达链表结尾.
在删除了指定结点之后, 返回修改过后的链表的头节点.

进阶问题: 你能通过就地修改链表的方式解决这个问题吗?



示例 1:



输入: head = [1,2,3,4,5,6,7,8,9,10,11,12,13], m = 2, n = 3
输出: [1,2,6,7,11,12]
解析: 保留前(m = 2)个结点,  也就是以黑色节点表示的从链表头结点开始的结点(1 ->2).
删除接下来的(n = 3)个结点(3 -> 4 -> 5), 在图中以红色结点表示.
继续相同的操作, 直到链表的末尾.
返回删除结点之后的链表的头结点.
示例 2:



输入: head = [1,2,3,4,5,6,7,8,9,10,11], m = 1, n = 3
输出: [1,5,9]
解析: 返回删除结点之后的链表的头结点.
示例 3:

输入: head = [1,2,3,4,5,6,7,8,9,10,11], m = 3, n = 1
输出: [1,2,3,5,6,7,9,10,11]
示例 4:

输入: head = [9,3,7,7,9,10,8,2], m = 1, n = 2
输出: [9,7,8]


提示:

 1 <= 链表结点数 <= 10^4
[1 <= 链表的每一个结点值 <=10^6]
1 <= m,n <= 1000
'''
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
思路：链表 模拟
模拟题目中的要求，就地删除

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        head = ListNode(0, head)  # 添加1个哨兵，简化判断
        node = head
        while node:
            for i in range(m):
                node = node.next
                if not node:
                    break
            pre = node
            for i in range(n):
                if not node:
                    break
                node = node.next
            if pre:
                pre.next = node.next if node else None
        return head.next


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


def toList(listNode: ListNode):
    if listNode is None:
        return []
    else:
        li = []
        while listNode is not None:
            li.append(listNode.val)
            listNode = listNode.next
        return li


s = Solution()
print(toList(s.deleteNodes(fromList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), m=2, n=3)))
print(toList(s.deleteNodes(fromList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), m=1, n=3)))
print(toList(s.deleteNodes(fromList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), m=3, n=1)))
print(toList(s.deleteNodes(fromList([9, 3, 7, 7, 9, 10, 8, 2]), m=1, n=2)))
