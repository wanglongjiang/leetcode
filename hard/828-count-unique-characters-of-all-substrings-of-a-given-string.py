'''
统计子串中的唯一字符

我们定义了一个函数 countUniqueChars(s) 来统计字符串 s 中的唯一字符，并返回唯一字符的个数。

例如：s = "LEETCODE" ，则其中 "L", "T","C","O","D" 都是唯一字符，因为它们只出现一次，所以 countUniqueChars(s) = 5 。

本题将会给你一个字符串 s ，我们需要返回 countUniqueChars(t) 的总和，其中 t 是 s 的子字符串。
注意，某些子字符串可能是重复的，但你统计时也必须算上这些重复的子字符串（也就是说，你必须统计 s 的所有子字符串中的唯一字符）。

由于答案可能非常大，请将结果 mod 10 ^ 9 + 7 后再返回。

 

示例 1：

输入: s = "ABC"
输出: 10
解释: 所有可能的子串为："A","B","C","AB","BC" 和 "ABC"。
     其中，每一个子串都由独特字符构成。
     所以其长度总和为：1 + 1 + 1 + 2 + 2 + 3 = 10
示例 2：

输入: s = "ABA"
输出: 8
解释: 除了 countUniqueChars("ABA") = 1 之外，其余与示例 1 相同。
示例 3：

输入：s = "LEETCODE"
输出：92
 

提示：

0 <= s.length <= 10^4
s 只包含大写英文字符
'''
import collections
'''
对于下标为 ii 的字符 c_ic 
i
​
 ，当它在某个子字符串中仅出现一次时，它会对这个子字符串统计唯一字符时有贡献。只需对每个字符，计算有多少子字符串仅包含该字符一次即可。对于 c_ic 
i
​
 ， 记同字符上一次出现的位置为 c_jc 
j
​
 ，下一次出现的位置为 c_kc 
k
​
 ，那么这样的子字符串就一共有 (c_i - c_j) \times (c_k - c_i)(c 
i
​
 −c 
j
​
 )×(c 
k
​
 −c 
i
​
 ) 种，即子字符串的起始位置有 c_jc 
j
​
 （不含）到 c_ic 
i
​
 （含）之间这 (c_i - c_j)(c 
i
​
 −c 
j
​
 ) 种可能，到结束位置有 (c_k - c_i)(c 
k
​
 −c 
i
​
 ) 种可能。可以预处理 ss，将相同字符的下标放入数组中，方便计算。最后对所有字符进行这种计算即可。
'''


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        index = collections.defaultdict(list)
        for i, c in enumerate(s):
            index[c].append(i)

        res = 0
        for arr in index.values():
            arr = [-1] + arr + [len(s)]
            for i in range(1, len(arr) - 1):
                res += (arr[i] - arr[i - 1]) * (arr[i + 1] - arr[i])
        return res
