'''
在每个树行中找最大值
您需要在二叉树的每一行中找到最大的值。
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
广度优先搜索，每层找到最大值

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        ans, mx = [], float('-inf')
        if not root:
            return ans
        q, nextq = [], []
        q.append(root)
        while q:
            node = q.pop()
            mx = max(mx, node.val)
            if node.left:
                nextq.append(node.left)
            if node.right:
                nextq.append(node.right)
            if not q:
                ans.append(mx)
                q, nextq = nextq, q
                mx = float('-inf')
        return ans
