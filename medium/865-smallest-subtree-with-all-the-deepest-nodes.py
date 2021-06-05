'''
具有所有最深节点的最小子树
给定一个根为 root 的二叉树，每个节点的深度是 该节点到根的最短距离 。

如果一个节点在 整个树 的任意节点之间具有最大的深度，则该节点是 最深的 。

一个节点的 子树 是该节点加上它的所有后代的集合。

返回能满足 以该节点为根的子树中包含所有最深的节点 这一条件的具有最大深度的节点。

 

注意：本题与力扣 1123 重复：https://leetcode-cn.com/problems/lowest-common-ancestor-of-deepest-leaves/

 

示例 1：



输入：root = [3,5,1,6,2,0,8,null,null,7,4]
输出：[2,7,4]
解释：
我们返回值为 2 的节点，在图中用黄色标记。
在图中用蓝色标记的是树的最深的节点。
注意，节点 5、3 和 2 包含树中最深的节点，但节点 2 的子树最小，因此我们返回它。
示例 2：

输入：root = [1]
输出：[1]
解释：根节点是树中最深的节点。
示例 3：

输入：root = [0,1,3,null,2]
输出：[2]
解释：树中最深的节点为 2 ，有效子树为节点 2、1 和 0 的子树，但节点 2 的子树最小。
 

提示：

树中节点的数量介于 1 和 500 之间。
0 <= Node.val <= 500
每个节点的值都是独一无二的。

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：深度优先搜索
1. 遍历所有节点，将达到最大深度的路径加入paths
2. 遍历所有的path，得到最大的公共路径
3. 最大公共路径的末端即为结果
与1123.[最深叶节点的最近公共祖先](medium/1123-lowest-common-ancestor-of-deepest-leaves.py)相同

时间复杂度：O(n^2)，遍历所有路径需要O(n^2)
空间复杂度：O(n^2)，存储所有路径需要O(n^2)
'''


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        paths = []
        maxDepth = 0

        # 1. 遍历所有路径，最长路径加入paths
        def dfs(node, path):
            nonlocal maxDepth
            path.append(node)
            if not node.left and not node.right:
                if len(path) > maxDepth:
                    maxDepth = len(path)
                    if paths:
                        paths.clear()
                    paths.append(path.copy())
                elif len(path) == maxDepth:
                    paths.append(path.copy())
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)
            path.pop()

        dfs(root, [])
        # 2. 遍历所有的path，得到最大的公共路径
        longestPath = []
        for i in range(maxDepth):
            node = paths[0][i]
            for j in range(1, len(paths)):
                if node != paths[j][i]:
                    node = None
                    break
            if node:
                longestPath.append(node)
            else:
                break
        return longestPath[-1]
