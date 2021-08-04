'''
根据二叉树创建字符串
你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。

空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。

示例 1:

输入: 二叉树: [1,2,3,4]
       1
     /   \\
    2     3
   /
  4

输出: "1(2(4))(3)"

解释: 原本将是“1(2(4)())(3())”，
在你省略所有不必要的空括号对之后，
它将是“1(2(4))(3)”。
示例 2:

输入: 二叉树: [1,2,3,null,4]
       1
     /   \\
    2     3
     \\
      4

输出: "1(2()(4))(3)"

解释: 和第一个示例相似，
除了我们不能省略第一个对括号来中断输入和输出之间的一对一映射关系。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-string-from-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：递归
递归处理树的每个节点：
> 如果节点左节点不为空，用（）包含左子树的处理结果
> 如果右子节点不为空，用（）包含右子树的处理结果

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def tree2str(self, root: TreeNode) -> str:
        ans = str(root.val)
        if root.left:
            ans += '(' + self.tree2str(root.left) + ')'
        if root.right:
            if not root.left:
                ans += '()'
            ans += '(' + self.tree2str(root.right) + ')'
        return ans
