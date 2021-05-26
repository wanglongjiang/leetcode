'''
二叉搜索树中第K小的元素

给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。

 

示例 1：
输入：root = [3,1,4,null,2], k = 1
输出：1

示例 2：
输入：root = [5,3,6,2,4,null,null,1], k = 3
输出：3

提示：

树中的节点数为 n 。
1 <= k <= n <= 10^4
0 <= Node.val <= 10^4
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：树
树的前序遍历，
1. 先遍历左子树，将k减去左子树的大小，
> 如果k还是大于0，k还需减一（减掉本节点）
    >> 如果k还是大于1，将k传入右子树继续减去右子树。
> 如果k小于等于0，说明第k个数在左子树，不需要遍历右子树
最后返回k

时间复杂度：O(k)
空间复杂度：O(h)，h为树的高度
'''


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ans = 0

        def findK(node, k):
            nonlocal ans
            if node.left:
                k = findK(node.left, k)  # k经过左子树的遍历后，变小
            if k > 0:
                k -= 1  # 经过了本节点，k减小
                if k == 0:  # 如果恰好等于0，当前节点就是第k个节点
                    ans = node.val
            if k == 0:  # 如果经过左子树、当前节点后，k变成了0，说明已经找到第k个节点，不需要遍历右子树了
                return k
            if node.right:
                return findK(node.right, k)  # 遍历右子树
            return k  # 经过了左、本节点、右子树后，仍然大于0，需要向上返回，由上级节点继续遍历

        findK(root, k)
        return ans
