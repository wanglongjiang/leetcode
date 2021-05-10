'''
叶子相似的树

请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。



举个例子，如上图所示，给定一棵叶值序列为 (6, 7, 4, 9, 8) 的树。

如果有两棵二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。

如果给定的两个根结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。

 

示例 1：
输入：root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
输出：true
示例 2：

输入：root1 = [1], root2 = [1]
输出：true
示例 3：

输入：root1 = [1], root2 = [2]
输出：false
示例 4：

输入：root1 = [1,2], root2 = [2,2]
输出：true

示例 5：

输入：root1 = [1,2,3], root2 = [1,3,2]
输出：false
 

提示：

给定的两棵树可能会有 1 到 200 个结点。
给定的两棵树上的值介于 0 到 200 之间。
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：中序遍历
使用递归中序遍历树，将叶节点输出到结果中
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node, leaf):
            if not node.left and not node.right:
                leaf.append(node.val)
            else:
                if node.left:
                    dfs(node.left, leaf)
                if node.right:
                    dfs(node.right, leaf)

        leaf1, leaf2 = [], []
        dfs(root1, leaf1)
        dfs(root2, leaf2)
        return leaf1 == leaf2


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
        if li[i] is not None:
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
print(s.leafSimilar(fromList([3, 5, 1, 6, 2, 9, 8, null, null, 7, 4]), fromList([3, 5, 1, 6, 7, 4, 2, null, null, null, null, null, null, 9, 8])))
print(s.leafSimilar(fromList([1]), fromList([1])))
print(s.leafSimilar(fromList([1]), fromList([2])))
print(s.leafSimilar(fromList([1, 2]), fromList([2, 2])))
print(s.leafSimilar(fromList([1, 2, 3]), fromList([1, 3, 2])))
