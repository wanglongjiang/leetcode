'''
剑指 Offer II 050. 向下的路径节点之和
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

 

示例 1：



输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3
解释：和等于 8 的路径有 3 条，如图所示。
示例 2：

输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：3
 

提示:

二叉树的节点个数的范围是 [0,1000]
-109 <= Node.val <= 109 
-1000 <= targetSum <= 1000 
 

注意：本题与主站 437 题相同：https://leetcode-cn.com/problems/path-sum-iii/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/6eUYwP
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：递归 哈希
遍历树，用一个哈希表记录从根节点到当前节点的所有前缀和，
> 如果当前节点前缀和prefixSum为sum，则从根节点到当前节点的路径满足要求
> 如果prefixSum-sum在哈希表中存在，说明有某个子路径也满足要求

该题与
437.[路径总和 III](medium/437-path-sum-iii.py)
面试题 04.12. [求和路径](interview/04.12.paths-with-sum-lcci.py)相同

时间复杂度：O(n)
空间复杂度：O(h),h为树的高度
'''


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        counter = defaultdict(int)
        ans = 0

        def dfs(node, prefixSum):
            nonlocal ans
            prefixSum += node.val
            if prefixSum == targetSum:
                ans += 1
            if counter[prefixSum - targetSum] > 0:
                ans += counter[prefixSum - targetSum]
            counter[prefixSum] += 1
            if node.left:
                dfs(node.left, prefixSum)
            if node.right:
                dfs(node.right, prefixSum)
            counter[prefixSum] -= 1

        dfs(root, 0)
        return ans
