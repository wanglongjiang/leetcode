'''
二叉树中的伪回文路径
给你一棵二叉树，每个节点的值为 1 到 9 。我们称二叉树中的一条路径是 「伪回文」的，当它满足：路径经过的所有节点值的排列中，存在一个回文序列。

请你返回从根到叶子节点的所有路径中 伪回文 路径的数目。

 

示例 1：



输入：root = [2,3,1,3,1,null,1]
输出：2
解释：上图为给定的二叉树。总共有 3 条从根到叶子的路径：红色路径 [2,3,3] ，绿色路径 [2,1,1] 和路径 [2,3,1] 。
     在这些路径中，只有红色和绿色的路径是伪回文路径，因为红色路径 [2,3,3] 存在回文排列 [3,2,3] ，绿色路径 [2,1,1] 存在回文排列 [1,2,1] 。
示例 2：



输入：root = [2,1,1,1,3,null,null,null,null,null,1]
输出：1
解释：上图为给定二叉树。总共有 3 条从根到叶子的路径：绿色路径 [2,1,1] ，路径 [2,1,3,1] 和路径 [2,1] 。
     这些路径中只有绿色路径是伪回文路径，因为 [2,1,1] 存在回文排列 [1,2,1] 。
示例 3：

输入：root = [9]
输出：1
 

提示：

给定二叉树的节点数目在 1 到 10^5 之间。
节点值在 1 到 9 之间。
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：位运算
如果想要构成伪回文串，路径上的至多只能有1个奇数数字存在，其他数字都必须是偶数。
又因为节点的值只有1-9，可以用1bit表示1个数字出现次数是奇数还是偶数，用9bit就可以表示9个数字出现是奇数还是偶数。
只有1个bit为1，或者全部为0的情况下是伪回文对。

时间复杂度：O(n)
空间复杂度：O(h),h为树的高度，用dfs遍历树需要的递归空间为h
'''


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        def dfs(node, bits):
            bits ^= 1 << node.val  # 如果该数字个数为奇数，bit为1，否则为0
            if not node.left and not node.right:
                return 1 if (bits == 0 or (bits & (bits - 1) == 0)) else 0  # 对于叶子节点，如果所有数字计数都是偶数，或者只有1个是奇数，是伪回文
            return (dfs(node.left, bits) if node.left else 0) + (dfs(node.right, bits) if node.right else 0)  # 非叶子节点返回其子节点的伪回文数

        return dfs(root, 0)


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
print(s.pseudoPalindromicPaths(fromList([2, 3, 1, 3, 1, null, 1])))
