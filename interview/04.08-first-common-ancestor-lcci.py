'''
面试题 04.08. 首个共同祖先
设计并实现一个算法，找出二叉树中某两个节点的第一个共同祖先。不得将其他的节点存储在另外的数据结构中。注意：这不一定是二叉搜索树。

例如，给定如下二叉树: root = [3,5,1,6,2,0,8,null,null,7,4]

    3
   / \\
  5   1
 / \\ / \\
6  2 0  8
  / \\
 7   4
示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。
'''

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
思路：DFS遍历
遍历树，分别找到p,q所在的路径，然后对比2个路径，最后一个相同的节点即为首个公共祖先

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path1, path2 = None, None

        def dfs(node, path: List):
            nonlocal path1, path2
            path.append(node)
            if node == p:
                path1 = path.copy()
            elif node == q:
                path2 = path.copy()
            if path1 and path2:
                return True
            if node.left:
                if dfs(node.left, path):
                    return True
            if node.right:
                if dfs(node.right, path):
                    return True
            path.pop()
            return False

        dfs(root, [])
        # 对比2个路径，找到最后一个相同节点
        i, n1, n2 = 0, len(path1), len(path2)
        while i < n1 and i < n2 and path1[i] == path2[i]:
            i += 1
        return path1[i - 1]


# list数据按照bfs遍历得到
def fromList(li: List[int]):
    if len(li) == 0:
        return None
    root = TreeNode(li[0])
    queue = [root]
    i = 1
    while i < len(li):
        node = queue[0]
        del queue[0]
        if li[i] is not None:
            node.left = TreeNode(li[i])
            queue.append(node.left)
        i += 1
        if i < len(li):
            if li[i]:
                node.right = TreeNode(li[i])
                queue.append(node.right)
            i += 1
    return root


s = Solution()
null = None
print(s.lowestCommonAncestor(fromList([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]), 5, 1))
