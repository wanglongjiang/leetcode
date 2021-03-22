'''
从前序与中序遍历序列构造二叉树
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。
例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
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
前序的第1个字符为根节点，中序的根节点在第i个，那么前序的1..i，中序的0..i-1为左子树，
i+1..n为右子树，根据以上特征，可以递归的生成子树
时间复杂度：O(nlogn)，对inorder要进行n*logn次遍历
空间复杂度：O(logn)，不考虑返回结果，递归占用O(logn)空间
'''


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def makeTree(pStart, pEnd, iStart, iEnd):
            rootVal = preorder[pStart]
            root = TreeNode(rootVal)
            i = inorder.index(rootVal, iStart, iEnd)
            if i > iStart:  # 中序左边有左子树的输出，说明有右子树
                root.left = makeTree(pStart + 1, pStart + 1 + i - iStart, iStart, i)
            if i + 1 < iEnd:  # 中序右边有右子树的输出，说明有右子树
                root.right = makeTree(pStart + 1 + i - iStart, pEnd, i + 1, iEnd)
            return root

        return makeTree(0, len(preorder), 0, len(inorder)) if preorder else None
