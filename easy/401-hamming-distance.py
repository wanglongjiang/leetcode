'''
汉明距离
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。
'''
'''
思路1，位移。2个数同时右移，最右边的位如果不同，加1
思路2，BK算法。2个数异或后，用BK算法统计其中1的数量。
'''


class Solution:
    # 思路2
    def hammingDistance(self, x: int, y: int) -> int:
        x ^= y
        i = 0
        while x > 0:
            x = x & (x - 1)
            i += 1
        return i


s = Solution()
print(s.hammingDistance(1, 4))
