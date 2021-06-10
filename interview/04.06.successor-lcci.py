'''
面试题 04.06. 后继者
设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）。

如果指定节点没有对应的“下一个”节点，则返回null。

示例 1:

输入: root = [2,1,3], p = 1

  2
 / \\
1   3

输出: 2
示例 2:

输入: root = [5,3,6,2,4,null,null,1], p = 6

      5
     / \\
    3   6
   / \\
  2   4
 /
1

输出: null
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
思路：
1. 先按照二叉树的性质和p的大小找到p
> 如果p大于node，则查找node.right
> 如果p小于node,则查找node.left

2. 找到p之后查找其右子树（如果有）的最左节点
> 用一个递归函数查找右子树的最小值，也就是刚刚大于p的节点
如果右子树不存在，向上找到将p作为左子树的第1个祖先节点


时间复杂度：O(h),h为树的高度
空间复杂度：O(h)
'''


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        ans = None

        def lookup(node):
            nonlocal ans
            if node.val > p.val:
                lookup(node.left)
                if not ans:  # p处于本节点的左子树，如果在p的右子树，或者p的上级中截止本节点之前未找到后续，则本节点为后续
                    ans = node
            elif node.val < p.val:
                lookup(node.right)
            else:
                if node.right:  # 如果p节点有右子树，找到右子树最小的节点
                    ans = lookupMin(node.right)

        def lookupMin(node):
            if node.left:
                return lookupMin(node.left)
            return node

        lookup(root)
        return ans
