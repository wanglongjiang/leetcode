'''
382. 链表随机节点
给定一个单链表，随机选择链表的一个节点，并返回相应的节点值。保证每个节点被选的概率一样。

进阶:
如果链表十分大且长度未知，如何解决这个问题？你能否使用常数级空间复杂度实现？

示例:

// 初始化一个单链表 [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom()方法应随机返回1,2,3中的一个，保证每个元素被返回的概率相等。
solution.getRandom();
'''

import random


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
思路：随机 水塘抽样
设一个指针p，初始指向head，每次执行getRandom，随机前进k步(k小于13)，如果遇到队尾，将队尾与队头连结起来。
返回随机的节点值

2个操作的时间复杂度都是O(1)，空间复杂度O(1)
'''


class Solution:
    def __init__(self, head: ListNode):
        self.head = head
        self.p = head

    def getRandom(self) -> int:
        k = random.randint(1, 13)
        while k:
            if not self.p.next:
                self.p.next = self.head
            self.p = self.p.next
            k -= 1
        return self.p.val
