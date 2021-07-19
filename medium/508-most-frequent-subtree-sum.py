'''
出现次数最多的子树元素和
给你一个二叉树的根结点，请你找出出现次数最多的子树元素和。一个结点的「子树元素和」定义为以该结点为根的二叉树上
所有结点的元素之和（包括结点本身）。

你需要返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。

 

示例 1：
输入:

  5
 /  \\
2   -3
返回 [2, -3, 4]，所有的值均只出现一次，以任意顺序返回所有值。

示例 2：
输入：

  5
 /  \\
2   -5
返回 [2]，只有 2 出现两次，-5 只出现 1 次。

'''
from typing import List
from collections import Counter


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：DFS+哈希
DFS遍历树，求所有子树节点之和，然后将和在哈希表中进行计数

时间复杂度：O(n),n为节点数
空间复杂度：O(n)
'''


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        counter = Counter()

        # 遍历树，将其子树和进行计数
        def dfs(node):
            val = node.val
            if node.left:
                val += dfs(node.left)
            if node.right:
                val += dfs(node.right)
            counter[val] += 1  # 子树和计数
            return val

        dfs(root)
        ans = []
        preCount = 0
        for num, count in counter.most_common():  # 按照个数从大到小排序，只输出计数最多的
            if count >= preCount:
                preCount = count
                ans.append(num)
            else:
                break
        return ans
