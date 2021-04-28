'''
二叉树的直径
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
注意：两结点之间的路径长度是以它们之间边的数目表示。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：递归
经过1个节点的直径为左子树最长路径+右子树最长路径，所以需要递归遍历所有的子树，返回自身最长子树的长度
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        maxLen = 0

        def lookup(node):
            nonlocal maxLen
            leftLen = 0
            if node.left:
                leftLen = 1 + lookup(node.left)
            rightLen = 0
            if node.right:
                rightLen = 1 + lookup(node.right)
            maxLen = max(maxLen, leftLen + rightLen)
            return max(leftLen, rightLen)

        lookup(root)
        return maxLen
