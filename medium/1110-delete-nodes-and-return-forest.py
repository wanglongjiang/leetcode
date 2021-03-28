'''
删点成林
给出二叉树的根节点 root，树上每个节点都有一个不同的值。

如果节点值在 to_delete 中出现，我们就把该节点从树上删去，最后得到一个森林（一些不相交的树构成的集合）。

返回森林中的每棵树。你可以按任意顺序组织答案。
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：dfs+哈希表
1、用dfs遍历树，将树的val:(node,parent)放入哈希表
2、遍历to_delete，从哈希表中取出待删除的节点，将其从父节点中删除，同时将其左右子树加入结果中
时间复杂度：O(m+n)，m为树的节点数，n为待删除节点
空间复杂度：O(m)
'''


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []
        d = {}

        # 遍历树
        def dfs(node):
            if node.left:
                d[node.left.val] = (node.left, node)
                dfs(node.left)
            if node.right:
                d[node.right.val] = (node.right, node)
                dfs(node.right)

        dfs(root)
        d[root.val] = (root, None)
        # 执行删除
        ans = set()
        ans.add(root)
        for val in to_delete:
            node, parent = d[val]
            # 从原树中删除
            if node in ans:
                ans.remove(node)
            if parent:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
            # 将子树加入结果
            if node.left:
                ans.add(node.left)
            if node.right:
                ans.add(node.right)
        return list(ans)


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
print(s.delNodes(fromList([1, 2, 3, 4, 5, 6, 7]), [3, 5]))
print(s.delNodes(fromList([1, 2, 3, null, null, null, 4]), [2, 1]))
