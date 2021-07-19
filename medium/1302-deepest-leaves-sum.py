'''
层数最深叶子节点的和

给你一棵二叉树的根节点 root ，请你返回 层数最深的叶子节点的和 。

 

示例 1：



输入：root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
输出：15
示例 2：

输入：root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
输出：19
 

提示：

树中节点数目在范围 [1, 10^4] 之间。
1 <= Node.val <= 100
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
递归进入树的最底层，合计叶子节点的和。如果树的深度变大，将以往的和抛弃，重新计算。

时间复杂度：O(n)
空间复杂度：O(h),h为树的高度
'''


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        ans, maxdepth = 0, 0

        def dfs(node, depth):
            nonlocal ans, maxdepth
            if not node.left and not node.right:
                if depth == maxdepth:
                    ans += node.val
                elif depth > maxdepth:
                    maxdepth = depth
                    ans = node.val
            else:
                if node.left:
                    dfs(node.left, depth + 1)
                if node.right:
                    dfs(node.right, depth + 1)

        dfs(root, 1)
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
            if li[i]:
                node.right = TreeNode(val=li[i])
                queue.append(node.right)
            i += 1
    return root


s = Solution()
null = None
print(s.deepestLeavesSum(fromList([1, 2, 3, 4, 5, null, 6, 7, null, null, null, null, 8])))
print(s.deepestLeavesSum(fromList([6, 7, 8, 2, 7, 1, 3, 9, null, 1, 4, null, null, null, 5])))
