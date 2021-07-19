'''
面试题 04.05. 合法二叉搜索树
实现一个函数，检查一棵二叉树是否为二叉搜索树。

示例 1:
输入:
    2
   / \\
  1   3
输出: true
示例 2:
输入:
    5
   / \\
  1   4
     / \\
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
思路：递归
按照树的前序算法遍历验证
1、验证节点与左右节点的大小关系是否正确
2、验证节点与左右所有子节点大小关系是否正确，向递归过程传递当前子树最大值和最小值

此题与 - 98.[验证二叉搜索树](medium/98-validate-binary-search-tree.py) 相同

时间复杂度：O(n)
空间复杂度：O(h)，h为树的高度
'''


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def recursion(node: TreeNode, lower=float('-inf'), upper=float('inf')):
            if node is None:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            if not recursion(node.right, node.val, upper):
                return False
            if not recursion(node.left, lower, node.val):
                return False
            return True

        return recursion(root)
