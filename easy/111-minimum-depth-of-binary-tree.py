'''
二叉树的最小深度
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明：叶子节点是指没有子节点的节点。
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
    def minDepth(self, root: TreeNode) -> int:
        mind = float('inf')

        def dfs(node, level):
            nonlocal mind
            if mind <= level:
                return True
            if node.left or node.right:
                if node.left:
                    if dfs(node.left, level + 1):
                        return True
                if node.right:
                    if dfs(node.right, level + 1):
                        return True
            else:
                mind = min(mind, level)
            return False

        if not root:
            return 0
        dfs(root, 1)
        return mind


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
print(s.minDepth(fromList([3, 9, 20, null, null, 15, 7])))
print(s.minDepth(fromList([2, null, 3, null, 4, null, 5, null, 6])))
