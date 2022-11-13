'''
从叶结点开始的最小字符串

给定一颗根结点为 root 的二叉树，树中的每一个结点都有一个从 0 到 25 的值，分别代表字母 'a' 到 'z'：值 0 代表 'a'，值 1 代表 'b'，依此类推。

找出按字典序最小的字符串，该字符串从这棵树的一个叶结点开始，到根结点结束。

（小贴士：字符串中任何较短的前缀在字典序上都是较小的：例如，在字典序上 "ab" 比 "aba" 要小。叶结点是指没有子结点的结点。）

 

示例 1：



输入：[0,1,2,3,4,3,4]
输出："dba"
示例 2：



输入：[25,1,3,1,3,0,2]
输出："adz"
示例 3：



输入：[2,2,1,null,1,0,null,0]
输出："abc"
 

提示：

给定树的结点数介于 1 和 8500 之间。
树中的每个结点都有一个介于 0 和 25 之间的值。
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
思路：DFS
遍历每条从叶节点到根节点的路径，与已往保存的最小路径minpath进行对比
minpath初始值为[26]

时间复杂度：最坏情况下O(n^2)，平均情况O(h^2)
空间复杂度：O(h)
'''


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        minPath = [26]

        def dfs(node, path):
            nonlocal minPath
            path.append(node.val)
            if not node.left and not node.right:  # 如果是叶子节点，从下往上对比每个值，如果比以往保存的小，则更换
                for i in range(-1, -min(len(path), len(minPath)) - 1, -1):
                    if path[i] < minPath[i]:
                        minPath = path.copy()
                        break
                    elif path[i] > minPath[i]:
                        break
                else:
                    if len(path) < len(minPath):
                        minPath = path.copy()
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)
            path.pop()

        dfs(root, [])
        s = ''
        for i in range(len(minPath) - 1, -1, -1):
            s += chr(minPath[i] + ord('a'))
        return s


# list数据按照bfs遍历得到
def fromList(li: List[int]):
    if len(li) == 0:
        return None
    root = TreeNode(x=li[0])
    queue = [root]
    i = 1
    while i < len(li):
        node = queue[0]
        del queue[0]
        if li[i] is not None:
            node.left = TreeNode(x=li[i])
            queue.append(node.left)
        i += 1
        if i < len(li):
            if li[i]:
                node.right = TreeNode(x=li[i])
                queue.append(node.right)
            i += 1
    return root


s = Solution()
null = None
assert s.smallestFromLeaf(fromList([4, 0, 1, 1])) == 'bae'
print(s.smallestFromLeaf(fromList([2, 2, 1, null, 1, 0, null, 0])))
print(s.smallestFromLeaf(fromList([0, 1, 2, 3, 4, 3, 4])))
