'''
二叉树中所有距离为 K 的结点
给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。

返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。

 

示例 1：

输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
输出：[7,4,1]
解释：
所求结点为与目标结点（值为 5）距离为 2 的结点，
值分别为 7，4，以及 1



注意，输入的 "root" 和 "target" 实际上是树上的结点。
上面的输入仅仅是对这些对象进行了序列化描述。
 

提示：

给定的树是非空的。
树上的每个结点都具有唯一的值 0 <= node.val <= 500 。
目标结点 target 是树上的结点。
0 <= K <= 1000.
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
思路：DFS
可以发现距离target为k的节点，分成2部分，1部分是target的子节点，离target的距离为k，
另外1部分是从target的父、祖先节点出发，距离为k-d，d为上级节点距离target的距离
具体算法如下：
1. DFS遍历树，查找target，在查找的过程中维护从根节点到target的路径path
2. 查找距离target为k，距离父节点为k-1,距离祖父节点为k-2。。。的所有节点

时间复杂度：O(n)
空间复杂度：O(h)
'''


class Solution:

    # 查找距离为d的子节点
    def lookupDistance(self, node, curDepth, d):
        if d == curDepth:
            self.ans.append(node.val)
        else:
            if node.left:
                self.lookupDistance(node.left, curDepth + 1, d)
            if node.right:
                self.lookupDistance(node.right, curDepth + 1, d)

    # 查找target
    def lookupTarget(self, node, path):
        path.append(node)
        if node == self.target:
            return True
        if node.left:
            if self.lookupTarget(node.left, path):
                return True
        if node.right:
            if self.lookupTarget(node.right, path):
                return True
        path.pop()
        return False

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        path = []
        self.target = target
        self.lookupTarget(root, path)
        self.ans, pathNodes = [], set(map(lambda node: node.val, path))

        # 从路径上每个节点出发，查找距离为k，k-1，k-2的子节点
        while path:
            node = path.pop()
            if k == 0:  # 路径上的祖先已经到了最大距离，不需要继续查找
                self.ans.append(node.val)  # 主路径上最多只有1个祖先节点满足距离为k
                break
            k -= 1
            if node.left and node.left.val not in pathNodes:  # 遍历当前节点的子节点查找满足距离要求的节点，另外需要确保子节点不在主路径上
                self.lookupDistance(node.left, 0, k)
            if node.right and node.right.val not in pathNodes:  # 遍历当前节点的子节点查找满足距离要求的节点，另外需要确保子节点不在主路径上
                self.lookupDistance(node.right, 0, k)
        return self.ans


# list数据按照bfs遍历得到
def fromList(li: List[int]):
    if len(li) == 0:
        return None
    root = TreeNode(x=li[0])
    queue = [root]
    i = 1
    while i < len(li):
        node = queue[0]
        del queue[0]
        if li[i] is not None:
            node.left = TreeNode(x=li[i])
            queue.append(node.left)
        i += 1
        if i < len(li):
            if li[i]:
                node.right = TreeNode(x=li[i])
                queue.append(node.right)
            i += 1
    return root


s = Solution()
null = None
print(s.distanceK(fromList([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]), 5, 2))
