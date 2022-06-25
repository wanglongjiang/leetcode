'''
1130. 叶值的最小代价生成树
给你一个正整数数组 arr，考虑所有满足以下条件的二叉树：

每个节点都有 0 个或是 2 个子节点。
数组 arr 中的值与树的中序遍历中每个叶节点的值一一对应。（知识回顾：如果一个节点有 0 个子节点，那么该节点为叶节点。）
每个非叶节点的值等于其左子树和右子树中叶节点的最大值的乘积。
在所有这样的二叉树中，返回每个非叶节点的值的最小可能总和。这个和的值是一个 32 位整数。

 

示例：

输入：arr = [6,2,4]
输出：32
解释：
有两种可能的树，第一种的非叶节点的总和为 36，第二种非叶节点的总和为 32。

    24            24
   /  \          /  \
  12   4        6    8
 /  \               / \
6    2             2   4
 

提示：

2 <= arr.length <= 40
1 <= arr[i] <= 15
答案保证是一个 32 位带符号整数，即小于 2^31。
'''
from typing import List
'''
思路：回溯+记忆化搜索
如果数组大小为2，返回元组(当前子数组的根节点值，非叶节点之和)
如果数组大小为大于2，设置1个挡板，将数组切分成2个子数组，记录挡板在不同位置时最小的，这个过程需要回溯。设置一个记忆表，避免重复计算。

时间复杂度：O(n^2)，需要计算任意2个start,end的组合，设n为arr.length，任意2个start,end的组合为O(n^2)
空间复杂度：O(n^2)
'''


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        mem = {}  # 记忆表

        def backtrack(start, end):
            if (start, end) in mem:  # 结果已经在记忆表种存在，直接返回
                return mem[(start, end)]
            if end - start == 2:
                return (max(arr[start], arr[start + 1]), arr[start] * arr[start + 1])  # 返回2个节点构成的子树的(最大叶节点,子树的非叶节点之和)
            leftMaxLeaf, leftSum = backtrack(start, end - 1)  # 计算挡板在end-1处，左子数组根节点值和非叶子节点和
            maxLeaf = max(leftMaxLeaf, arr[end - 1])
            ansSumVal = leftMaxLeaf * arr[end - 1] + leftSum  # 计算挡板在end-1处的结果
            rightMaxLeaf, rightSum = backtrack(start + 1, end)  # 计算挡板在start+1处，右子数组根节点值和非叶子节点和
            if rightMaxLeaf * arr[start] + rightSum < ansSumVal:  # 挡板在start+1处比在end-1处更合理，更换结果
                ansSumVal = rightMaxLeaf * arr[start] + rightSum
                maxLeaf = max(rightMaxLeaf, arr[start])
            for mid in range(start + 2, end - 1):  # 遍历剩下的挡板位置
                leftMaxLeaf, leftSum = backtrack(start, mid)
                rightMaxLeaf, rightSum = backtrack(mid, end)
                if leftMaxLeaf * rightMaxLeaf + leftSum + rightSum < ansSumVal:  # 如果该切分的结果更小，更换结果
                    ansSumVal = leftMaxLeaf * rightMaxLeaf + leftSum + rightSum
                    maxLeaf = max(leftMaxLeaf, rightMaxLeaf)
            mem[(start, end)] = (maxLeaf, ansSumVal)
            return (maxLeaf, ansSumVal)

        return backtrack(0, len(arr))[1]


s = Solution()
print(s.mctFromLeafValues([13, 15, 12, 15, 4, 1, 7, 9, 13, 2, 15, 5, 12, 5, 3, 6, 8, 7, 7, 15, 7, 12, 6, 6, 8, 13, 1]))
print(s.mctFromLeafValues([6, 2, 4]))
print(s.mctFromLeafValues([15, 13, 5, 3, 15]))
