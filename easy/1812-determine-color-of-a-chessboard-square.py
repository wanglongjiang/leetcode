'''
1812. 判断国际象棋棋盘中一个格子的颜色
简单
19
相关企业
给你一个坐标 coordinates ，它是一个字符串，表示国际象棋棋盘中一个格子的坐标。下图是国际象棋棋盘示意图。



如果所给格子的颜色是白色，请你返回 true，如果是黑色，请返回 false 。

给定坐标一定代表国际象棋棋盘上一个存在的格子。坐标第一个字符是字母，第二个字符是数字。

 

示例 1：

输入：coordinates = "a1"
输出：false
解释：如上图棋盘所示，"a1" 坐标的格子是黑色的，所以返回 false 。
示例 2：

输入：coordinates = "h3"
输出：true
解释：如上图棋盘所示，"h3" 坐标的格子是白色的，所以返回 true 。
示例 3：

输入：coordinates = "c7"
输出：false
 

提示：

coordinates.length == 2
'a' <= coordinates[0] <= 'h'
'1' <= coordinates[1] <= '8'
'''
'''
[TOC]

# 思路
位运算

# 解题方法
将横坐标a、b、c转为0，1，2，将纵坐标1、2、3也转为0、1、2。

观察规律得知，当x,y同为奇数坐标，或者同为偶数坐标时，棋盘是黑色的，否则为白色

算法是首先将纵横坐标转为0，1，2...，然后mod2，如果异或结果为1，为白色，否则为黑色

# 复杂度
- 时间复杂度: 
> $O(n)$ 

- 空间复杂度: 
> $O(1)$
'''


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x, y = ord(coordinates[0]) - ord('a'), int(coordinates[1]) - 1
        return x % 2 ^ y % 2 == 1
