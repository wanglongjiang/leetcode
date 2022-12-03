'''
1796. 字符串中第二大的数字
简单
21
相关企业
给你一个混合字符串 s ，请你返回 s 中 第二大 的数字，如果不存在第二大的数字，请你返回 -1 。

混合字符串 由小写英文字母和数字组成。

 

示例 1：

输入：s = "dfa12321afd"
输出：2
解释：出现在 s 中的数字包括 [1, 2, 3] 。第二大的数字是 2 。
示例 2：

输入：s = "abc1111"
输出：-1
解释：出现在 s 中的数字只包含 [1] 。没有第二大的数字。
 

提示：

1 <= s.length <= 500
s 只包含小写英文字母和（或）数字。
'''
'''
[TOC]

# 思路
模拟

# 解题方法

遍历所有字符，找到第2大的


# 复杂度
- 时间复杂度: 
> $O(n)$ 

- 空间复杂度: 
> $O(1)$
'''


class Solution:
    def secondHighest(self, s: str) -> int:
        max1, max2 = -1, -1
        for char in s:
            if char.isdigit():
                if int(char) > max1:
                    max1, max2 = int(char), max1
                elif int(char) != max1 and int(char) > max2:
                    max2 = int(char)
        return max2
