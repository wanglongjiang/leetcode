'''
剑指 Offer II 049. 从根节点到叶节点的路径数字之和
给定一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。

每条从根节点到叶节点的路径都代表一个数字：

例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
计算从根节点到叶节点生成的 所有数字之和 。

叶节点 是指没有子节点的节点。

 

示例 1：


输入：root = [1,2,3]
输出：25
解释：
从根到叶子节点路径 1->2 代表数字 12
从根到叶子节点路径 1->3 代表数字 13
因此，数字总和 = 12 + 13 = 25
示例 2：


输入：root = [4,9,0,5,1]
输出：1026
解释：
从根到叶子节点路径 4->9->5 代表数字 495
从根到叶子节点路径 4->9->1 代表数字 491
从根到叶子节点路径 4->0 代表数字 40
因此，数字总和 = 495 + 491 + 40 = 1026
 

提示：

树中节点的数目在范围 [1, 1000] 内
0 <= Node.val <= 9
树的深度不超过 10
 

注意：本题与主站 129 题相同： https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3Etpl5
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路，遍历树，到了叶子节点时，将这条路径上经过的节点转换成数字累加到结果中
时间复杂度：O(n)
空间复杂度：O(logn)
'''


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        ans = [0]
        path = []

        # 前序遍历树
        def preorder(node):
            path.append(node.val)
            if not node.left and not node.right:
                num = 0
                for i in range(len(path)):  # 将节点从头到尾拼接成整数
                    num = num * 10 + path[i]
                ans[0] += num  # 整数累加到结果
            else:
                if node.left:
                    preorder(node.left)
                if node.right:
                    preorder(node.right)
            path.pop()

        if root:
            preorder(root)
        return ans[0]
