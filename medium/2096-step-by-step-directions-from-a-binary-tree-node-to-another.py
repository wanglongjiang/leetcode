'''
2096. 从二叉树一个节点到另一个节点每一步的方向
给你一棵 二叉树 的根节点 root ，这棵二叉树总共有 n 个节点。每个节点的值为 1 到 n 中的一个整数，且互不相同。
给你一个整数 startValue ，表示起点节点 s 的值，和另一个不同的整数 destValue ，表示终点节点 t 的值。

请找到从节点 s 到节点 t 的 最短路径 ，并以字符串的形式返回每一步的方向。每一步用 大写 字母 'L' ，'R' 和 'U' 分别表示一种方向：

'L' 表示从一个节点前往它的 左孩子 节点。
'R' 表示从一个节点前往它的 右孩子 节点。
'U' 表示从一个节点前往它的 父 节点。
请你返回从 s 到 t 最短路径 每一步的方向。

 

示例 1：



输入：root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
输出："UURL"
解释：最短路径为：3 → 1 → 5 → 2 → 6 。
示例 2：



输入：root = [2,1], startValue = 2, destValue = 1
输出："L"
解释：最短路径为：2 → 1 。
 

提示：

树中节点数目为 n 。
2 <= n <= 105
1 <= Node.val <= n
树中所有节点的值 互不相同 。
1 <= startValue, destValue <= n
startValue != destValue
'''

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：DFS递归查找树
递归查找函数逻辑如下：
    函数的返回值是：(startToDest,toStart,toDest)，startToDest为源节点到目标节点路径，toStart为到源节点路径，toDest为到目标节点路径
    函数的入参是：父节点到当前节点的前进方向
    如果当前节点无子节点：
        如果当前节点是源节点或目标节点，将父节点到当前节点的路径附加到startToDest或者toStart返回
        如果当前节点不是源、目标，返回空
    如果当前节点有左子节点：
        遍历左子节点，
            如果子节点返回值里面有startToDest，说明已经找到最短路径，直接返回list
            如果子节点返回值里面有toStart或toDest，返回值复制到当前节点
            如果子节点返回值里面没有内容，什么也不做
    如果当前节点有右子节点：
        遍历右子节点，
            如果子节点返回值里面有startToDest，说明已经找到最短路径，直接返回list
            如果子节点返回值里面有toStart或toDest，返回值复制到当前节点
            如果子节点返回值里面没有内容，什么也不做
    如果当前节点值为源或目标：
        将' '添加到toStart或toDest
    如果toStart、toDest都有值，也就是源、目标的路径都已找到，将toStart字符替换为'U'（因为之前的路径是从上往下的），然后startToDest=toStart+toDest
    如果toStart、toDest有一个有值，将父节点到当前节点的路径添加到toStart或toDest
    
时间复杂度：O(n)
空间复杂度：O(h)，h为树的高度
'''


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(node: TreeNode, parentDir: str):
            if not node.left and not node.right:
                if node.val == startValue:
                    return (None, parentDir, None)
                elif node.val == destValue:
                    return (None, None, parentDir)
                return (None, None, None)
            startToDest, toStart, toDest = None, None, None
            if node.left:
                ret = dfs(node.left, 'L')
                if ret[0]:
                    return ret
                if ret[1]:
                    toStart = ret[1]
                if ret[2]:
                    toDest = ret[2]
            if node.right:
                ret = dfs(node.right, 'R')
                if ret[0]:
                    return ret
                if ret[1]:
                    toStart = ret[1]
                if ret[2]:
                    toDest = ret[2]
            if node.val == startValue:
                toStart = ' '
            elif node.val == destValue:
                toDest = ' '
            if toStart and toDest:
                toStart, toDest = toStart.strip(), toDest.strip()
                toStart = ''.join(['U' for _ in range(len(toStart))])
                startToDest = toStart + toDest
            elif toStart:
                toStart = parentDir + toStart.strip()
            elif toDest:
                toDest = parentDir + toDest.strip()
            return (startToDest, toStart, toDest)

        return dfs(root, 'L')[0]
