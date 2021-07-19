'''
前序遍历构造二叉搜索树

返回与给定前序遍历 preorder 相匹配的二叉搜索树（binary search tree）的根结点。

(回想一下，二叉搜索树是二叉树的一种，其每个节点都满足以下规则，对于 node.left 的任何后代，值总 < node.val，而 node.right 的任何后代，值总 > node.val。
此外，前序遍历首先显示节点 node 的值，然后遍历 node.left，接着遍历 node.right。）

题目保证，对于给定的测试用例，总能找到满足要求的二叉搜索树。

 

示例：

输入：[8,5,1,7,10,12]
输出：[8,5,10,1,7,null,12]

 

提示：

1 <= preorder.length <= 100
1 <= preorder[i] <= 10^8
preorder 中的值互不相同
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：递归
根据前序遍历的定义，数组第0个元素为根节点值，然后再根据二叉搜索树的定义，
从第1个开始，依次遍历数组剩余元素，<nums[0]的，是左子树的前序遍历结果，>nums[0]的，是右子树的前序遍历结果。
将这2个子数组分别递归处理

时间复杂度：O(n^2)，每次子数组去掉开头的元素后，剩余的要分成>nums[0]和<nums[0]2部分，故需要O(n^2)
空间复杂度：O(n)
'''


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def make(start, end):
            node = TreeNode(val=preorder[start])
            i = start + 1
            for i in range(start + 1, end):
                if preorder[i] < preorder[start]:
                    i += 1
                else:
                    break
            if i > start + 1:
                node.left = make(start + 1, i)
            if i < end:
                node.right = make(i, end)
            return node

        return make(0, len(preorder))


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
print(toList(s.bstFromPreorder([8, 5, 1, 7, 10, 12])))
