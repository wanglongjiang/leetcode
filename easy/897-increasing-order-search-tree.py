'''
递增顺序搜索树
给你一棵二叉搜索树，请你 按中序遍历 将其重新排列为一棵递增顺序搜索树，
使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。
'''

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：后序遍历树
对于每个节点，先将右子树展开，返回值连结变成本节点的右节点
然后展开左子树，并将自身传入左子树展开过程，连结到右子树的尾部
时间复杂度：O(n)
空间复杂度：O(n)，最坏情况下堆栈深度为n
'''


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def recu(node, greatParent):
            if node.right:
                node.right = recu(node.right, greatParent)
            else:
                node.right = greatParent
            if node.left:
                left = node.left
                node.left = None
                return recu(left, node)
            else:
                return node

        return recu(root, None)


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
print(s.increasingBST(fromList([5, 3, 6, 2, 4, null, 8, 1, null, null, null, 7, 9])))
