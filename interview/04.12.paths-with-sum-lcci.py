'''
面试题 04.12. 求和路径
给定一棵二叉树，其中每个节点都含有一个整数数值(该值或正或负)。设计一个算法，打印节点数值总和等于某个给定值的所有路径的数量。
注意，路径不一定非得从二叉树的根节点或叶节点开始或结束，但是其方向必须向下(只能从父节点指向子节点方向)。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \\
            4   8
           /   / \\
          11  13  4
         /  \\    / \\
        7    2  5   1
返回:

3
解释：和为 22 的路径有：[5,4,11,2], [5,8,4,5], [4,11,7]
提示：

节点总数 <= 10000
'''
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
思路：递归 哈希
遍历树，用一个哈希表记录从根节点到当前节点的所有前缀和，
> 如果当前节点前缀和prefixSum为sum，则从根节点到当前节点的路径满足要求
> 如果prefixSum-sum在哈希表中存在，说明有某个子路径也满足要求

该题与 437.[路径总和 III](medium/437-path-sum-iii.py)相同

时间复杂度：O(n)
空间复杂度：O(h),h为树的高度
'''


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        counter = defaultdict(int)
        ans = 0

        def dfs(node, prefixSum):
            nonlocal ans
            prefixSum += node.val
            if prefixSum == targetSum:
                ans += 1
            if counter[prefixSum - targetSum] > 0:
                ans += counter[prefixSum - targetSum]
            counter[prefixSum] += 1
            if node.left:
                dfs(node.left, prefixSum)
            if node.right:
                dfs(node.right, prefixSum)
            counter[prefixSum] -= 1

        dfs(root, 0)
        return ans
