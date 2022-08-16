'''
655. 输出二叉树
在一个 m*n 的二维字符串数组中输出二叉树，并遵守以下规则：

行数 m 应当等于给定二叉树的高度。
列数 n 应当总是奇数。
根节点的值（以字符串格式给出）应当放在可放置的第一行正中间。根节点所在的行与列会将剩余空间划分为两部分（左下部分和右下部分）。你应该将左子树输出在左下部分，右子树输出在右下部分。左下和右下部分应当有相同的大小。即使一个子树为空而另一个非空，你不需要为空的子树输出任何东西，但仍需要为另一个子树留出足够的空间。然而，如果两个子树都为空则不需要为它们留出任何空间。
每个未使用的空间应包含一个空的字符串""。
使用相同的规则输出子树。
示例 1:

输入:
     1
    /
   2
输出:
[["", "1", ""],
 ["2", "", ""]]
示例 2:

输入:
     1
    / \
   2   3
    \
     4
输出:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]
示例 3:

输入:
      1
     / \
    2   5
   /
  3
 /
4
输出:
[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
注意: 二叉树的高度在范围 [1, 10] 中。
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
1. DFS遍历树，得到树的高度m
2. 构造矩阵，矩阵的高度为m,宽度n=2^h-1
3. 递归下降设置每层的值，递归函数有3个参数，第0个参数是当前树节点，第1个参数是当前节点的坐标，第2个参数是当前子树的层数

时间复杂度：O(mn)，需要构造m*n的矩阵，遍历树需要O(n)时间复杂度
空间复杂度：O(m)，除了返回值，只需要深度为m的递归深度
'''


class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        # 遍历树，得到高度
        def getHeight(node, h):
            ans = h
            if node.left:
                ans = getHeight(node.left, h + 1)
            if node.right:
                ans = max(ans, getHeight(node.right, h + 1))
            return ans

        m = getHeight(root, 1)
        n = 2**m - 1
        # 构造矩阵
        ans = [[""] * n for _ in range(m)]

        # 递归下降设置值
        def setVal(node, i, h):
            ans[h][i] = str(node.val)
            subWidth = (2**(m - h) - 1) // 2  # 得到子树的宽度
            if node.left:
                setVal(node.left, i - subWidth // 2 - 1, h + 1)  # 左子树的根节点索引是i-子树宽度的一半-1
            if node.right:
                setVal(node.right, i + subWidth // 2 + 1, h + 1)  # 右子树的根节点索引是i+子树宽度的一半+1

        setVal(root, n // 2, 0)
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
            if li[i]:
                node.right = TreeNode(val=li[i])
                queue.append(node.right)
            i += 1
    return root


s = Solution()
print(s.printTree(fromList([1, 2, 3, None, 4])) == [["", "", "", "1", "", "", ""], ["", "2", "", "", "", "3", ""], ["", "", "4", "", "", "", ""]])
print(s.printTree(fromList([1, 2])))
print(
    s.printTree(fromList([1, 2, 5, 3, None, None, None, 4])) ==
    [["", "", "", "", "", "", "", "1", "", "", "", "", "", "", ""], ["", "", "", "2", "", "", "", "", "", "", "", "5", "", "", ""],
     ["", "3", "", "", "", "", "", "", "", "", "", "", "", "", ""], ["4", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]])
