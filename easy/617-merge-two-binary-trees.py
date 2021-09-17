'''
合并二叉树
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：递归
递归处理每个节点，节点的值相加
左/右节点如果有1个为空，将左/右节点设置为非空的那个
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val  # 直接修改root1返回
        if root1.left and root2.left:
            root1.left = self.mergeTrees(root1.left, root2.left)
        else:
            root1.left = root1.left if root1.left else root2.left
        if root1.right and root2.right:
            root1.right = self.mergeTrees(root1.right, root2.right)
        else:
            root1.right = root1.right if root1.right else root2.right
        return root1
