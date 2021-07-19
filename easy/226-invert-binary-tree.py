'''
翻转二叉树
翻转一棵二叉树。

示例：

输入：

     4
   /   \\
  2     7
 / \\   / \\
1   3 6   9
输出：

     4
   /   \\
  7     2
 / \\   / \\
9   6 3   1
备注:
这个问题是受到 Max Howell 的 原问题 启发的 ：

谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：递归
用一个递归函数，直接在原数据结构上交换左右子树

时间复杂度：O(n)
'''


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        root.left, root.right = root.right, root.left
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        return root
