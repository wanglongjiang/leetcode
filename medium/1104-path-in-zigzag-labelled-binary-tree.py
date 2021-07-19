'''
二叉树寻路
在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 逐行 依次按 “之” 字形进行标记。

如下图所示，在奇数行（即，第一行、第三行、第五行……）中，按从左到右的顺序进行标记；

而偶数行（即，第二行、第四行、第六行……）中，按从右到左的顺序进行标记。



给你树上某一个节点的标号 label，请你返回从根节点到该标号为 label 节点的路径，该路径是由途经的节点标号所组成的。

 

示例 1：

输入：label = 14
输出：[1,3,4,14]
示例 2：

输入：label = 26
输出：[1,2,6,10,26]
 

提示：

1 <= label <= 10^6
'''
from typing import List
'''
思路：迭代
设父节点编号为i（从1开始），则左右子节点分别为2i,2i+1
目前已知label，label=2^0+2^1+2^2+...+2^(level-2)+x
通过迭代过程，label减去2的幂，可以得到目前的层数level
用一个迭代过程，减少level直至第1层，在这个过程中根据no得到label=2^(level)-no+2^(level-1)-1，计算得到父编号parentNo = no/2

时间复杂度：O(log(label))
空间复杂度：O(1)
'''


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # 第1次迭代，求出层数和label的编号
        level = 1
        while (1 << level) - 1 < label:
            level += 1
        no = label  # 奇数行,no为label
        if level % 2 == 0:  # 求偶数行的no，为2^(level)-label+2^(level-1)-1
            no = (1 << level) - label + (0 if level == 1 else (1 << (level - 1))) - 1
        # 第2次迭代，求出自底向上经过的路径上的label
        ans = []
        ans.append(label)
        while level > 1:
            no = max(no >> 1, 1)
            level -= 1
            if level % 2:  # 奇数行的no与label相同
                label = no
            else:  # 求偶数行的label，为2^(level)-no+2^(level-1)-1
                label = (1 << level) - no + (0 if level == 1 else (1 << (level - 1))) - 1
            ans.append(label)
        ans.reverse()
        return ans


s = Solution()
print(s.pathInZigZagTree(8) == [1, 2, 7, 8])
print(s.pathInZigZagTree(4) == [1, 3, 4])
print(s.pathInZigZagTree(7) == [1, 2, 7])
print(s.pathInZigZagTree(3) == [1, 3])
print(s.pathInZigZagTree(2) == [1, 2])
print(s.pathInZigZagTree(14) == [1, 3, 4, 14])
print(s.pathInZigZagTree(26) == [1, 2, 6, 10, 26])
print(s.pathInZigZagTree(1) == [1])
print(s.pathInZigZagTree(15) == [1, 3, 4, 15])
print(s.pathInZigZagTree(13) == [1, 3, 5, 13])
print(s.pathInZigZagTree(16) == [1, 3, 4, 15, 16])
