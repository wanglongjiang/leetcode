'''
2385. 感染二叉树需要的总时间
给你一棵二叉树的根节点 root ，二叉树中节点的值 互不相同 。另给你一个整数 start 。在第 0 分钟，感染 将会从值为 start 的节点开始爆发。

每分钟，如果节点满足以下全部条件，就会被感染：

节点此前还没有感染。
节点与一个已感染节点相邻。
返回感染整棵树需要的分钟数。

 

示例 1：


输入：root = [1,5,3,null,4,10,6,9,2], start = 3
输出：4
解释：节点按以下过程被感染：
- 第 0 分钟：节点 3
- 第 1 分钟：节点 1、10、6
- 第 2 分钟：节点5
- 第 3 分钟：节点 4
- 第 4 分钟：节点 9 和 2
感染整棵树需要 4 分钟，所以返回 4 。
示例 2：


输入：root = [1], start = 1
输出：0
解释：第 0 分钟，树中唯一一个节点处于感染状态，返回 0 。
 

提示：

树中节点的数目在范围 [1, 105] 内
1 <= Node.val <= 105
每个节点的值 互不相同
树中必定存在值为 start 的节点
'''
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：DFS+BFS
先从根节点开始遍历一次树，将每个节点的父节点找到，这样之后从一个接口出发的所有的路径能够打通
然后从start开始，BFS遍历所有节点，返回最远的路径长度

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        nodes, parents = {}, {}

        # dfs遍历所有节点，找到每个节点的父节点
        def dfs(node: TreeNode):
            nodes[node.val] = node
            if node.left:
                dfs(node.left)
                parents[node.left.val] = node
            if node.right:
                dfs(node.right)
                parents[node.right.val] = node

        dfs(root)
        # bfs遍历所有节点
        ans = 0
        q, nextq, marked = [nodes[start]], [], set([nodes[start].val])
        while q:
            node = q.pop()
            if node.left and node.left.val not in marked:
                nextq.append(node.left)
                marked.add(node.left.val)
            if node.right and node.right.val not in marked:
                nextq.append(node.right)
                marked.add(node.right.val)
            if node.val in parents and parents[node.val].val not in marked:
                nextq.append(parents[node.val])
                marked.add(parents[node.val].val)
            if not q and nextq:
                q, nextq = nextq, q
                ans += 1
        return ans
