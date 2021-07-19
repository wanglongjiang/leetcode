'''
面试题 05.08. 绘制直线
绘制直线。有个单色屏幕存储在一个一维数组中，使得32个连续像素可以存放在一个 int 里。屏幕宽度为w，
且w可被32整除（即一个 int 不会分布在两行上），屏幕高度可由数组长度及屏幕宽度推算得出。请实现一个函数，绘制从点(x1, y)到点(x2, y)的水平线。

给出数组的长度 length，宽度 w（以比特为单位）、直线开始位置 x1（比特为单位）、直线结束位置 x2（比特为单位）、直线所在行数 y。返回绘制过后的数组。

示例1:

 输入：length = 1, w = 32, x1 = 30, x2 = 31, y = 0
 输出：[3]
 说明：在第0行的第30位到第31为画一条直线，屏幕表示为[0b000000000000000000000000000000011]
示例2:

 输入：length = 3, w = 96, x1 = 0, x2 = 95, y = 0
 输出：[-1, -1, -1]
'''
from typing import List
'''
思路：数组 位运算
设wsize=w/32得到表示一行需要多少个整数
需要返回一个大小为length的数组

可以从x1遍历到x2，该bit的定位方式是：
> 首先确定整数的索引i = y*wsize + x//32
> 然后bit索引是高位为0，低位为31，那么bitOffset = 31-x%32
> 将1<<bitOffset与nums[i]执行或操作即可

时间复杂度：O(length+(x2-x1))
空间复杂度：O(1)
'''


class Solution:
    def drawLine(self, length: int, w: int, x1: int, x2: int, y: int) -> List[int]:
        ans = [0] * length
        wsize = w // 32
        for x in range(x1, x2 + 1):
            i = y * wsize + x // 32
            bitOffset = 31 - (x % 32)
            ans[i] |= 1 << bitOffset
        return ans
