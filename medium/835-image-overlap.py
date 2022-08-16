'''
835. 图像重叠
给你两个图像 img1 和 img2 ，两个图像的大小都是 n x n ，用大小相同的二维正方形矩阵表示。（并且为二进制矩阵，只包含若干 0 和若干 1 ）

转换其中一个图像，向左，右，上，或下滑动任何数量的单位，并把它放在另一个图像的上面。之后，该转换的 重叠 是指两个图像都具有 1 的位置的数目。

（请注意，转换 不包括 向任何方向旋转。）

最大可能的重叠是多少？



示例 1：


输入：img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
输出：3
解释：将 img1 向右移动 1 个单位，再向下移动 1 个单位。

两个图像都具有 1 的位置的数目是 3（用红色标识）。

示例 2：

输入：img1 = [[1]], img2 = [[1]]
输出：1
示例 3：

输入：img1 = [[0]], img2 = [[0]]
输出：0


提示：

n == img1.length
n == img1[i].length
n == img2.length
n == img2[i].length
1 <= n <= 30
img1[i][j] 为 0 或 1
img2[i][j] 为 0 或 1
'''
from typing import List
'''
思路：位运算
因为n最大是30，可以将矩阵的一行压缩为一个整数。
然后将矩阵上下、左右移位0..n-1位，与另外一个矩阵进行重叠，对比1的个数。

时间复杂度：O(n^4)
空间复杂度：O(n)
'''


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        # 状态压缩，bitmap1的上下各添加了n-1行0，是为了上下移动时简化算法
        bitmap1, bitmap2 = [0] * (3 * n - 1), [0] * n
        for i in range(n):
            for j in range(n):
                bitmap1[n - 1 + i] |= img1[i][j] << j
        for i in range(n):
            for j in range(n):
                bitmap2[i] |= img2[i][j] << j
        # 用2重循环上下左右移动bitmap1，与bitmap2进行重叠
        ans = 0
        for roffset in range(2 * n - 1):  # 上下移动
            for coffset in range(1, n):  # 左移
                count = 0
                for i in range(n):
                    count += self.bitCount((bitmap1[roffset + i] << coffset) & bitmap2[i])
                ans = max(ans, count)
            for coffset in range(n):  # 右移
                count = 0
                for i in range(n):
                    count += self.bitCount((bitmap1[roffset + i] >> coffset) & bitmap2[i])
                ans = max(ans, count)
        return ans

    # 对整数num中1的个数计数
    def bitCount(self, num):
        count = 0
        while num:
            num &= num - 1
            count += 1
        return count


s = Solution()
print(s.largestOverlap(img1=[[1, 1, 0], [0, 1, 0], [0, 1, 0]], img2=[[0, 0, 0], [0, 1, 1], [0, 0, 1]]))
print(s.largestOverlap(img1=[[1]], img2=[[1]]))
print(s.largestOverlap(img1=[[0]], img2=[[0]]))
