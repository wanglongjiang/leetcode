'''
最大层内元素和
给你一个二叉树的根节点 root。设根节点位于二叉树的第 1 层，而根节点的子节点位于第 2 层，依此类推。

请你找出层内元素之和 最大 的那几层（可能只有一层）的层号，并返回其中 最小 的那个。

 

示例 1：



输入：root = [1,7,0,7,-8,null,null]
输出：2
解释：
第 1 层各元素之和为 1，
第 2 层各元素之和为 7 + 0 = 7，
第 3 层各元素之和为 7 + -8 = -1，
所以我们返回第 2 层的层号，它的层内元素之和最大。
示例 2：

输入：root = [989,null,10250,98693,-89388,null,null,null,-32127]
输出：2
 

提示：

树中的节点数介于 1 和 10^4 之间
-10^5 <= node.val <= 10^5
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：BFS
BFS遍历树，合计每一层的所有节点和

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        q, nextq = [], []
        ans, maxsum, level = 1, root.val, 1
        q.append(root)
        while q:
            node = q.pop()
            if node.left:
                nextq.append(node.left)
            if node.right:
                nextq.append(node.right)
            if not q:
                q, nextq = nextq, q
                nextsum = sum(map(lambda node: node.val, q))
                level += 1
                if nextsum > maxsum and q:
                    maxsum = nextsum
                    ans = level
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
print(s.maxLevelSum(fromList([-100, -200, -300, -20, -5, -10, null])))
