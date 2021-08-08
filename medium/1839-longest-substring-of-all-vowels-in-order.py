'''
所有元音按顺序排布的最长子字符串

当一个字符串满足如下条件时，我们称它是 美丽的 ：

所有 5 个英文元音字母（'a' ，'e' ，'i' ，'o' ，'u'）都必须 至少 出现一次。
这些元音字母的顺序都必须按照 字典序 升序排布（也就是说所有的 'a' 都在 'e' 前面，所有的 'e' 都在 'i' 前面，以此类推）
比方说，字符串 "aeiou" 和 "aaaaaaeiiiioou" 都是 美丽的 ，但是 "uaeio" ，"aeoiu" 和 "aaaeeeooo" 不是美丽的 。

给你一个只包含英文元音字母的字符串 word ，请你返回 word 中 最长美丽子字符串的长度 。如果不存在这样的子字符串，请返回 0 。

子字符串 是字符串中一个连续的字符序列。

 

示例 1：

输入：word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
输出：13
解释：最长子字符串是 "aaaaeiiiiouuu" ，长度为 13 。
示例 2：

输入：word = "aeeeiiiioooauuuaeiou"
输出：5
解释：最长子字符串是 "aeiou" ，长度为 5 。
示例 3：

输入：word = "a"
输出：0
解释：没有美丽子字符串，所以返回 0 。
 

提示：

1 <= word.length <= 5 * 10^5
word 只包含字符 'a'，'e'，'i'，'o' 和 'u' 。
'''
'''
思路：状态机
状态机有8个状态：
- 0 是未读入元音字母a之前的状态，此时如果读入a，状态转为1
- 1 是已经读入a，如果读入a，状态转为2；如果读入e，状态转为3；如果读入其他元音字母，状态转为0；如果读入其他字符，状态为2
- 2 是处于持续读入a的状态，如果读入a，状态还是2；如果读入e，状态转为3；如果读入其他元音字母，状态转为0；如果读入其他字符，状态为2
- 3 是读入e的状态，如果读入e，状态为3；如果读入i，状态为4；如果读入a，状态为1；如果读入其他元音，状态转为0；如果读入其他字符，状态为3
- 4 是读入i的状态，如果读入i，状态为4；如果读入o，状态为5；如果读入a，状态为1；如果读入其他元音，状态转为0；如果读入其他字符，状态为4
- 5 是读入o的状态，如果读入o，状态为5；如果读入u，状态为6；如果读入a，状态为1；如果读入其他元音，状态转为0；如果读入其他字符，状态为5
- 6 是读入u的状态，如果读入u，状态为6；如果读入a，状态为1；如果读入其他元音，状态转为0；如果读入其他字符，状态转为7
- 7 是读入u后又读入其他字符的状态，如果读入u状态为6；如果读入a，状态为1；如果读入其他元音，状态转为0；如果读入其他字符，状态为7
将上面的状态机写成二维数组：每个状态为1行；a、e、i、o、u、其他字符分别对应第0、1、2、3、4、5列。
当状态为1时，开始计数，当状态为6时统计长度

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        # 状态机
        sm = [
            [1, 0, 0, 0, 0, 0],  # 未读入元音字母a之前的状态，此时如果读入a，状态转为1
            [2, 3, 0, 0, 0, 2],  # 已经读入a，如果读入a，状态转为2；如果读入e，状态转为3；如果读入其他元音字母，状态转为0；如果读入其他字符，状态为2
            [2, 3, 0, 0, 0, 2],  # 持续读入a的状态，如果读入a，状态还是2；如果读入e，状态转为3；如果读入其他元音字母，状态转为0；如果读入其他字符，状态为2
            [1, 3, 4, 0, 0, 3],  # 读入e的状态，如果读入e，状态为3；如果读入i，状态为4；如果读入a，状态为1；如果读入其他元音，状态转为0；如果读入其他字符，状态为3
            [1, 0, 4, 5, 0, 4],  # 读入i的状态，如果读入i，状态为4；如果读入o，状态为5；如果读入a，状态为1；如果读入其他元音，状态转为0；如果读入其他字符，状态为4
            [1, 0, 0, 5, 6, 5],  # 读入o的状态，如果读入o，状态为5；如果读入u，状态为6；如果读入a，状态为1；如果读入其他元音，状态转为0；如果读入其他字符，状态为5
            [1, 0, 0, 0, 6, 7],  # 读入u的状态，如果读入u，状态为6；如果读入a，状态为1；如果读入其他元音，状态转为0；如果读入其他字符，状态转为7
            [1, 0, 0, 0, 6, 7]  # 读入u后又读入其他字符的状态，如果读入u状态为6；如果读入a，状态为1；如果读入其他元音，状态转为0；如果读入其他字符，状态为7
        ]

        # 取得字符对应状态机里面的列
        def getIdx(ch):
            if ch == 'a':
                return 0
            elif ch == 'e':
                return 1
            elif ch == 'i':
                return 2
            elif ch == 'o':
                return 3
            elif ch == 'u':
                return 4
            else:
                return 5

        state = 0
        start = 0
        ans = 0
        # 遍历所有字符，通过状态机进行处理
        for i in range(len(word)):
            state = sm[state][getIdx(word[i])]
            if state == 1:  # a开始了
                start = i
            elif state == 6:  # 已经到了u
                ans = max(ans, i - start + 1)
        return ans


s = Solution()
print(s.longestBeautifulSubstring('aeiaaioaaaaeiiiiouuuooaauuaeiu'))
print(s.longestBeautifulSubstring('aeeeiiiioooauuuaeiou'))
print(s.longestBeautifulSubstring('a'))
