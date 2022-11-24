'''
2476. 二叉搜索树最近节点查询
中等
14
相关企业
给你一个 二叉搜索树 的根节点 root ，和一个由正整数组成、长度为 n 的数组 queries 。

请你找出一个长度为 n 的 二维 答案数组 answer ，其中 answer[i] = [mini, maxi] ：

mini 是树中小于等于 queries[i] 的 最大值 。如果不存在这样的值，则使用 -1 代替。
maxi 是树中大于等于 queries[i] 的 最小值 。如果不存在这样的值，则使用 -1 代替。
返回数组 answer 。

 

示例 1 ：



输入：root = [6,2,13,1,4,9,15,null,null,null,null,null,null,14], queries = [2,5,16]
输出：[[2,2],[4,6],[15,-1]]
解释：按下面的描述找出并返回查询的答案：
- 树中小于等于 2 的最大值是 2 ，且大于等于 2 的最小值也是 2 。所以第一个查询的答案是 [2,2] 。
- 树中小于等于 5 的最大值是 4 ，且大于等于 5 的最小值是 6 。所以第二个查询的答案是 [4,6] 。
- 树中小于等于 16 的最大值是 15 ，且大于等于 16 的最小值不存在。所以第三个查询的答案是 [15,-1] 。
示例 2 ：



输入：root = [4,null,9], queries = [3]
输出：[[-1,4]]
解释：树中不存在小于等于 3 的最大值，且大于等于 3 的最小值是 4 。所以查询的答案是 [-1,4] 。
 

提示：

树中节点的数目在范围 [2, 105] 内
1 <= Node.val <= 106
n == queries.length
1 <= n <= 105
1 <= queries[i] <= 106
'''
from bisect import bisect_left
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
[TOC]

# 思路
DFS + 二分

# 解题方法
因为测试用例中有不平衡的二叉树，所以不能直接搜索二叉树

首先用前序遍历将所有的值放入数组中

然后遍历queries，用二分查找数组，找到最接近的2个元素

# 复杂度
- 时间复杂度: 
> $O(nlog(m))$ ,m为树的节点数量

- 空间复杂度: 
> $O(m)$，
'''


class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        li = []

        def dfs(node: TreeNode):
            if node.left:
                dfs(node.left)
            li.append(node.val)
            if node.right:
                dfs(node.right)

        dfs(root)
        ans = []
        for q in queries:
            i = bisect_left(li, q)
            if i == 0:
                if li[i] == q:
                    ans.append([q, q])
                else:
                    ans.append([-1, li[i]])
            elif i == len(li):
                ans.append([li[-1], -1])
            elif li[i] == q:
                ans.append([q, q])
            else:
                ans.append([li[i - 1], li[i]])
        return ans


s = Solution()
assert s.closestNodes()
