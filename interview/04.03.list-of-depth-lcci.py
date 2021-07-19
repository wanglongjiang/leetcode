'''
面试题 04.03. 特定深度节点链表
给定一棵二叉树，设计一个算法，创建含有某一深度上所有节点的链表（比如，若一棵树的深度为 D，则会创建出 D 个链表）。
返回一个包含所有深度的链表的数组。

 

示例：

输入：[1,2,3,4,5,null,7,8]

        1
       /  \\
      2    3
     / \\    \\
    4   5    7
   /
  8

输出：[[1],[2,3],[4,5,7],[8]]
'''
from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
思路：BFS 队列
用BFS遍历树，将每一层的节点串联为一个链表

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        ans = []
        head = ListNode(0)
        prev = head
        ans.append(head)
        # BFS遍历树
        q, nextq = deque(), deque()
        q.append(tree)
        while q:
            node = q.popleft()
            prev.next = ListNode(node.val)
            prev = prev.next
            if node.left:
                nextq.append(node.left)
            if node.right:
                nextq.append(node.right)
            if not q:
                q, nextq = nextq, q
                ans[-1] = head.next
                ans.append(head)
                prev = head
        ans.pop()
        return ans
