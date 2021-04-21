'''
面试题 05.04. 下一个数
下一个数。给定一个正整数，找出与其二进制表达式中1的个数相同且大小最接近的那两个数（一个略大，一个略小）。

提示:

num的范围在[1, 2147483647]之间；
如果找不到前一个或者后一个满足条件的正数，那么输出 -1。
'''
from typing import List
'''
思路：位运算
如果num的二进制最高位的1之前的低位中有0存在，暂时把它称为有洞的数
对于有洞的数，肯定有满足条件的2个数与它1的位数相同，略大或略小。
    比它略大的数为最低位的0右边的1左移一位，0右边的1向右紧缩
    比它略小的数为最低位的0左边的1右移1位，再右边的1向左紧缩
对于全是1的数，比它略小的数不存在，按照题目返回-1
    如果该数为2^31-1，也就是2147483647，比它略大的数也不存在。

时间复杂度：O(1)
空间复杂度：O(1)
'''


class Solution:
    def findClosedNumbers(self, num: int) -> List[int]:
        if num == 2147483647:
            return [-1, -1]
        print(bin(num))
        low0 = (~num) & (-(~num))  # num求反可以将0变成1，然后num&-num可以提取出最低位的0变成的1
        if low0 > num:  # 如果最低位的0变成1大于该数，说明该数字的低位二进制中全是1，略小的数不存在
            if (num << 1) > 2147483647:  # 超过上界
                return [-1, -1]
            else:
                return [num << 1, -1]
        if low0 == 1:  # 0右边没有1，略大的数是第1个左边为0的1向左进位，右边的1全都向右紧缩，略小的数是最低位的1右移1位
            low1 = num & (-num)
            low1left0 = low1
            while low1left0 & num:
                low1left0 <<= 1
            mask = 0
            low1left1 = low1left0 >> 1
            if num & (low1left1 - 1):  # 右边有1，需要将1进行向右靠齐
                t = num & (low1left1 - 1)
                while t:
                    t = t & (t - 1)
                    mask = mask << 1 | 1
            h = (num | low1left0) & ~(low1left0 >> 1)
            if mask:
                h = h & ~(low1left1 - 1) | mask
            if h > 2147483647:
                h = -1
            low = num & (~low1) | (low1 >> 1)
            return [h, low]
        else:  # 0的右边有1，略大的数是最低位的0变成1，最低位的0右边的1变成0，略小的数是最低位的0左边的1右移1位，该位之后的1全部向左紧缩
            h = (num | low0) & (~(low0 >> 1))
            if h > 2147483647:
                h = -1
            low0left1 = low0
            while (low0left1 & num) == 0:  # 找到最低位的0左边的1
                low0left1 <<= 1
            # 统计左边的1的低位有多少个1
            left = (low0left1 - 1) & num
            num = num & ~left
            left1Count = 0
            while left:
                left = left & (left - 1)
                left1Count += 1
            mask = 0
            if left1Count > 0:
                while left1Count:
                    mask = mask << 1 | 1
                    left1Count -= 1
                while mask & (low0left1 >> 1) == 0:
                    mask <<= 1
                mask >>= 1
            low = num & (~low0left1) | (low0left1 >> 1) | mask
            return [h, low]


s = Solution()
print(s.findClosedNumbers(124))
print(s.findClosedNumbers(67))
print(s.findClosedNumbers(34))
print(s.findClosedNumbers(5))
print(s.findClosedNumbers(2))
print(s.findClosedNumbers(1))
print(s.findClosedNumbers(4))
