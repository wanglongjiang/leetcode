'''
面试题 08.06. 汉诺塔问题
在经典汉诺塔问题中，有 3 根柱子及 N 个不同大小的穿孔圆盘，盘子可以滑入任意一根柱子。一开始，所有盘子自上而下按升序依次套在第一根柱子上(即每一个盘子只能放在更大的盘子上面)。
移动圆盘时受到以下限制:
(1) 每次只能移动一个盘子;
(2) 盘子只能从柱子顶端滑出移到下一根柱子;
(3) 盘子只能叠在比它大的盘子上。

请编写程序，用栈将所有盘子从第一根柱子移到最后一根柱子。

你需要原地修改栈。
提示:

A中盘子的数目不大于14个。
'''
from typing import List
'''
思路：递归
TODO
'''


class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        if len(A) == 1 and len(B) == 0 and C[-1] > A[0]:
            C.append(A.pop())
        elif len(A) == 2 and len(B) == 0:
            B.append(A.pop())
            C.append(A.pop())
            C.append(B.pop())
        else:
            self.hanota(A[1:], C, B)
            C.append(A.pop())
            self.hanota(B, A, C)
