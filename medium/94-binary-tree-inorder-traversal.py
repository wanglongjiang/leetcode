'''
二叉树的中序遍历
给定一个二叉树的根节点 root ，返回它的 中序 遍历。
'''
from typing import List
'''
思路：树的遍历
迭代算法需要使用栈
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归算法
class Solution1:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []

        def recursion(node: TreeNode):
            if node.left:
                recursion(node.left)
            ans.append(node.val)
            if node.right:
                recursion(node.right)

        if root:
            recursion(root)
        return ans


# 迭代算法
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        while len(stack) > 0 or root is not None:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ans.append(root.val)
            root = root.right
        return ans


s = Solution()
print(s.inorderTraversal())
