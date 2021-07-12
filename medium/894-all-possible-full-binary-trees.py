'''
所有可能的满二叉树
满二叉树是一类二叉树，其中每个结点恰好有 0 或 2 个子结点。

返回包含 N 个结点的所有可能满二叉树的列表。 答案的每个元素都是一个可能树的根结点。

答案中每个树的每个结点都必须有 node.val=0。

你可以按任何顺序返回树的最终列表。

 

示例：

输入：7
输出：[[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,
null,0,0],[0,0,0,0,0,null,null,0,0]]
解释：

 

提示：

1 <= N <= 20

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/all-possible-full-binary-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：动态规划
满二叉树的节点数肯定是奇数，它的子树的节点数也必须是0或者奇数
设dp[i]为节点数为i个的满二叉树的所有树的列表
状态转移方程为：
dp[i]=dp[1..i-1]*dp[i-1..1]的组合

时间复杂度：O(2^n)
空间复杂度：O(2^n)
'''


class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        dp = [[] for _ in range(n + 1)]
        dp[1].append(TreeNode(0))
        for i in range(3, n + 1, 2):  # 遍历所有节点数量
            for j in range(1, i - 1, 2):  # 遍历左子树所有节点数量，从1到i-2
                lefts, rights = dp[j], dp[i - j - 1]
                for left in lefts:
                    for right in rights:
                        dp[i].append(TreeNode(0, left, right))
        return dp[n]
