'''
把二叉搜索树转换为累加树
给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），
使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。

提醒一下，二叉搜索树满足下列约束条件：

节点的左子树仅包含键 小于 节点键的节点。
节点的右子树仅包含键 大于 节点键的节点。
左右子树也必须是二叉搜索树。

提示：

树中的节点数介于 0 和 104 之间。
每个节点的值介于 -104 和 104 之间。
树中的所有值 互不相同 。
给定的树为二叉搜索树。
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
从题目中可以了解到累加树的定义，一个节点的值是其原树中大于等于其node.val的值之和
也就是如果节点是上级的右子树，其和为node.val+右子树的累加+祖父节点累加
如果节点是上级的左子树，其和为node.val+右子树累计+父节点累计
根据上面的信息可以写出递归函数
时间复杂度：O(n)，所有节点都需要遍历一次
空间复杂度：O(logn)，递归深度为logn
'''


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def recu(node: TreeNode, parentSum):
            if node.right:
                node.val += recu(node.right, parentSum)
            else:
                node.val += parentSum
            if node.left:
                return recu(node.left, node.val)
            return node.val

        if root:
            recu(root, 0)
        return root


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


def toList(node: TreeNode):
    li = []
    if node is None:
        return li
    queue = [node]
    li.append(node.val)
    while len(queue) > 0:
        node = queue[0]
        del queue[0]
        if node.left:
            queue.append(node.left)
            li.append(node.left.val)
        else:
            li.append(None)
        if node.right:
            queue.append(node.right)
            li.append(node.right.val)
        else:
            li.append(None)

    # 删掉末尾的null
    i = len(li) - 1
    while i > 0:
        if li[i] is None:
            del li[i]
        else:
            break
        i -= 1
    return li


s = Solution()
null = None
print(toList(s.convertBST(fromList([4, 1, 6, 0, 2, 5, 7, null, null, null, 3, null, null, null, 8]))))
print(toList(s.convertBST(fromList([0, null, 1]))))
print(toList(s.convertBST(fromList([1, 0, 2]))))
print(toList(s.convertBST(fromList([3, 2, 4, 1]))))
