'''
1644. 二叉树的最近公共祖先 II
给定一棵二叉树的根节点 root，返回给定节点 p 和 q 的最近公共祖先（LCA）节点。
如果 p 或 q 之一不存在于该二叉树中，返回 null。树中的每个节点值都是互不相同的。

根据维基百科中对最近公共祖先节点的定义：
“两个节点 p 和 q 在二叉树 T 中的最近公共祖先节点是后代节点中既包括 p 又包括 q 的最深节点（我们允许一个节点为自身的一个后代节点）”。
一个节点 x 的后代节点是节点 x 到某一叶节点间的路径中的节点 y。



示例 1:


输入： root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出： 3
解释： 节点 5 和 1 的共同祖先节点是 3。
示例 2:



输入： root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出： 5
解释： 节点 5 和 4 的共同祖先节点是 5。根据共同祖先节点的定义，一个节点可以是自身的后代节点。
示例 3:



输入： root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 10
输出： null
解释： 节点 10 不存在于树中，所以返回 null。


提示:

树中节点个数的范围是 [1, 104]。
-10^9 <= Node.val <= 10^9
所有节点的值 Node.val 是互不相同的。
p != q
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


'''
思路：树 递归

递归处理每个节点，查找当前节点，左右子树节点在p,q相同的数量，如果当前节点+左右子树中的节点数=2，则找到了最近公共子节点。

时间复杂度：O(n)
空间复杂度：O(h)，h为树的高度
'''


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None

        def count(node):
            nonlocal ans
            cnt = 1 if node.val == p.val or node.val == q.val else 0
            if node.left:
                cnt += count(node.left)
            if not ans and node.right:
                cnt += count(node.right)
            if not ans and cnt == 2:
                ans = node
            return cnt

        count(root)
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
print(s.lowestCommonAncestor(fromList([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]), TreeNode(5), TreeNode(1)).val)
print(s.lowestCommonAncestor(fromList([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]), TreeNode(5), TreeNode(4)).val)
print(s.lowestCommonAncestor(fromList([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]), TreeNode(5), TreeNode(10)))
