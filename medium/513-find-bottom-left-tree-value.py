'''
找树左下角的值

给定一个二叉树，在树的最后一行找到最左边的值。

示例 1:

输入:

    2
   / \\
  1   3

输出:
1
 

示例 2:

输入:

        1
       / \\
      2   3
     /   / \\
    4   5   6
       /
      7

输出:
7
 

注意: 您可以假设树（即给定的根节点）不为 NULL。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：树 DFS
树的DFS遍历每一个节点如果当前节点深度高于以往遍历过的最深深度，更新值
时间复杂度：O(n)
空间复杂度：O(h)，h为树的高度
'''


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        maxdepth, ans = 0, 0

        def dfs(node, depth):
            nonlocal maxdepth, ans
            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)
            if not node.left and not node.right:
                if depth > maxdepth:
                    maxdepth = depth
                    ans = node.val

        dfs(root, 1)
        return ans
