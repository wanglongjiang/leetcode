'''
路径总和 III

给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

'''
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：递归 哈希
遍历树，用一个哈希表记录从根节点到当前节点的所有前缀和，
> 如果当前节点前缀和prefixSum为sum，则从根节点到当前节点的路径满足要求
> 如果prefixSum-sum在哈希表中存在，说明有某个子路径也满足要求

该题与 面试题 04.12. [求和路径](interview/04.12.paths-with-sum-lcci.py)相同

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
