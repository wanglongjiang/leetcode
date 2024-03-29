'''
剑指 Offer II 056. 二叉搜索树中两个节点之和
给定一个二叉搜索树的 根节点 root 和一个整数 k , 请判断该二叉搜索树中是否存在两个节点它们的值之和等于 k 。假设二叉搜索树中节点的值均唯一。

 

示例 1：

输入: root = [8,6,10,5,7,9,11], k = 12
输出: true
解释: 节点 5 和节点 7 之和等于 12
示例 2：

输入: root = [8,6,10,5,7,9,11], k = 22
输出: false
解释: 不存在两个节点值之和为 22 的节点
 

提示：

二叉树的节点个数的范围是  [1, 10^4].
-10^4 <= Node.val <= 10^4
root 为二叉搜索树
-10^5 <= k <= 10^5
 

注意：本题与主站 653 题相同： https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/opLdQZ
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：树 哈希
设一个哈希表hashset用于保存节点值
遍历树的每个节点，查找哈希表中是否存在k-node.val，如果存在，返回true，否则将node.val加入hashset

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        hashset = set()

        def dfs(node):
            if k - node.val in hashset:
                return True
            hashset.add(node.val)
            if node.left and dfs(node.left):
                return True
            if node.right and dfs(node.right):
                return True
            return False

        return dfs(root)
