'''
找出克隆二叉树中的相同节点
给你两棵二叉树，原始树 original 和克隆树 cloned，以及一个位于原始树 original 中的目标节点 target。

其中，克隆树 cloned 是原始树 original 的一个 副本 。

请找出在树 cloned 中，与 target 相同 的节点，并返回对该节点的引用（在 C/C++ 等有指针的语言中返回 节点指针，其他语言返回节点本身）。

 

注意：

你 不能 对两棵二叉树，以及 target 节点进行更改。
只能 返回对克隆树 cloned 中已有的节点的引用。
进阶：如果树中允许出现值相同的节点，你将如何解答？
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
思路：递归
同时递归遍历2棵树，如果找到了原树中的节点，也就找到了cloned树中的节点。

时间复杂度：O(n)
空间复杂度：O(h)，h为树的高度
'''


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original == target:
            return cloned
        if original.left:
            t = self.getTargetCopy(original.left, cloned.left, target)
            if t:
                return t
        if original.right:
            t = self.getTargetCopy(original.right, cloned.right, target)
            if t:
                return t
        return None
