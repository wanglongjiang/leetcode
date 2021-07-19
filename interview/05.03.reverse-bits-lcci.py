'''
面试题 05.03. 翻转数位

给定一个32位整数 num，你可以将一个数位从0变为1。请编写一个程序，找出你能够获得的最长的一串1的长度。

示例 1：

输入: num = 1775(110111011112)
输出: 8
示例 2：

输入: num = 7(01112)
输出: 4
'''
'''
思路：位运算 贪心算法
1. 将所有的连续1的区间都记录下来
2. 将任意2个只间隔1个数字的区间大小相加，最大的2个区间和即为答案

时间复杂度：O(1)，整数最大是32位
空间复杂度：O(1)
'''


class Solution:
    def reverseBits(self, num: int) -> int:
        ranges = []
        for i in range(32):
            if num & (1 << i):
                if ranges and ranges[-1][1] == i - 1:
                    ranges[-1][1] = i
                else:
                    ranges.append([i, i])
        ans = 1  # 最差情况下都是0，只能翻转1位
        if ranges:
            ans = max(map(lambda r: r[1] - r[0] + 2, ranges))  # 区间如果都没有相邻，最坏情况下是单个区间大小+1
            for i in range(1, len(ranges)):
                if (ranges[i][0] - 2) == ranges[i - 1][1]:
                    ans = max(ans, ranges[i][1] - ranges[i][0] + 1 + 1 + ranges[i - 1][1] - ranges[i - 1][0] + 1)
        return ans


s = Solution()
print(s.reverseBits(2147483647))
print(s.reverseBits(1775))
print(s.reverseBits(7))
