'''
将有序数组转换为二叉搜索树
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。

高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。
'''
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：递归创建树。
时间复杂度：O(n)
空间复杂度：O(logn)，递归需要的空间
'''


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def makeTree(start, end):
            if start == end:
                return None
            if end - start == 1:
                return TreeNode(nums[start])
            if end - start == 2:
                return TreeNode(nums[start + 1], TreeNode(nums[start]))
            if end - start == 3:
                return TreeNode(nums[start + 1], TreeNode(nums[start]), TreeNode(nums[start + 2]))
            mid = (start + end) // 2
            return TreeNode(nums[mid], makeTree(start, mid), makeTree(mid + 1, end))

        return makeTree(0, len(nums))
