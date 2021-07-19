'''
面试题 10.01. 合并排序的数组
给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。

初始化 A 和 B 的元素数量分别为 m 和 n。

示例:

输入:
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
说明:

A.length == n + m
'''
from typing import List
'''
思路：从右向左依次填充A的空白位置
从A、B的最大元素开始对比，先取较大的元素，将其复制到A的最右侧空白位置

时间复杂度：O(m+n)
空间复杂度：O(1)
'''


class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        pa, pb, pc = m - 1, n - 1, m + n - 1  # 3个指针分别指向a的最后一个元素、b的最后一个元素、a的最后一个空白位置
        while pb >= 0:  # 直至b的所有元素都被复制完毕
            if pa < 0 or A[pa] <= B[pb]:  # 如果A数组的元素全部被复制完毕，或者B数组元素更大，复制B数组元素到A
                A[pc] = B[pb]
                pb -= 1
            else:
                A[pc] = A[pa]
                pa -= 1
            pc -= 1


s = Solution()
print(s.merge(A=[1, 2, 3, 0, 0, 0], m=3, B=[2, 5, 6], n=3))
