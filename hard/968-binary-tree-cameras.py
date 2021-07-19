'''
监控二叉树

给定一个二叉树，我们在树的节点上安装摄像头。

节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。

计算监控树的所有节点所需的最小摄像头数量。


示例 1：



输入：[0,0,null,0,0]
输出：1
解释：如图所示，一台摄像头足以监控所有节点。
示例 2：



输入：[0,0,null,0,null,0,null,null,0]
输出：2
解释：需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。

提示：

给定树的节点数的范围是 [1, 1000]。
每个节点的值都是 0。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：DFS 贪心算法
叶子节点的父节点设置为有监控，然后向上隔一个节点设置一个摄像头

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans
            if not node.left and not node.right:  # 叶子节点不需要设置
                return False
            leftHas, rightHas = False, False
            if node.left:
                leftHas = dfs(node.left)
            if node.right:
                rightHas = dfs(node.right)
            if not leftHas and not rightHas:
                ans += 1
                return True
            return False

        dfs(root)
        return ans
