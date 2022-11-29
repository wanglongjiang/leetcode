'''
2487. 从链表中移除节点
中等
10
相关企业
给你一个链表的头节点 head 。

对于列表中的每个节点 node ，如果其右侧存在一个具有 严格更大 值的节点，则移除 node 。

返回修改后链表的头节点 head 。

 

示例 1：



输入：head = [5,2,13,3,8]
输出：[13,8]
解释：需要移除的节点是 5 ，2 和 3 。
- 节点 13 在节点 5 右侧。
- 节点 13 在节点 2 右侧。
- 节点 8 在节点 3 右侧。
示例 2：

输入：head = [1,1,1,1]
输出：[1,1,1,1]
解释：每个节点的值都是 1 ，所以没有需要移除的节点。
 

提示：

给定列表中的节点数目在范围 [1, 105] 内
1 <= Node.val <= 105
'''
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
[TOC]

# 思路
单调栈

# 解题方法
设一个单调栈，栈内元素单调递减

遍历链表，如果当前节点值大于栈顶元素，将所有小于当前节点的栈内元素出栈，然后将当前元素入栈

最后将栈内元素依次链接起来

# 复杂度
- 时间复杂度: 
> $O(n)$ 

- 空间复杂度: 
> $O(n)$
'''


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stk = []
        while head:
            while stk and stk[-1].val < head.val:
                stk.pop()
            stk.append(head)
            head = head.next
        for i in range(len(stk) - 1):
            stk[i].next = stk[i + 1]
        stk[-1].next = None
        return stk[0]


def fromList(li: int):
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
