'''
250. 统计同值子树
给定一个二叉树，统计该二叉树数值相同的子树个数。

同值子树是指该子树的所有节点都拥有相同的数值。

示例：

输入: root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \\  \
          5   5   5

输出: 4
'''

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：递归
递归遍历树，如果节点是叶子节点，该子树肯定是同值
如果节点不是叶子节点，且左右子树都是同值，且节点值与左右子树相同，则是同值

时间复杂度：O(n)
空间复杂度：O(h)
'''


class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        ans = 0

        def dfs(node: TreeNode) -> bool:  # 递归处理树，返回节点是否为同值
            nonlocal ans
            if not node.left and not node.right:
                ans += 1
                return True
            left, right = True, True
            if node.left:  # 判断与左子树是否同值
                left = dfs(node.left) and node.val == node.left.val
            if node.right:  # 判断与右子树是否同值
                right = dfs(node.right) and node.val == node.right.val
            if left and right:
                ans += 1
            return left and right

        dfs(root)
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


s = Solution()
null = None
print(s.countUnivalSubtrees(fromList([5, 1, 5, 5, 5, null, 5])))
