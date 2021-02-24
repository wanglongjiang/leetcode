'''
翻转图像

给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。

水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。

反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。

'''
from typing import List
'''
思路：简单题目，双指针交换，异或1取反
'''


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        n = len(A)
        for nums in A:
            for i in range(n // 2 + n % 2):
                nums[i], nums[n - 1 - i] = nums[n - 1 - i] ^ 0x1, nums[i] ^ 0x1
        return A


s = Solution()
print(s.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
print(
    s.flipAndInvertImage([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1],
                          [1, 0, 1, 0]]))
