'''
二叉树的最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。
'''

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：递归搜索
递归搜索树每深入1层加1，同时设置1个变量，记录最大深度
'''


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.maxDep = 0

        def recursion(node: TreeNode, depth: int):
            self.maxDep = max(self.maxDep, depth)
            if node.left:
                recursion(node.left, depth + 1)
            if node.right:
                recursion(node.right, depth + 1)

        recursion(root, 1)
        return self.maxDep


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
print(s.maxDepth(fromList([3, 9, 20, null, null, 15, 7])))
