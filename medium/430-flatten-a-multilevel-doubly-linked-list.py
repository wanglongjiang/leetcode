'''
扁平化多级双向链表
多级双向链表中，除了指向下一个节点和前一个节点指针之外，它还有一个子链表指针，可能指向单独的双向链表。
这些子列表也可能会有一个或多个自己的子项，依此类推，生成多级数据结构，如下面的示例所示。

给你位于列表第一级的头节点，请你扁平化列表，使所有结点出现在单级双链表中。
'''


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


'''
思路：栈，链表操作
遇到有字节点的节点，将当前节点的下一节点入栈，然后将当前节点的下一节点设置为子节点
如果当前节点没有下一节点，从栈中取出节点作为下一节点
时间复杂度：O(n)
空间复杂度：O(n)，最坏情况下节点有1个字节点和右节点
'''


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        stack = []
        node = head
        prev = None
        while node or stack:
            while node and node.child is None:  # 跳过没有子节点的节点
                prev = node
                node = node.next
            if node and node.child:  # 如果有子节点，将子节点设置为下一节点，原下一节点入栈
                if node.next:
                    stack.append(node.next)
                node.next = node.child
                node.next.prev = node
                node.child = None
            if not node and stack:  # 当前节点为空，需要从栈中恢复上一层的下一节点继续
                node = stack.pop()
                prev.next = node
                node.prev = prev
        return head
