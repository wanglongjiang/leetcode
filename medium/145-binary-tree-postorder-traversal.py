'''
二叉树的后序遍历
给定一个二叉树，返回它的 后序 遍历。
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：后序遍历。先左，中间右，最后自身
时间复杂度：O(n)
空间复杂度：O(logn)，需要logn层的递归深度，最坏情况下O(n)
'''


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []

        def postorder(node):
            if node.left:
                postorder(node.left)
            if node.right:
                postorder(node.right)
            ans.append(node.val)

        if root:
            postorder(root)
        return ans
