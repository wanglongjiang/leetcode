'''
[TOC]

# 思路
小学数学交换律

# 解题方法
因为只能交换相邻字符，所以类似于冒泡排序，每个0需要从右侧移动到左侧，需要移动的距离是与其交换的最左侧1的距离，也即2个字符的下标之差。
设字符串中有m个0，那么左侧m个字符中如果有x个0，m-x个1，这些1需要与右侧同样数量的0进行交换位置。
他们的交换步数之和是：zero[0]-one[0]+zero[1]-one[1]+...+zero[m-x-1]-one[m-x-1]，根据小学学到的加法交换律，
（zero[0]+zero[1]+...+zero[m-x-1]）-(one[0]+one[1]+...+one[m-x-1])

也即所有需要交换的0的下标之和，减去所有需要交换的1的下标之和。从公式中可以看出，左侧的哪个1跟右侧的哪个0交换都是一样的。

# 复杂度
- 时间复杂度: 
> $O(n)$ ，2次遍历数组

- 空间复杂度: 
> $O(1)$
'''
class Solution:
    def minimumSteps(self, s: str) -> int:
        m = s.count('0') # 统计0的个数
        oneIdxSum = sum(i for i,ch in enumerate(s[:m]) if ch=='1') # 统计左侧需要交换的1的下标和
        zeroIdxSum = sum(i+m for i,ch in enumerate(s[m:]) if ch=='0') # 统计右侧需要交换的0的下标和
        return zeroIdxSum-oneIdxSum
    
        