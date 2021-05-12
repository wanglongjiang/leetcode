'''
打家劫舍 III

在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。
除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:

输入: [3,2,3,null,3,null,1]

     3
    / \\
   2   3
    \\   \\
     3   1

输出: 7
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
示例 2:

输入: [3,4,5,1,3,null,1]

     3
    / \\
   4   5
  / \\   \\
 1   3   1

输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
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
因不能选择连续的2个节点，即节点与其子节点不能同时选择。可以找出状态转移方程为：
dp[i] = max(当前节点.val+sum(孙节点.val),sum(子节点.val))
因这里为二叉树，可以使用2个哈希表代替dp数组
哈希表1：dp，key=id(node),val为当前节点所代表的子树最大能提供的金额
哈希表2：child,key=id(node),val为当前节点直接子节点的dp和

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def rob(self, root: TreeNode) -> int:
        dp, child = {}, {}

        def dfs(node):
            thisId = id(node)
            if thisId in dp:  # 如果在dp中已计算完成，直接返回
                return
            val = node.val  # 存放当前节点值+孙节点值之和
            childSum = 0  # 存放子节点值之和
            if node.left:
                dfs(node.left)
                leftId = id(node.left)
                childSum += dp[leftId]  # 累计子节点值
                val += child[leftId]  # 累计孙节点值
            if node.right:
                dfs(node.right)
                rightId = id(node.right)
                childSum += dp[rightId]  # 累计子节点值
                val += child[rightId]  # 累计孙节点值
            child[thisId] = childSum  # 将子节点和存储起来，供父节点计算时使用
            dp[thisId] = max(val, childSum)  # 当前节点的最大值

        dfs(root)
        return dp[id(root)]


# list数据按照bfs遍历得到
def fromList(li: List[int]):
    if len(li) == 0:
        return None
    root = TreeNode(val=li[0])
    queue = [root]
    i = 1
    while i < len(li):
        node = queue[0]
        del queue[0]
        if li[i] is not None:
            node.left = TreeNode(val=li[i])
            queue.append(node.left)
        i += 1
        if i < len(li):
            if li[i]:
                node.right = TreeNode(val=li[i])
                queue.append(node.right)
            i += 1
    return root


s = Solution()
null = None
print(s.rob(fromList([3, 2, 3, null, 3, null, 1])))
print(s.rob(fromList([3, 4, 5, 1, 3, null, 1])))
