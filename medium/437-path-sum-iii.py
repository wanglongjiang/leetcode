'''
路径总和 III

给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：递归
遍历树，记录从根节点到当前节点的路径，然后从根节点开始，依次去掉其祖父，计算是否和为targetSum
时间复杂度：O(n^2)，树的遍历为O(n)，针对每个节点，依次去掉其祖父，直至只剩当前节点，最坏情况下每个节点的时间复杂度也是O(n)
空间复杂度：O(n)
'''


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        path = []

        def calc(node, total):
            path.append(node.val)
            total += node.val
            count = 0
            if node.left:
                count += calc(node.left, total)  # 累加左子树的路径
            if node.right:
                count += calc(node.right, total)  # 累加右子树的路径
            for val in path:  # 从根节点到当前节点的路径，从上到下减掉上级节点，判断路径和是否与目标值相同
                if total == targetSum:
                    count += 1
                total -= val
            path.pop()
            return count

        return calc(root, 0)
