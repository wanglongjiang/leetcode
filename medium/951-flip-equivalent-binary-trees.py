'''
翻转等价二叉树

我们可以为二叉树 T 定义一个翻转操作，如下所示：选择任意节点，然后交换它的左子树和右子树。

只要经过一定次数的翻转操作后，能使 X 等于 Y，我们就称二叉树 X 翻转等价于二叉树 Y。

编写一个判断两个二叉树是否是翻转等价的函数。这些树由根节点 root1 和 root2 给出。

 

示例：

输入：root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
输出：true
解释：我们翻转值为 1，3 以及 5 的三个节点。

 

提示：

每棵树最多有 100 个节点。
每棵树中的每个值都是唯一的、在 [0, 99] 范围内的整数。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：递归 树
对比2个子树的根节点，如果相同，递归对比左右子节点 或者 交换后的左右子节点
如果不相同返回False

时间复杂度：O(n)
空间复杂度：O(h)
'''


class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def cmp(node1: TreeNode, node2: TreeNode):
            if node1 is None and node2 is None:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return (cmp(node1.left, node2.left) and cmp(node1.right, node2.right)) or (cmp(node1.left, node2.right) and cmp(node1.right, node2.left))

        return cmp(root1, root2)
