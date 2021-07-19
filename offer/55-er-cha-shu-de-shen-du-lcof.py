'''
剑指 Offer 55 - I. 二叉树的深度

输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：

给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \\
  9  20
    /  \\
   15   7
返回它的最大深度 3 。

 

提示：

节点总数 <= 10000
注意：本题与主站 104 题相同：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
思路：DFS
时间复杂度：O(n)
空间复杂度：O(h)
'''


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.maxDep = 0

        def recursion(node: TreeNode, depth: int):
            self.maxDep = max(self.maxDep, depth)
            if node.left:
                recursion(node.left, depth + 1)
            if node.right:
                recursion(node.right, depth + 1)

        recursion(root, 1)
        return self.maxDep
