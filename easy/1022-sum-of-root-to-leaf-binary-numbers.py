'''
从根到叶的二进制数之和
给出一棵二叉树，其上每个结点的值都是 0 或 1 。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。
例如，如果路径为 0 -> 1 -> 1 -> 0 -> 1，那么它表示二进制数 01101，也就是 13 。

对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。

返回这些数字之和。题目数据保证答案是一个 32 位 整数。

 

示例 1：


输入：root = [1,0,1,0,1,0,1]
输出：22
解释：(100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
示例 2：

输入：root = [0]
输出：0
示例 3：

输入：root = [1]
输出：1
示例 4：

输入：root = [1,1]
输出：3
 

提示：

树中的结点数介于 1 和 1000 之间。
Node.val 为 0 或 1 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-root-to-leaf-binary-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：DFS
DFS遍历树，得到从根节点到叶子节点的值，然后返回

时间复杂度：O(n)
空间复杂度：O(h)
'''


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(node, val):
            val = val * 2 + node.val
            if not node.left and not node.right:
                return val
            ans = 0
            if node.left:
                ans = dfs(node.left, val)
            if node.right:
                ans += dfs(node.right, val)
            return ans

        return dfs(root, 0)
