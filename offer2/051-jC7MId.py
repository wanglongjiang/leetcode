'''
剑指 Offer II 051. 节点之和最大的路径
路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。
该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给定一个二叉树的根节点 root ，返回其 最大路径和，即所有路径上节点值之和的最大值。

 

示例 1：



输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
示例 2：



输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
 

提示：

树中节点数目范围是 [1, 3 * 10^4]
-1000 <= Node.val <= 1000
 

注意：本题与主站 124 题相同： https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jC7MId
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：动态规划。
该题目具有典型的最优子结构。
1、叶子节点的最大路径和为val
2、非叶子节点，经过它的的最大路径和为val+min(0,左子树的最大路径和)+min(0,右子树的最大路径和)
首先计算所有叶子节点的最大路径和，然后计算上级节点的路径和。
1、层遍历所有节点，加入二维数组。
2、从最下面一层节点开始计算其最大路径和，放入哈希表中。
    如果是叶子节点，pathSum[node] = node.val
    如果不是叶子节点，pathSum[node] = pathSum[node] = max(leftsum, rightsum) + node.val
所有的节点的最大路径和中的最大值即为返回值

时间复杂度：O(n)，需要遍历2次节点
空间复杂度：O(n)，遍历和动态规划哈希表都需要O(n)空间
'''


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        nodes = [[]]
        # bfs遍历所有节点
        queue = [root, None]
        while queue:
            node = queue[0]
            del queue[0]
            if not node:
                if not queue or not queue[-1]:  # 如果队列中最后一个节点为null，说明没有需要遍历的
                    continue
                queue.append(node)
                nodes.append([])
                continue
            nodes[-1].append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        # 从最下面一层开始，依次计算所有节点的最大路径和
        pathSums = {}
        maxSum = float('-inf')
        while nodes:
            layer = nodes.pop()
            for node in layer:
                leftsum, rightsum = 0, 0
                if node.left and pathSums[id(node.left)] > 0:  # 只有大于0才合计
                    leftsum = pathSums[id(node.left)]
                if node.right and pathSums[id(node.right)] > 0:
                    rightsum = pathSums[id(node.right)]
                pathSums[id(node)] = max(leftsum, rightsum) + node.val
                maxSum = max(maxSum, leftsum + rightsum + node.val)
        return maxSum


s = Solution()
print(s.maxPathSum(TreeNode(-3)) == -3)
