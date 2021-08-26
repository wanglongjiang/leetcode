'''
117. 填充每个节点的下一个右侧节点指针 II
给定一个二叉树

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。



进阶：

你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。


示例：



输入：root = [1,2,3,4,5,null,7]
输出：[1,#,2,3,#,4,5,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
序列化输出按层序遍历顺序（由 next 指针连接），'#' 表示每层的末尾。


提示：

树中的节点数小于 6000
-100 <= node.val <= 100
'''
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


'''
思路：BFS
这题天然应该用BFS解决，每层的节点出来后它右边的节点也就确定了

时间复杂度：O(n)
空间复杂度：O(n)
'''


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
