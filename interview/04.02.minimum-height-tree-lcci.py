'''
面试题 04.02. 最小高度树
给定一个有序整数数组，元素各不相同且按升序排列，编写一个算法，创建一棵高度最小的二叉搜索树。

示例:
给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

          0
         / \\
       -3   9
       /   /
     -10  5
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
思路：分治
1. 取数组中点元素为子树根节点
2. 中点左边的子数组递归处理为左子树
3. 中点右边的子数组递归处理为右子树
4. 重复上面1.2.3直至子数组长度为0

时间复杂度：O(n)
空间复杂度：O(logn)
'''


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def dc(start, end):
            mid = (start + end) // 2 + (start + end) % 2
            node = TreeNode(nums[mid])
            if mid > start:
                node.left = dc(start, mid - 1)
            if mid < end:
                node.right = dc(mid + 1, end)
            return node

        return dc(0, len(nums) - 1)
