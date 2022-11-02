'''

255. 验证前序遍历序列二叉搜索树
给定一个整数数组，你需要验证它是否是一个二叉搜索树正确的先序遍历序列。

你可以假定该序列中的数都是不相同的。

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：

输入: [5,2,6,1,3]
输出: false
示例 2：

输入: [5,2,1,3,6]
输出: true
进阶挑战：

您能否使用恒定的空间复杂度来完成此题？
'''
from typing import List
'''
思路：分治
根据前序遍历的性质，第0个元素将后面的部分拆分成<它和>它的2部分，
小于部分，其上限为根
大于部分，其下限为根
根据这个性质，进行递归分治，直至分解到每个子树大小为0或者不满足上下限要求。

时间复杂度：O(nlogh)，设h为树的高度
空间复杂度：O(logh)
'''


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        def f(start, end, lowLimit, upLimit):
            if preorder[start] > upLimit or preorder[start] < lowLimit:  # 节点值超出限值，返回false
                return False
            rightBegin = 0
            for i in range(start + 1, end):
                if preorder[start] < preorder[i]:  # 查找右子树开始下标
                    rightBegin = i
                    break
            else:
                rightBegin = end
            ans = True
            if rightBegin and rightBegin < end:
                ans = f(rightBegin, end, preorder[start], upLimit)  # 右子树的下限变成当前节点
            if ans and rightBegin - start > 1:  # 右子树没有问题，再检查左子树
                ans = f(start + 1, rightBegin, lowLimit, preorder[start])  # 左子树的上限变成当前节点
            return ans

        return f(0, len(preorder), float('-inf'), float('inf'))


s = Solution()
print(s.verifyPreorder([5, 2, 6, 1, 3]))
print(s.verifyPreorder([5, 2, 1, 3, 6]))
