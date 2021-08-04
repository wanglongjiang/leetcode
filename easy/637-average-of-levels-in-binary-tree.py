'''
二叉树的层平均值
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。

 

示例 1：

输入：
    3
   / \\
  9  20
    /  \\
   15   7
输出：[3, 14.5, 11]
解释：
第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。
 

提示：

节点值的范围在32位有符号整数范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/average-of-levels-in-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：BFS
用BFS遍历每一层元素，求平均值

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        q, nextq = deque(), deque()
        ans = [root.val]
        q.append(root)
        total = 0
        while q:
            node = q.popleft()
            if node.left:
                nextq.append(node.left)
                total += node.left.val
            if node.right:
                nextq.append(node.right)
                total += node.right.val
            if not q:
                if nextq:
                    ans.append(total / len(nextq))
                    total = 0
                    q, nextq = nextq, q
        return ans
