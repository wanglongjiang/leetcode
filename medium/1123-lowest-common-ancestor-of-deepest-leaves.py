'''
最深叶节点的最近公共祖先
给你一个有根节点的二叉树，找到它最深的叶节点的最近公共祖先。

回想一下：

叶节点 是二叉树中没有子节点的节点
树的根节点的 深度 为 0，如果某一节点的深度为 d，那它的子节点的深度就是 d+1
如果我们假定 A 是一组节点 S 的 最近公共祖先，S 中的每个节点都在以 A 为根节点的子树中，且 A 的深度达到此条件下可能的最大值。
 

注意：本题与力扣 865 重复：https://leetcode-cn.com/problems/smallest-subtree-with-all-the-deepest-nodes/

 

示例 1：


输入：root = [3,5,1,6,2,0,8,null,null,7,4]
输出：[2,7,4]
解释：
我们返回值为 2 的节点，在图中用黄色标记。
在图中用蓝色标记的是树的最深的节点。
注意，节点 6、0 和 8 也是叶节点，但是它们的深度是 2 ，而节点 7 和 4 的深度是 3 。
示例 2：

输入：root = [1]
输出：[1]
解释：根节点是树中最深的节点，它是它本身的最近公共祖先。
示例 3：

输入：root = [0,1,3,null,2]
输出：[2]
解释：树中最深的叶节点是 2 ，最近公共祖先是它自己。
 

提示：

给你的树中将有 1 到 1000 个节点。
树中每个节点的值都在 1 到 1000 之间。
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

时间复杂度：O(n^2)，遍历所有路径需要O(n^2)
空间复杂度：O(n^2)，存储所有路径需要O(n^2)
'''


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
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
