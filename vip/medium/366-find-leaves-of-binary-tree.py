'''
366. 寻找二叉树的叶子节点
给你一棵二叉树，请按以下要求的顺序收集它的全部节点：

依次从左到右，每次收集并删除所有的叶子节点
重复如上过程直到整棵树为空


示例:

输入: [1,2,3,4,5]

          1
         / \
        2   3
       / \
      4   5

输出: [[4,5,3],[2],[1]]


解释:

1. 删除叶子节点 [4,5,3] ，得到如下树结构：

          1
         /
        2


2. 现在删去叶子节点 [2] ，得到如下树结构：

          1


3. 现在删去叶子节点 [1] ，得到空树：

          []
'''

from typing import List
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：后序遍历+哈希
如果按照后序遍历进行输出，会先输出左子树，达不到题目要求的按层输出叶子节点的效果。
设置一个哈希表，key为层级（叶子节点为0），value为list，list中保存遍历到的叶子节点。
进行后序遍历时，
如果是叶子节点，将其添加到key为0的list中
如果是非叶子节点，需要计算出其高度height = max(left,right)，然后保存到key=height的list中
最后，按照key的排序输出

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        hashmap = defaultdict(list)

        def process(node: TreeNode):
            h = 0  # 记录当前子树的高度，叶子节点高度为0
            if node.left:
                h = process(node.left) + 1
            if node.right:
                h = max(h, process(node.right) + 1)
            hashmap[h].append(node.val)  # 根据子树的高度，确定当前节点在第几个list中输出
            return h

        h = process(root)
        ans = []
        for i in range(h + 1):
            ans.append(hashmap[i])
        return ans


# list数据按照bfs遍历得到
def fromList(li: List[int]):
    if len(li) == 0:
        return None
    root = TreeNode(val=li[0])
    queue = [root]
    i = 1
    while i < len(li):
        node = queue[0]
        del queue[0]
        if li[i] is not None:
            node.left = TreeNode(val=li[i])
            queue.append(node.left)
        i += 1
        if i < len(li):
            if li[i] is not None:
                node.right = TreeNode(val=li[i])
                queue.append(node.right)
            i += 1
    return root


s = Solution()
print(s.findLeaves(fromList([1, 2, 3, 4, 5])))
