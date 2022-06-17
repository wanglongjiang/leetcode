'''
2074. 反转偶数长度组的节点
给你一个链表的头节点 head 。

链表中的节点 按顺序 划分成若干 非空 组，这些非空组的长度构成一个自然数序列（1, 2, 3, 4, ...）。一个组的 长度 就是组中分配到的节点数目。换句话说：

节点 1 分配给第一组
节点 2 和 3 分配给第二组
节点 4、5 和 6 分配给第三组，以此类推
注意，最后一组的长度可能小于或者等于 1 + 倒数第二组的长度 。

反转 每个 偶数 长度组中的节点，并返回修改后链表的头节点 head 。

 

示例 1：



输入：head = [5,2,6,3,9,1,7,3,8,4]
输出：[5,6,2,3,9,1,4,8,3,7]
解释：
- 第一组长度为 1 ，奇数，没有发生反转。
- 第二组长度为 2 ，偶数，节点反转。
- 第三组长度为 3 ，奇数，没有发生反转。
- 最后一组长度为 4 ，偶数，节点反转。
示例 2：



输入：head = [1,1,0,6]
输出：[1,0,1,6]
解释：
- 第一组长度为 1 ，没有发生反转。
- 第二组长度为 2 ，节点反转。
- 最后一组长度为 1 ，没有发生反转。
示例 3：



输入：head = [2,1]
输出：[2,1]
解释：
- 第一组长度为 1 ，没有发生反转。
- 最后一组长度为 1 ，没有发生反转。
 

提示：

链表中节点数目范围是 [1, 105]
0 <= Node.val <= 105
'''
from operator import length_hint
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
思路：模拟
模拟题目要求，递增子链表长度，获取子链表，如果子链表长度为奇数，不翻转，否则翻转。

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 1
        prevTailNode, nextNode = ListNode(), head
        while nextNode:
            subSize, subHead, subTail = 0, nextNode, None
            while nextNode and subSize < length:
                subTail = nextNode
                nextNode = nextNode.next
                subSize += 1
            if subSize % 2:  # 奇数子链表，直接连结
                prevTailNode = subTail
            else:  # 偶数子链表，翻转
                newHead, p = None, subHead
                while p != nextNode:
                    tmp = p.next
                    p.next = newHead
                    newHead = p
                    p = tmp
                prevTailNode.next = subTail
                prevTailNode = subHead
                prevTailNode.next = nextNode
            length += 1
        return head


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
print(toList(s.reverseEvenLengthGroups(fromList([1, 1, 0, 6, 5]))))
print(toList(s.reverseEvenLengthGroups(fromList([2, 1]))))
