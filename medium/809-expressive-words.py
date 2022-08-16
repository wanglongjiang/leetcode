'''
809. 情感丰富的文字
有时候人们会用重复写一些字母来表示额外的感受，比如 "hello" -> "heeellooo", "hi" -> "hiii"。我们将相邻字母都相同的一串字符定义为相同字母组，例如："h", "eee", "ll", "ooo"。

对于一个给定的字符串 S ，如果另一个单词能够通过将一些字母组扩张从而使其和 S 相同，我们将这个单词定义为可扩张的（stretchy）。扩张操作定义如下：选择一个字母组（包含字母 c ），
然后往其中添加相同的字母 c 使其长度达到 3 或以上。

例如，以 "hello" 为例，我们可以对字母组 "o" 扩张得到 "hellooo"，但是无法以同样的方法得到 "helloo" 因为字母组 "oo" 长度小于 3。
此外，我们可以进行另一种扩张 "ll" -> "lllll" 以获得 "helllllooo"。如果 S = "helllllooo"，那么查询词 "hello" 是可扩张的，
因为可以对它执行这两种扩张操作使得 query = "hello" -> "hellooo" -> "helllllooo" = S。

输入一组查询单词，输出其中可扩张的单词数量。



示例：

输入：
S = "heeellooo"
words = ["hello", "hi", "helo"]
输出：1
解释：
我们能通过扩张 "hello" 的 "e" 和 "o" 来得到 "heeellooo"。
我们不能通过扩张 "helo" 来得到 "heeellooo" 因为 "ll" 的长度小于 3 。


提示：

0 <= len(S) <= 100。
0 <= len(words) <= 100。
0 <= len(words[i]) <= 100。
S 和所有在 words 中的单词都只由小写字母组成。
'''
from typing import List
'''
思路：双指针
遍历words中的每个单词，检查它是否能扩展成s
检查是否能扩展成s，可以使用双指针

时间复杂度：O(mn),m为len(words),n为len(s)
空间复杂度：O(1)
'''


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        ans = 0
        for word in words:
            ps, pw = 0, 0  # 2个指针分别指向s和word
            while ps < len(s) and pw < len(word):
                if s[ps] == word[pw]:  # 两个字符相同，跳过
                    ps += 1
                    pw += 1
                elif pw > 0 and word[pw - 1] == s[ps]:  # word的上一个字符等于s的当前字符，需要s跳过2个以上
                    count = 0
                    while ps < len(s) and s[ps] == word[pw - 1]:
                        ps += 1
                        count += 1
                    if count < 2:  # 扩展了不到2次，不是合法的扩张单词
                        break
                else:  # 2个字符不同，word的上一个字符不等于s的当前字符，不是扩张单词
                    break
            if ps < len(s) and pw == len(word):  # word遍历完，s未遍历完，需要继续尝试扩展
                while ps < len(s) and s[ps] == word[pw - 1]:
                    ps += 1
            if ps == len(s) and pw == len(word):
                ans += 1
        return ans


s = Solution()
print(s.expressiveWords('heeellooo', ["hello", "hi", "helo"]))
