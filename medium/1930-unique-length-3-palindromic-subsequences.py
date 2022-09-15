'''
1930. 长度为 3 的不同回文子序列
给你一个字符串 s ，返回 s 中 长度为 3 的不同回文子序列 的个数。

即便存在多种方法来构建相同的子序列，但相同的子序列只计数一次。

回文 是正着读和反着读一样的字符串。

子序列 是由原字符串删除其中部分字符（也可以不删除）且不改变剩余字符之间相对顺序形成的一个新字符串。

例如，"ace" 是 "abcde" 的一个子序列。
 

示例 1：

输入：s = "aabca"
输出：3
解释：长度为 3 的 3 个回文子序列分别是：
- "aba" ("aabca" 的子序列)
- "aaa" ("aabca" 的子序列)
- "aca" ("aabca" 的子序列)
示例 2：

输入：s = "adc"
输出：0
解释："adc" 不存在长度为 3 的回文子序列。
示例 3：

输入：s = "bbcbaba"
输出：4
解释：长度为 3 的 4 个回文子序列分别是：
- "bbb" ("bbcbaba" 的子序列)
- "bcb" ("bbcbaba" 的子序列)
- "bab" ("bbcbaba" 的子序列)
- "aba" ("bbcbaba" 的子序列)
 

提示：

3 <= s.length <= 105
s 仅由小写英文字母组成
'''
'''
思路：前缀和 哈希
1. 遍历字符串s：
- 统计每个字符首次出现和最后一次出现的索引；
- 统计每个字符出现的次数；
- 统计字符出现次数的前缀和数组。
2. 对于每个出现2次以上的字符，通过首次出现索引、最后一次出现的索引、前缀和数组得到被该字符包围的字符个数，也就是回文序列的个数。

时间复杂度：O(n)
空间复杂度：O(26n)
'''


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        firstIdxs, lastIdxs = [-1] * 26, [0] * 26  # 统计字符首次出现和最后一次出现的索引
        counts = [0] * 26  # 统计字符出现个数
        pre = [None] * len(s)  # 字符计数的前缀和数组
        for i in range(len(s)):
            charIdx = ord(s[i]) - ord('a')
            counts[charIdx] += 1  # 字符计数+1
            if firstIdxs[charIdx] < 0:  # 记录第1次出现字符的索引
                firstIdxs[charIdx] = i
            lastIdxs[charIdx] = i  # 记录最后一次出现字符的索引
            if i == 0:
                pre[i] = [0] * 26
            else:
                pre[i] = pre[i - 1].copy()
            pre[i][charIdx] += 1  # 前缀和数组更新
        ans = 0
        for charIdx in range(26):
            if counts[charIdx] >= 2:
                left, right = pre[firstIdxs[charIdx]], pre[lastIdxs[charIdx]]  # 找到前缀和数组
                innerCount = [right[i] - left[i] for i in range(26)]  # 计算2个相同字符内包围的字符数
                innerCount[charIdx] -= 1  # 需要将当前字符的作为边界时字符都删除，以只保留内部被包围的计数
                for innerIdx in range(26):
                    if innerCount[innerIdx] > 0:  # 与超过0个的字符能构成回文
                        ans += 1
        return ans


s = Solution()
print(s.countPalindromicSubsequence("aabca"))
print(s.countPalindromicSubsequence("bbcbaba"))
print(s.countPalindromicSubsequence("adc"))
