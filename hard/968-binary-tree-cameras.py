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
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：DFS 贪心算法
叶子节点的父节点设置为有监控，然后向上隔一个节点设置一个摄像头，需要很多判断，详见代码

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        ans = 0

        def dfs(node, hasParent):
            nonlocal ans
            if not node.left and not node.right:
                if hasParent:  # 叶子节点不需要设置
                    return 0
                ans += 1  # 根节点没有子节点，需要设置
                return 1
            left, right = 1, 1
            if node.left:
                left = dfs(node.left, True)
            if node.right:
                right = dfs(node.right, True)
            # 子节点只要有1个为0，即为未监控；子节点只要有1个设置了监控，当前节点就不用设置监控；
            child = 0 if left == 0 or right == 0 else (2 if left == 2 or right == 2 else 1)
            if child == 0:  # 0代表子节点至少有1个未被监控，当前节点需要设置
                ans += 1
                return 2
            if child == 1:  # 1代表子节点都被监控，但不能影响当前节点
                if hasParent:  # 有父节点，当前节点可以不设置
                    return 0
                else:
                    ans += 1  # 没有父节点，当前节点必须设置监控了
                    return 2
            return 1  # 子节点只要有1个设置了监控，当前节点就不用设置监控

        dfs(root, False)
        return ans


null = None


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


s = Solution()
print(s.minCameraCover(fromList([0, 1, 2, null, 3, 4, null, null, 5])))
print(s.minCameraCover(fromList([0, 1, null, null, 2, 3, null, null, 4, 5])))
print(s.minCameraCover(fromList([0, 1, 2, null, null, null, 3])))
print(s.minCameraCover(fromList([0])))
