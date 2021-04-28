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
经典的递归教学题
从a移动到c，
如果a上面只有1个盘子，可以将a内的元素直接给c
否则需要使用b作为中介：
    首先递归将a的1..n-1个盘子通过c移动到b
    然后将a的第0个盘子移动到c
    最后递归将b的1..n-1个盘子通过a移动到c
时间复杂度：O(2^n-1)
'''


class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        def move(n, src, buffer, dst):
            if n == 1:
                dst.append(src.pop())
            else:
                move(n - 1, src, dst, buffer)
                dst.append(src.pop())
                move(n - 1, buffer, src, dst)

        move(len(A), A, B, C)


s = Solution()
A = [2, 1, 0]
B = []
C = []
s.hanota(A, B, C)
print(A, B, C)
