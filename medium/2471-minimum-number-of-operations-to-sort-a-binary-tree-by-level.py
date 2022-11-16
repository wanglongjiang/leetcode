'''
2471. 逐层排序二叉树所需的最少操作数目
中等
10
相关企业
给你一个 值互不相同 的二叉树的根节点 root 。

在一步操作中，你可以选择 同一层 上任意两个节点，交换这两个节点的值。

返回每一层按 严格递增顺序 排序所需的最少操作数目。

节点的 层数 是该节点和根节点之间的路径的边数。

 

示例 1 ：


输入：root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
输出：3
解释：
- 交换 4 和 3 。第 2 层变为 [3,4] 。
- 交换 7 和 5 。第 3 层变为 [5,6,8,7] 。
- 交换 8 和 7 。第 3 层变为 [5,6,7,8] 。
共计用了 3 步操作，所以返回 3 。
可以证明 3 是需要的最少操作数目。
示例 2 ：


输入：root = [1,3,2,7,6,5,4]
输出：3
解释：
- 交换 3 和 2 。第 2 层变为 [2,3] 。 
- 交换 7 和 4 。第 3 层变为 [4,6,5,7] 。 
- 交换 6 和 5 。第 3 层变为 [4,5,6,7] 。
共计用了 3 步操作，所以返回 3 。 
可以证明 3 是需要的最少操作数目。
示例 3 ：


输入：root = [1,2,3,4,5,6]
输出：0
解释：每一层已经按递增顺序排序，所以返回 0 。
 

提示：

树中节点的数目在范围 [1, 105] 。
1 <= Node.val <= 105
树中的所有值 互不相同 。
'''
# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
[TOC]

# 思路
BFS 排序

# 解题方法
> 用BFS遍历每层元素
> 一层元素完整的取到后，一个副本进行排序，排序后的顺序与未排序的进行对比，找到最小交换次数


# 复杂度
- 时间复杂度: 
> $O(nlog(n))$，每层元素都需要排序，最下面一层节点数量最大是n/2+1，时间复杂度为O(nlog(n))

- 空间复杂度: 
> $O(n)$
'''


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        # 计算数组变成有序的最小交换次数
        def getMinSwap(arr):
            indexMap = {}
            for i, num in enumerate(arr):
                indexMap[num] = i
            count = 0
            for i, num in enumerate(sorted(arr)):
                if arr[i] != num:
                    j = indexMap[num]
                    arr[i], arr[j] = arr[j], arr[i]
                    indexMap[arr[i]], indexMap[arr[j]] = i, j
                    count += 1
            return count

        queue = deque()
        queue.append(root)
        ans = 0
        while queue:
            arr = list(map(lambda node: node.val, queue))
            ans += getMinSwap(arr)
            for _ in range(len(arr)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans


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
null = None
assert s.minimumOperations(fromList([1, 4, 3, 7, 6, 8, 5, null, null, null, null, 9, null, 10])) == 3
assert s.minimumOperations(fromList([1, 3, 2, 7, 6, 5, 4])) == 3
assert s.minimumOperations(fromList([1, 2, 3, 4, 5, 6])) == 0
