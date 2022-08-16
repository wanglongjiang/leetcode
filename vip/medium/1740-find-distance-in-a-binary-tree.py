'''
1740. 找到二叉树中的距离
给定一棵二叉树的根节点 root 以及两个整数 p 和 q ，返回该二叉树中值为 p 的结点与值为 q 的结点间的 距离 。

两个结点间的 距离 就是从一个结点到另一个结点的路径上边的数目。



示例 1：


输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 0
输出：3
解释：在 5 和 0 之间有 3 条边：5-3-1-0
示例 2：


输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 7
输出：2
解释：在 5 和 7 之间有 2 条边：5-2-7
示例 3：


输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 5
输出：0
解释：一个结点与它本身之间的距离为 0


提示：

树中结点个数的范围在 [1, 10^4].
0 <= Node.val <= 10^9
树中所有结点的值都是唯一的.
p 和q 是树中结点的值.
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：树的递归遍历
检查左子树中是否有某个节点，
再检查右子树中是否有另外一个节点，
如果2者都有，同时距离未被设置，需要设置结果。
如果只有2者之一，返回与某个节点的距离。

时间复杂度：O(n)
空间复杂度：O(h)
'''


class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        if p == q:
            return 0
        ans = 0

        def find(node, h):
            nonlocal ans
            if node.val == p or node.val == q:  # 当前节点是p,q之一，检查左右子树
                if node.left:
                    leftHeight = find(node.left, h + 1)
                    if leftHeight:  # 子树中有节点，距离是当前节点到子树中节点的距离
                        ans = leftHeight - h
                if not ans and node.right:
                    rightHeight = find(node.right, h + 1)
                    if rightHeight:  # 子树中有节点，距离是当前节点到子树中节点的距离
                        ans = rightHeight - h
                return h
            else:  # 当前节点不是节点之一，检查左右子树中是否有节点
                leftHeight, rightHeight = 0, 0
                if node.left:
                    leftHeight = find(node.left, h + 1)
                if not ans and node.right:
                    rightHeight = find(node.right, h + 1)
                if not ans and leftHeight and rightHeight:  # 左右子树中分别有2个节点，距离是当前节点到2个子节点距离之和
                    ans = leftHeight - h + rightHeight - h
                if leftHeight or rightHeight:
                    return leftHeight if leftHeight else rightHeight
                return 0

        find(root, 0)
        return ans


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
            if li[i] is not None:
                node.right = TreeNode(val=li[i])
                queue.append(node.right)
            i += 1
    return root


null = None
s = Solution()
print(s.findDistance(root=fromList([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]), p=5, q=0))
print(s.findDistance(root=fromList([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]), p=5, q=7))
print(s.findDistance(root=fromList([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]), p=5, q=5))
