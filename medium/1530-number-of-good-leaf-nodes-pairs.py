'''
好叶子节点对的数量

给你二叉树的根节点 root 和一个整数 distance 。

如果二叉树中两个 叶 节点之间的 最短路径长度 小于或者等于 distance ，那它们就可以构成一组 好叶子节点对 。

返回树中 好叶子节点对的数量 。

 

示例 1：

 



输入：root = [1,2,3,null,4], distance = 3
输出：1
解释：树的叶节点是 3 和 4 ，它们之间的最短路径的长度是 3 。这是唯一的好叶子节点对。
示例 2：



输入：root = [1,2,3,4,5,6,7], distance = 3
输出：2
解释：好叶子节点对为 [4,5] 和 [6,7] ，最短路径长度都是 2 。但是叶子节点对 [4,6] 不满足要求，因为它们之间的最短路径长度为 4 。
示例 3：

输入：root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
输出：1
解释：唯一的好叶子节点对是 [2,5] 。
示例 4：

输入：root = [100], distance = 1
输出：0
示例 5：

输入：root = [1,1,1], distance = 2
输出：1
 

提示：

tree 的节点数在 [1, 2^10] 范围内。
每个节点的值都在 [1, 100] 之间。
1 <= distance <= 10
'''
from sortedcontainers import SortedList


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：SortedList
递归遍历每个子树，
> 统计左子树和右子树中每个叶子节点的距离，将其记录到leftSortedList和rightSortedList中
> 然后遍历leftSortedList中<distance的节点i，在rightSortedList中二分查找<=distance-leftSortedList[i]的节点数量，这个数量就是凑成好节点数的数量
通过上面的遍历累计所有的好节点数量

时间复杂度：O(n^2)，每个节点都需要遍历一次，在统计每个节点的左右子节点距离时需要遍历所有子节点
空间复杂度：O(n)
'''


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans
            leafList = SortedList()
            if node.left and node.right:  # 有左右子树，统计2个子树构成的好叶子节点对
                leftList = dfs(node.left)
                rightList = dfs(node.right)
                for d in leftList:  # 在右子树中寻找<=distance - d的叶子节点数，它与左子树的节点可以构成好叶子对
                    if d < distance:
                        ans += rightList.bisect_right(distance - d)
                    else:
                        break
                for d in leftList:
                    if d < distance - 1:
                        leafList.add(d + 1)
                    else:
                        break
                for d in rightList:
                    if d < distance - 1:
                        leafList.add(d + 1)
                    else:
                        break
            elif node.left:  # 添加左子树叶子节点
                for d in dfs(node.left):
                    if d < distance - 1:
                        leafList.add(d + 1)
                    else:
                        break
            elif node.right:  # 添加右子树叶子节点
                for d in dfs(node.right):
                    if d < distance - 1:
                        leafList.add(d + 1)
                    else:
                        break
            else:
                leafList.add(1)
            return leafList

        dfs(root)
        return ans
