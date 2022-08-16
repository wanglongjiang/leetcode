'''
536. 从字符串生成二叉树
你需要从一个包括括号和整数的字符串构建一棵二叉树。

输入的字符串代表一棵二叉树。它包括整数和随后的 0 ，1 或 2 对括号。整数代表根的值，一对括号内表示同样结构的子树。

若存在左子结点，则从左子结点开始构建。



示例：

输入："4(2(3)(1))(6(5))"
输出：返回代表下列二叉树的根节点:

       4
     /   \
    2     6
   / \\   /
  3   1 5


提示：

输入字符串中只包含 '(', ')', '-' 和 '0' ~ '9'
空树由 "" 而非"()"表示。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：TODO
'''


class Solution:
    def str2tree(self, s: str) -> TreeNode:
        pass
