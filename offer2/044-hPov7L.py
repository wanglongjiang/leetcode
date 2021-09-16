'''
剑指 Offer II 044. 二叉树每层的最大值
给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。

 

示例1：

输入: root = [1,3,2,5,3,null,9]
输出: [1,3,9]
解释:
          1
         / \
        3   2
       / \\  \\
      5   3   9
示例2：

输入: root = [1,2,3]
输出: [1,3]
解释:
          1
         / \\
        2   3
示例3：

输入: root = [1]
输出: [1]
示例4：

输入: root = [1,null,2]
输出: [1,2]
解释:
           1
            \\
             2
示例5：

输入: root = []
输出: []
 

提示：

二叉树的节点个数的范围是 [0,104]
-2^31 <= Node.val <= 231 - 1
 

注意：本题与主站 515 题相同： https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/hPov7L
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
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
