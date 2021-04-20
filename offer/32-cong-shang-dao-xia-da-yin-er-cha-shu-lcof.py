'''
剑指 Offer 32 - I. 从上到下打印二叉树
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
思路：BFS遍历树
广度优先遍历树，使用队列保存待遍历的节点
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans
        from collections import deque
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            ans.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return ans
