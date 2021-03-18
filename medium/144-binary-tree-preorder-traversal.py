'''
二叉树的前序遍历
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路，按照前序进行遍历。先父节点，然后左、右
时间复杂度：O(n)
空间复杂度：O(logn)，需要logn层的递归深度，最坏情况下O(n)
'''


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []

        def preorder(node):
            ans.append(node.val)
            if node.left:
                preorder(node.left)
            if node.right:
                preorder(node.right)

        if root:
            preorder(root)
        return ans
