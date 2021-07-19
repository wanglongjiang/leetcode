'''
面试题 05.07. 配对交换
配对交换。编写程序，交换某个整数的奇数位和偶数位，尽量使用较少的指令（也就是说，位0与位1交换，位2与位3交换，以此类推）。

示例1:

 输入：num = 2（或者0b10）
 输出 1 (或者 0b01)
示例2:

 输入：num = 3
 输出：3
提示:

num的范围在[0, 2^30 - 1]之间，不会发生整数溢出。
'''
'''
思路：位运算
异或的各种操作，详细算法见代码

时间复杂度：O(1)
空间复杂度：O(1)
'''


class Solution:
    def exchangeBits(self, num: int) -> int:
        xor = num ^ (num << 1)
        a = (xor >> 1) ^ num  # 得到结果是1,2,3,4,5..位
        b = xor ^ num  # 得到的结果是0,0,1,2,3,4..位
        mask = 0
        for i in range(0, 32, 2):
            mask |= 1 << i
        return (a & mask) | (b & (mask >> 1))


s = Solution()
print(s.exchangeBits(2))
print(s.exchangeBits(3))
