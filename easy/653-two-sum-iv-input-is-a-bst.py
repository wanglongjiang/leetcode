'''
两数之和 IV - 输入 BST
给定一个二叉搜索树 root 和一个目标结果 k，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

 

示例 1：


输入: root = [5,3,6,2,4,null,7], k = 9
输出: true
示例 2：


输入: root = [5,3,6,2,4,null,7], k = 28
输出: false
示例 3：

输入: root = [2,1,3], k = 4
输出: true
示例 4：

输入: root = [2,1,3], k = 1
输出: false
示例 5：

输入: root = [2,1,3], k = 3
输出: true
 

提示:

二叉树的节点个数的范围是  [1, 10^4].
-10^4 <= Node.val <= 10^4
root 为二叉搜索树
-10^5 <= k <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst
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
