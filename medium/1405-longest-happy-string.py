'''
1405. 最长快乐字符串
如果字符串中不含有任何 'aaa'，'bbb' 或 'ccc' 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。

给你三个整数 a，b ，c，请你返回 任意一个 满足下列全部条件的字符串 s：

s 是一个尽可能长的快乐字符串。
s 中 最多 有a 个字母 'a'、b 个字母 'b'、c 个字母 'c' 。
s 中只含有 'a'、'b' 、'c' 三种字母。
如果不存在这样的字符串 s ，请返回一个空字符串 ""。

 

示例 1：

输入：a = 1, b = 1, c = 7
输出："ccaccbcc"
解释："ccbccacc" 也是一种正确答案。
示例 2：

输入：a = 2, b = 2, c = 1
输出："aabbc"
示例 3：

输入：a = 7, b = 1, c = 0
输出："aabaa"
解释：这是该测试用例的唯一正确答案。
 

提示：

0 <= a, b, c <= 100
a + b + c > 0
'''
from collections import Counter
'''
思路：贪心
遍历3个变量，
    每次都取最大的那个变量，如果其与输出最后一个字符不同，将其减2，输出字符串增加2个字符，
    然后取次大的变量，输出字符串增加1个字符。
重复上述过程，直至有2个变量变为0，详见代码注释

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        counter = Counter({'a': a, 'b': b, 'c': c})
        ans = ''
        while True:
            li = counter.most_common(2)
            if li[0][1] == 0:  # 最多的字符为0，退出
                break
            if len(ans) == 0 or li[0][0] != ans[-1]:  # 输出的最后一个字符与最大字符不相同才输出最大字符
                if li[0][1] == 1:  # 最多的字符只剩一个，输出1个字符
                    ans += li[0][0]
                    counter[li[0][0]] -= 1
                elif li[0][1] > 1:  # 最多的字符超过1个，输出2个字符
                    ans += li[0][0] + li[0][0]
                    counter[li[0][0]] -= 2
                if li[1][1] == 0:  # 剩余的2个字符个数为0，退出
                    break
            ans += li[1][0]
            counter[li[1][0]] -= 1
        return ans


s = Solution()
print(s.longestDiverseString(4, 4, 3))
print(s.longestDiverseString(a=1, b=1, c=7))
print(s.longestDiverseString(a=2, b=2, c=1))
print(s.longestDiverseString(a=7, b=1, c=0))
