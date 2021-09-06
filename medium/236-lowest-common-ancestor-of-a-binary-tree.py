'''
二叉树的最近公共祖先
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，
满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

 

示例 1：


输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
示例 2：


输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
示例 3：

输入：root = [1,2], p = 1, q = 2
输出：1
 

提示：

树中节点数目在范围 [2, 10^5] 内。
-10^9 <= Node.val <= 10^9
所有 Node.val 互不相同 。
p != q
p 和 q 均存在于给定的二叉树中。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
思路：树的遍历
设一个遍历pathLists用于保存含有目标值的路径。
1. DFS遍历树，遍历的过程中记住当前路径。
> 如果当前节点是目标，将当前路径加入pathLists，如果pathLists.length为2，则2个节点都找到，退出。
> 如果当前节点不是目标，查找左子树，如果pathLists.length<2；继续查找右子树。
2. 对比pathLists的2条路径，直到一个路径到了末尾或者下一个节点不同，返回该节点。

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pathLists = []

        # 查找2个节点所处的路径
        def find(node, path):
            path.append(node)
            if node == p or node == q:
                pathLists.append(path.copy())  # 当前节点是目标之一，将当前路径保存起来
                if len(pathLists) == 2:  # 已经找到2个目标值，退出
                    return
            if node.left:  # 遍历左子树
                find(node.left, path)
                if len(pathLists) == 2:  # 已经找到2个目标值，退出
                    return
            if node.right:  # 遍历右子树
                find(node.right, path)
                if len(pathLists) == 2:  # 已经找到2个目标值，退出
                    return
            path.pop()

        find(root, [])
        # 对比路径，找到最深的一个
        path1, path2 = pathLists[0], pathLists[1]
        n = min(len(path1), len(path2))
        for i in range(n):
            if i == n - 1 or path1[i + 1] != path2[i + 1]:  # 已经到了队尾，当前节点就是祖先；下一个节点不同，当前节点也是祖先
                return path1[i]
