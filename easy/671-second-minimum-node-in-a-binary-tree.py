'''
二叉树中第二小的节点
给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。如果一个节点有两个子节点的话，
那么该节点的值等于两个子节点中较小的一个。

更正式地说，root.val = min(root.left.val, root.right.val) 总成立。

给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。

 

示例 1：


输入：root = [2,2,5,null,null,5,7]
输出：5
解释：最小的值是 2 ，第二小的值是 5 。
示例 2：


输入：root = [2,2,2]
输出：-1
解释：最小的值是 2, 但是不存在第二小的值。
 

提示：

树中节点数目在范围 [1, 25] 内
1 <= Node.val <= 2^31 - 1
对于树中每个节点 root.val == min(root.left.val, root.right.val)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：递归
遍历所有节点，找到最小和次小的元素

时间复杂度：O(n)
空间复杂度：O(h)
'''


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.min1, self.min2 = float('inf'), float('inf')

        def dfs(node):
            if not node.left:
                if self.min1 >= node.val:
                    if self.min1 != node.val:
                        self.min2 = self.min1
                        self.min1 = node.val
                elif self.min2 > node.val:
                    self.min2 = node.val
            else:
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return -1 if self.min2 == float('inf') else self.min2


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
print(s.findSecondMinimumValue(fromList([2, 2, 2])))
print(s.findSecondMinimumValue(fromList([5, 8, 5])))
print(s.findSecondMinimumValue(fromList([1, 1, 3, 1, 1, 3, 4, 3, 1, 1, 1, 3, 8, 4, 8, 3, 3, 1, 6, 2, 1])))
