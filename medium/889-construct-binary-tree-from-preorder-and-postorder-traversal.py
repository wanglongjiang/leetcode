'''
根据前序和后序遍历构造二叉树

返回与给定的前序和后序遍历匹配的任何二叉树。

 pre 和 post 遍历中的值是不同的正整数。

 

示例：

输入：pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
输出：[1,2,3,4,5,6,7]
 

提示：

1 <= pre.length == post.length <= 30
pre[] 和 post[] 都是 1, 2, ..., pre.length 的排列
每个输入保证至少有一个答案。如果有多个答案，可以返回其中一个。
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
思路：树 递归
前序是：根左右，后序是：左右根
根据上面的性质，对于2个子数组pre[prestart,preend],post[pstart,pend]，
pre[pstart]是子树的根节点，设pre[start+1]在post中的索引是i，则post[i]是子树的根节点，post[pstart,i]是左子树,post[i+1,pend]是右子树
根据上面的性质，写出递归处理程序
TODO
时间复杂度：O(n^2)
空间复杂度：O(n)
'''


class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        root = TreeNode(0)

        def make(parent, preStart, preEnd, postStart, postEnd):
            if preStart > preEnd:
                return
            leftroot = TreeNode(pre[preStart])
            parent.left = leftroot
            leftend = post.index(leftroot.val, postStart, postEnd + 1)  # 找到左子树末尾
            leftsize = leftend - postStart + 1  # 左子树大小
            make(leftroot, preStart + 1, preStart + leftsize - 1, postStart, leftend)  # 处理左子树
            rightsize = postEnd - leftend
            if rightsize > 0:  # 处理右子树
                rightroot = TreeNode(pre[preStart + leftsize])
                parent.right = rightroot
                make(rightroot, preStart + leftsize + 1, preEnd, leftend + 1, postEnd - 1)

        make(root, 0, len(pre) - 1, 0, len(post) - 1)
        return root.left


def toList(node: TreeNode):
    li = []
    if node is None:
        return li
    queue = [node]
    li.append(node.val)
    while len(queue) > 0:
        node = queue[0]
        del queue[0]
        if node.left:
            queue.append(node.left)
            li.append(node.left.val)
        else:
            li.append(None)
        if node.right:
            queue.append(node.right)
            li.append(node.right.val)
        else:
            li.append(None)

    # 删掉末尾的null
    i = len(li) - 1
    while i > 0:
        if li[i] is None:
            del li[i]
        else:
            break
        i -= 1
    return li


s = Solution()
print(toList(s.constructFromPrePost(pre=[1, 2, 4, 5, 3, 6, 7], post=[4, 5, 2, 6, 7, 3, 1])) == [1, 2, 3, 4, 5, 6, 7])
