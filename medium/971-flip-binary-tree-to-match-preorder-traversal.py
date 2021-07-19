'''
翻转二叉树以匹配先序遍历
给你一棵二叉树的根节点 root ，树中有 n 个节点，每个节点都有一个不同于其他节点且处于 1 到 n 之间的值。

另给你一个由 n 个值组成的行程序列 voyage ，表示 预期 的二叉树 先序遍历 结果。

通过交换节点的左右子树，可以 翻转 该二叉树中的任意节点。例，翻转节点 1 的效果如下：


请翻转 最少 的树中节点，使二叉树的 先序遍历 与预期的遍历行程 voyage 相匹配 。 

如果可以，则返回 翻转的 所有节点的值的列表。你可以按任何顺序返回答案。如果不能，则返回列表 [-1]。

 

示例 1：


输入：root = [1,2], voyage = [2,1]
输出：[-1]
解释：翻转节点无法令先序遍历匹配预期行程。
示例 2：


输入：root = [1,2,3], voyage = [1,3,2]
输出：[1]
解释：交换节点 2 和 3 来翻转节点 1 ，先序遍历可以匹配预期行程。
示例 3：


输入：root = [1,2,3], voyage = [1,2,3]
输出：[]
解释：先序遍历已经匹配预期行程，所以不需要翻转节点。
 

提示：

树中的节点数目为 n
n == voyage.length
1 <= n <= 100
1 <= Node.val, voyage[i] <= n
树中的所有值 互不相同
voyage 中的所有值 互不相同
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：DFS
深度优先遍历树，如果当前节点node.val=voyage[i]，继续递归匹配左子树与voyage[i+1]，如果匹配失败，匹配右子树与voyage[i+1]，如果2者有1个匹配成功，返回true
否则返回false

时间复杂度：O(n)
空间复杂度：O(h)
'''


class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        ans = []

        # 从i开始，匹配当前节点和其子节点，匹配成功返回当前子树的节点个数，否则返回0
        def match(node, i):
            if node.val != voyage[i]:
                return 0
            leftSize, rightSize = 0, 0
            if node.left:
                leftSize = match(node.left, i + 1)
                if not leftSize:  # 先匹配左子树失败
                    rightSize = match(node.right, i + 1)
                    if rightSize:  # 尝试匹配右子树匹配成功
                        leftSize = match(node.left, i + 1 + rightSize)
                        if leftSize:  # 左右子树都匹配成功，node需要进行交换
                            ans.append(node.val)
                            return leftSize + rightSize + 1
                        else:  # 右子树匹配成功，左子树匹配失败
                            return 0
                    else:  # 左右子树均匹配失败
                        return 0
            if node.right:
                rightSize = match(node.right, i + 1 + leftSize)  # 左子树匹配成功，继续匹配右子树
                if rightSize:  # 右子树匹配成功
                    return leftSize + 1 + rightSize
                else:
                    return 0  # 右子树匹配失败
            return leftSize + rightSize + 1

        if match(root, 0) == len(voyage):
            return ans
        else:
            return [-1]
