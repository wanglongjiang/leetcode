'''
剑指 Offer 50. 第一个只出现一次的字符

在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:

s = "abaccdeff"
返回 "b"

s = ""
返回 " "
 

限制：

0 <= s 的长度 <= 50000
'''
'''
思路：计数
用大小为26的数组记录各个字符出现的次数，用大小为26的数组记录每个字符第1次出现的索引
最后输出次数为1的字符中最早出现的1个

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def firstUniqChar(self, s: str) -> str:
        counter, indexs, charBase = [0] * 26, [-1] * 26, ord('a')
        for i in range(len(s)):
            charIndex = ord(s[i]) - charBase
            counter[charIndex] += 1
            if indexs[charIndex] < 0:
                indexs[charIndex] = i
        minIndex = float('inf')
        for i in range(26):  # 遍历所有字符出现次数，找到出现次数为1的字符中最早出现的1个
            if counter[i] == 1 and minIndex > indexs[i]:
                minIndex = indexs[i]
        return ' ' if minIndex == float('inf') else s[minIndex]


s = Solution()
print(s.firstUniqChar('leetcode'))
