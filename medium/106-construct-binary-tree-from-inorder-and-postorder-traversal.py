'''
从中序与后序遍历序列构造二叉树
根据一棵树的中序遍历与后序遍历构造二叉树。
例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \\
  9  20
    /  \\
   15   7
'''
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：递归遍历树。
后序序的最后1个(第n个)字符为根节点，中序的根节点在第i个，那么后序的i..n-1，中序的i+1..n为右子树，
0..i-1为左子树，根据以上特征，可以递归的生成子树
时间复杂度：O(nlogn)，对inorder要进行n*logn次遍历
空间复杂度：O(logn)，不考虑返回结果，递归占用O(logn)空间
'''


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def makeTree(pStart, pEnd, iStart, iEnd):
            rootVal = postorder[pEnd]
            root = TreeNode(rootVal)
            i = inorder.index(rootVal, iStart, iEnd + 1)
            if i > iStart:  # 中序左边有左子树的输出，说明有左子树
                root.left = makeTree(pStart, pStart + i - iStart - 1, iStart, i - 1)
            if i < iEnd:  # 中序右边有右子树的输出，说明有右子树
                root.right = makeTree(pStart + i - iStart, pEnd - 1, i + 1, iEnd)
            return root

        return makeTree(0, len(postorder) - 1, 0, len(inorder) - 1) if postorder else None
