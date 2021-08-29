'''
270. 最接近的二叉搜索树值
给定一个不为空的二叉搜索树和一个目标值 target，请在该二叉搜索树中找到最接近目标值 target 的数值。

注意：

给定的目标值 target 是一个浮点数
题目保证在该二叉搜索树中只会存在一个最接近目标值的数
示例：

输入: root = [4,2,5,1,3]，目标值 target = 3.714286

    4
   / \
  2   5
 / \
1   3

输出: 4
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：递归遍历树的所有节点
递归遍历树的所有节点，计算节点值与目标的差，返回差的绝对值较小的值

时间复杂度：O(n)
空间复杂度：O(h)
'''


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        val = root.val
        if root.left:
            left = self.closestValue(root.left, target)
            if abs(left - target) < abs(val - target):
                val = left
        if root.right:
            right = self.closestValue(root.right, target)
            if abs(right - target) < abs(val - target):
                val = right
        return val
