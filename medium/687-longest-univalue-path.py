'''
最长同值路径
给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。
注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：递归
递归计算与当前节点同值的边长度，
    如果左子树与当前节点同值，leftLen += dfs(left)+1
    如果右子树与当前节点同值，rightLen += dfs(right)+1
    当前同值路径长度为：pathLen = max(parentLen + leftLen, parentLen + rightLen, leftLen + rightLen)
时间复杂度：O(n)
空间复杂度：O(logn)
'''


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        maxLen = 0

        def dfs(node: TreeNode, parentLen):
            nonlocal maxLen
            leftLen = 0
            if node.left:
                if node.val == node.left.val:  # 如果左子树根节点与当前节点同值，路径长度累加
                    leftLen += dfs(node.left, parentLen + 1) + 1
                else:  # 如果子树节点与当前节点不同值，单点计算子树的同值长度
                    dfs(node.left, 0)
            rightLen = 0
            if node.right:
                if node.val == node.right.val:  # 如果右子树根节点与当前节点同值，路径长度累加
                    rightLen += dfs(node.right, parentLen + 1) + 1
                else:  # 如果子树节点与当前节点不同值，单点计算子树的同值长度
                    dfs(node.right, 0)
            pathLen = max(parentLen + leftLen, parentLen + rightLen, leftLen + rightLen)
            if pathLen > maxLen:  # 如果当前同值路径超过最大长度，更新最大长度
                maxLen = pathLen
            return max(leftLen, rightLen)

        dfs(root, 0)
        return maxLen


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
print(s.longestUnivaluePath(fromList([1, null, 1, 1, 1, 1, 1, 1])))
