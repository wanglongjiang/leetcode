'''
剑指 Offer 26. 树的子结构
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \\
   4   5
  / \\
 1   2
给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：

输入：A = [1,2,3], B = [3,1]
输出：false
示例 2：

输入：A = [3,4,5,1,2], B = [4,1]
输出：true
限制：

0 <= 节点个数 <= 10000
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
思路：递归
1. 递归在A中查找B的根节点，如果能找到，进入2
2. 递归对比2个子树的每个节点是否相同

该题与 面试题 04.10.[检查子树](interview/04.10.check-subtree-lcci.py)类似

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False

        def lookup(node):
            if node.val == B.val:
                return comp(node, B)
            if node.left:
                if lookup(node.left):
                    return True
            if node.right:
                if lookup(node.right):
                    return True
            return False

        def comp(node1, node2):
            if node1.val != node2.val:
                return False
            if node1.left and node2.right:
                if not comp(node1.left, node2.left):
                    return False
            elif node1.left or node2.left:
                return False
            if node1.right and node2.right:
                if not comp(node1.right, node2.right):
                    return False
            elif node1.right or node2.right:
                return False
            return True

        return lookup(A)
