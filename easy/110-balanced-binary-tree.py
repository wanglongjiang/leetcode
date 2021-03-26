'''
平衡二叉树
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：递归遍历所有的分支，记录最低高度、最高高度。二者之差如果大于1则返回False
时间复杂度：O(n)
空间复杂度：O(logn)
'''


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        minHeight, maxHeight = float('inf'), float('-inf')

        def dfs(node, h):
            nonlocal minHeight
            nonlocal maxHeight
            if node.left:
                if not dfs(node.left, h + 1):
                    return False
            else:
                minHeight = min(h, minHeight)
                maxHeight = max(h, maxHeight)
                if maxHeight - minHeight > 1:
                    return False
            if node.right:
                if not dfs(node.right, h + 1):
                    return False
            else:
                minHeight = min(h, minHeight)
                maxHeight = max(h, maxHeight)
                if maxHeight - minHeight > 1:
                    return False
            return True

        if not root:
            return True
        return dfs(root, 1)


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
print(s.isBalanced(fromList([3, 9, 20, None, None, 15, 7])))
