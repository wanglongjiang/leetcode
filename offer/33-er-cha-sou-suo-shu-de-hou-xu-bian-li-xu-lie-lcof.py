'''
剑指 Offer 33. 二叉搜索树的后序遍历序列
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

 

参考以下这颗二叉搜索树：

     5
    / \\
   2   6
  / \\
 1   3
示例 1：

输入: [1,6,3,2,5]
输出: false
示例 2：

输入: [1,3,2,6,5]
输出: true
 

提示：

数组长度 <= 1000
'''
from typing import List
'''
思路：递归
根据二叉搜索树和后序遍历的性质（左、右、根）
子数组的最后1个元素root是根节点，然后子数组从start开始向后遍历找到的第1个>root的索引为mid
那么start..mid-1 全部都<root，mid..end-1全部都>root，且start..mid-1 全部都<mid..end-1 (左子树小于右子树)
如果满足如上性质，start..mid-1，mid..end-1 这2部分也是左右2颗子树的后序遍历，需要递归处理

时间复杂度：O(n^2)
空间复杂度：O(logn)
'''


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def isPostOrder(start, end):
            root = postorder[end]
            for i in range(start, end):
                if postorder[i] > root:  # 找到的第1个>root的元素作为中点，分为左右2个子树
                    for j in range(i, end):  # 遍历i之后的元素，确保右子树全部>root,>左子树
                        if postorder[j] <= root:
                            return False
                    if i > start and not isPostOrder(start, i - 1):  # 递归处理左子树
                        return False
                    if end > i and not isPostOrder(i, end - 1):  # 递归处理右子树
                        return False
            return True

        return isPostOrder(0, len(postorder) - 1)


s = Solution()
print(s.verifyPostorder([1, 2, 5, 10, 6, 9, 4, 3]))
