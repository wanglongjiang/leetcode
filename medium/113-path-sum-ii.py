'''
路径总和 II
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

叶子节点 是指没有子节点的节点。
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：还是深度遍历
时间复杂度：O(n)
空间复杂度：O(logn)
'''


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ans = []
        comb = []

        def dfs(node, target):
            comb.append(node.val)
            if node.val == target and not node.right and not node.left:
                ans.append(comb.copy())
            if node.left:
                dfs(node.left, target - node.val)
            if node.right:
                dfs(node.right, target - node.val)
            comb.pop()

        if root:
            dfs(root, targetSum)
        return ans


# list数据按照bfs遍历得到
def fromList(li: List[int]):
    if len(li) == 0:
        return None
    root = TreeNode(val=li[0])
    queue = [root]
    i = 1
    while i < len(li):
        node = queue[0]
        del queue[0]
        if li[i]:
            node.left = TreeNode(val=li[i])
            queue.append(node.left)
        i += 1
        if i < len(li):
            if li[i]:
                node.right = TreeNode(val=li[i])
                queue.append(node.right)
            i += 1
    return root


s = Solution()
null = None
print(s.pathSum(fromList([5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1]), 22))
print(s.pathSum(fromList([1, 2, 3]), 5))
print(s.pathSum(fromList([1, 2]), 0))
