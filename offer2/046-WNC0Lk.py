'''
剑指 Offer II 046. 二叉树的右侧视图
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

 

示例 1:



输入: [1,2,3,null,5,null,4]
输出: [1,3,4]
示例 2:

输入: [1,null,3]
输出: [1,3]
示例 3:

输入: []
输出: []
 

提示:

二叉树的节点个数的范围是 [0,100]
-100 <= Node.val <= 100 
 

注意：本题与主站 199 题相同：https://leetcode-cn.com/problems/binary-tree-right-side-view/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/WNC0Lk
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：树的遍历，栈
用1个栈vstack存放能看到的部分
按照父->右->左的顺序遍历树，用栈tstack保存需要遍历的节点。
当栈tstack的高度超过vstack时，高出的元素能看到，需要将其入vstack。
树遍历完成后，输出vstack。
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        vstack = []
        tstack = []

        def each(node):
            tstack.append(node.val)
            if len(tstack) > len(vstack):
                vstack.append(tstack[-1])
            if node.right:
                each(node.right)
            if node.left:
                each(node.left)
            tstack.pop()

        each(root)
        return vstack
