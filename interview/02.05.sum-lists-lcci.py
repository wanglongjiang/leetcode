'''
面试题 02.05. 链表求和
给定两个用链表表示的整数，每个节点包含一个数位。

这些数位是反向存放的，也就是个位排在链表首部。

编写函数对这两个整数求和，并用链表形式返回结果。

 

示例：

输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
输出：2 -> 1 -> 9，即912
进阶：思考一下，假设这些数位是正向存放的，又该如何解决呢?

示例：

输入：(6 -> 1 -> 7) + (2 -> 9 -> 5)，即617 + 295
输出：9 -> 1 -> 2，即912
'''

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
思路：链表
按照顺序节点相加，创建新的节点返回

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(0)  # 头部节点为哨兵
        l3 = ans
        carry = 0
        while l1 or l2 or carry:  # l1，l2及进位全部处理完才算完成
            val = carry  # 新节点的值从进位开始累加
            carry = 0
            if l1:
                val += l1.val  # 累加l1
            if l2:
                val += l2.val  # 累加l2
            if val >= 10:  # 如果需要进位，进行处理
                carry = 1
                val -= 10
            l3.next = ListNode(val)  # 创建节点
            l3 = l3.next  # 3个链表都指向下一个节点
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return ans.next


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
print(s.addTwoNumbers(fromList([5]), fromList([5])))
