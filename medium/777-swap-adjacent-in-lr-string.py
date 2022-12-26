'''
777. 在LR字符串中交换相邻字符
在一个由 'L' , 'R' 和 'X' 三个字符组成的字符串（例如"RXXLRXRXL"）中进行移动操作。
一次移动操作指用一个"LX"替换一个"XL"，或者用一个"XR"替换一个"RX"。
现给定起始字符串start和结束字符串end，请编写代码，当且仅当存在一系列移动操作使得start可以转换成end时， 返回True。

 

示例 :

输入: start = "RXXLRXRXL", end = "XRLXXRRLX"
输出: True
解释:
我们可以通过以下几步将start转换成end:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
 

提示：

1 <= len(start) = len(end) <= 10000。
start和end中的字符串仅限于'L', 'R'和'X'。
'''
'''
思路：双指针
从题意中得知，L可以穿过X向左移动，R可以穿过X向右移动。
同一个下标，如果start[left]==end[left]，可以跳过。
同一个下标，如果start[left]为'X'，end[left]为'L'，那么可以视为将start[left]右边某个'L'（设下标为right)移动到下标left，left和right之间不能有R
同一个下标，如果start[left]为'R'，end[left]为'X'，那么可以视为将start[left]处的'R'向右移动到右边某个'X'（设下标为right)，left和right之间不能有L
除上述3种情况，其他都不能移动。

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        start, end = list(start), list(end)
        left, right, n = 0, 0, len(start)
        while left < n:
            while left < n and start[left] == end[left]:  # 跳过相同的字符
                left += 1
            right = left
            if left < n:
                if start[left] == 'X' and end[left] == 'L':
                    while right < n and start[right] == 'X':
                        right += 1
                    if right < n and start[right] == 'L':
                        start[left], start[right] = start[right], start[left]  # 将'L'移动到左边
                    else:
                        return False  # 找不到匹配的'L'
                elif start[left] == 'R' and end[left] == 'X':
                    while right < n and start[right] == 'R':
                        right += 1
                    if right < n and start[right] == 'X':
                        start[left], start[right] = start[right], start[left]  # 将'R'移动到右边
                    else:
                        return False  # 找不到匹配的'X'
                else:
                    return False
                left += 1
        return True
