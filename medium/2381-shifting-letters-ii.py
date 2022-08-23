'''
2381. 字母移位 II
给你一个小写英文字母组成的字符串 s 和一个二维整数数组 shifts ，其中 shifts[i] = [starti, endi, directioni] 。
对于每个 i ，将 s 中从下标 starti 到下标 endi （两者都包含）所有字符都进行移位运算，如果 directioni = 1 将字符向后移位，如果 directioni = 0 将字符向前移位。

将一个字符 向后 移位的意思是将这个字符用字母表中 下一个 字母替换（字母表视为环绕的，所以 'z' 变成 'a'）。
类似的，将一个字符 向前 移位的意思是将这个字符用字母表中 前一个 字母替换（字母表是环绕的，所以 'a' 变成 'z' ）。

请你返回对 s 进行所有移位操作以后得到的最终字符串。

 

示例 1：

输入：s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
输出："ace"
解释：首先，将下标从 0 到 1 的字母向前移位，得到 s = "zac" 。
然后，将下标从 1 到 2 的字母向后移位，得到 s = "zbd" 。
最后，将下标从 0 到 2 的字符向后移位，得到 s = "ace" 。
示例 2:

输入：s = "dztz", shifts = [[0,0,0],[1,1,1]]
输出："catz"
解释：首先，将下标从 0 到 0 的字母向前移位，得到 s = "cztz" 。
最后，将下标从 1 到 1 的字符向后移位，得到 s = "catz" 。
 

提示：

1 <= s.length, shifts.length <= 5 * 104
shifts[i].length == 3
0 <= starti <= endi < s.length
0 <= directioni <= 1
s 只包含小写英文字母。
'''

from typing import List
'''
思路：差分数组
设一个与s等长的差分数组，将shifts中对区间的移动指令更新到差分数组上去，所有的shifts计算完毕之后，能够得到每个字符需要移位的次数
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)
        for shift in shifts:
            if shift[2]:  # 向右移动
                diff[shift[0]] += 1
                diff[shift[1] + 1] -= 1
            else:
                diff[shift[0]] -= 1
                diff[shift[1] + 1] += 1
        for i in range(1, n):  # 计算每个位置上的字符需要移位的次数，正数代表向后移位，负数代表向前移位
            diff[i] += diff[i - 1]
        ans = []
        for i in range(n):
            char = ord(s[i]) + diff[i] % 26  # 计算出移位后的字符ascii码
            if char > ord('z'):  # 移位后超过'z'，需要从'a'再开始
                char = char - ord('z') + ord('a') - 1
            ans.append(chr(char))
        return ''.join(ans)


s = Solution()
print(s.shiftingLetters(s="abc", shifts=[[0, 1, 0], [1, 2, 1], [0, 2, 1]]))
print(s.shiftingLetters(s="dztz", shifts=[[0, 0, 0], [1, 1, 1]]))
