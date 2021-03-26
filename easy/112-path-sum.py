'''
路径总和
给你二叉树的根节点 root 和一个表示目标和的整数 targetSum ，判断该树中是否存在 根节点到叶子节点 的路径，
这条路径上所有节点值相加等于目标和 targetSum 。

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
思路：就是遍历啊
'''


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def dfs(node, target):
            if node.val == target and not node.right and not node.left:
                return True
            if node.left:
                if dfs(node.left, target - node.val):
                    return True
            if node.right:
                if dfs(node.right, target - node.val):
                    return True
            return False

        if not root:
            return targetSum == 0
        return dfs(root, targetSum)


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
print(s.hasPathSum(root=fromList([5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1]), targetSum=22))
print(s.hasPathSum(root=fromList([1, 2, 3]), targetSum=5))
print(s.hasPathSum(root=fromList([1, 2]), targetSum=0))
