'''
二叉树的右视图
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：树的遍历，栈
用1个栈vstack存放能看到的部分
按照父->右->左的顺序遍历树，用栈tstack保存需要遍历的节点。
当栈tstack的高度超过vstack时，高出的元素能看到，需要将其入vstack。
树遍历完成后，输出vstack。
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        vstack = []
        tstack = []

        def each(node):
            tstack.append(node.val)
            if len(tstack) > len(vstack):
                vstack.append(tstack[-1])
            if node.right:
                each(node.right)
            if node.left:
                each(node.left)
            tstack.pop()

        each(root)
        return vstack
