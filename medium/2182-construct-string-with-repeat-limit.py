'''
2182. 构造限制重复的字符串
给你一个字符串 s 和一个整数 repeatLimit ，用 s 中的字符构造一个新字符串 repeatLimitedString ，
使任何字母 连续 出现的次数都不超过 repeatLimit 次。你不必使用 s 中的全部字符。

返回 字典序最大的 repeatLimitedString 。

如果在字符串 a 和 b 不同的第一个位置，字符串 a 中的字母在字母表中出现时间比字符串 b 对应的字母晚，
则认为字符串 a 比字符串 b 字典序更大 。如果字符串中前 min(a.length, b.length) 个字符都相同，那么较长的字符串字典序更大。

 

示例 1：

输入：s = "cczazcc", repeatLimit = 3
输出："zzcccac"
解释：使用 s 中的所有字符来构造 repeatLimitedString "zzcccac"。
字母 'a' 连续出现至多 1 次。
字母 'c' 连续出现至多 3 次。
字母 'z' 连续出现至多 2 次。
因此，没有字母连续出现超过 repeatLimit 次，字符串是一个有效的 repeatLimitedString 。
该字符串是字典序最大的 repeatLimitedString ，所以返回 "zzcccac" 。
注意，尽管 "zzcccca" 字典序更大，但字母 'c' 连续出现超过 3 次，所以它不是一个有效的 repeatLimitedString 。
示例 2：

输入：s = "aababab", repeatLimit = 2
输出："bbabaa"
解释：
使用 s 中的一些字符来构造 repeatLimitedString "bbabaa"。 
字母 'a' 连续出现至多 2 次。 
字母 'b' 连续出现至多 2 次。 
因此，没有字母连续出现超过 repeatLimit 次，字符串是一个有效的 repeatLimitedString 。 
该字符串是字典序最大的 repeatLimitedString ，所以返回 "bbabaa" 。 
注意，尽管 "bbabaaa" 字典序更大，但字母 'a' 连续出现超过 2 次，所以它不是一个有效的 repeatLimitedString 。
 

提示：

1 <= repeatLimit <= s.length <= 10^5
s 由小写英文字母组成
'''
'''
思路：贪心
首先对s中所有字符进行计数，
然后找到字典序最大的字符，用掉min(repeatLimit,字符个数)个，然后选次大的字符，用掉1个
重复上面过程，直至所有字符都被用光或者最后的字符重复repeatLimit个

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        ans = []
        count = [0] * 26
        for char in s:  # 对所有字符进行计数
            count[ord(char) - ord('a')] += 1
        largest, nlargest = 25, 24
        length = 0
        while True:
            for largest in range(largest, -1, -1):  # 找到最大字符
                if count[largest] > 0:
                    charNum = min(repeatLimit, count[largest])
                    char = chr(largest + ord('a'))
                    if ans and ans[-1] == char:  # 上次的结尾就是本字符，需要控制次数
                        lastCount = 0
                        for i in range(len(ans) - 1, -1, -1):  # 查找字符串末尾当前字符个数
                            if ans[i] != char:
                                break
                            lastCount += 1
                        charNum = min(repeatLimit - lastCount, count[largest])  # 重新计算可以追加的字符数
                    count[largest] -= charNum
                    for i in range(charNum):
                        ans.append(char)
                    break
            for nlargest in range(largest - 1, -1, -1):  # 找到次大字符
                if count[nlargest] > 0:
                    ans.append(chr(nlargest + ord('a')))
                    count[nlargest] -= 1
                    break
            if length != len(ans):  # 如果一次处理没有增加长度，说明无法再追加字符，需要退出
                length = len(ans)
            else:
                break
        return ''.join(ans)


s = Solution()
print(s.repeatLimitedString(s="cczazcc", repeatLimit=3))
print(s.repeatLimitedString(s="aababab", repeatLimit=2))
