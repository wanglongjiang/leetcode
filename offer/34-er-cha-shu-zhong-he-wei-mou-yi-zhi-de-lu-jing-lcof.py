'''
剑指 Offer 34. 二叉树中和为某一值的路径

输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

 

示例:
给定如下二叉树，以及目标和 target = 22，

              5
             / \\
            4   8
           /   / \\
          11  13  4
         /  \\    / \\
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
 

提示：

节点总数 <= 10000
注意：本题与主站 113 题相同：https://leetcode-cn.com/problems/path-sum-ii/
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：DFS
时间复杂度：O(n)
空间复杂度：O(logn)
'''


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ans = []
        comb = []

        def dfs(node, target):
            comb.append(node.val)
            if node.val == target and not node.right and not node.left:
                ans.append(comb.copy())
            if node.left:
                dfs(node.left, target - node.val)
            if node.right:
                dfs(node.right, target - node.val)
            comb.pop()

        if root:
            dfs(root, targetSum)
        return ans
