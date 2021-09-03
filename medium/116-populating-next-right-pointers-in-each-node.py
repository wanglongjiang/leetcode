'''
填充每个节点的下一个右侧节点指针

给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。
'''
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


"""
思路：BFS
这题天然应该用BFS解决，每层的节点出来后它右边的节点也就确定了
与117题类似

时间复杂度：O(n)
空间复杂度：O(n)
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q, nextq = deque(), deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node.left:
                nextq.append(node.left)
            if node.right:
                nextq.append(node.right)
            if not q:
                q, nextq = nextq, q
                prev = None
                for node in q:  # 遍历这一层所有的节点，设置next
                    if prev:
                        prev.next = node
                    prev = node
        return root
