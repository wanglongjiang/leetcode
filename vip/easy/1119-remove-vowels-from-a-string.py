'''
1119. 删去字符串中的元音
给你一个字符串 S，请你删去其中的所有元音字母（ 'a'，'e'，'i'，'o'，'u'），并返回这个新字符串。



示例 1：

输入："leetcodeisacommunityforcoders"
输出："ltcdscmmntyfrcdrs"
示例 2：

输入："aeiou"
输出：""


提示：

S 仅由小写英文字母组成。
1 <= S.length <= 1000
'''
'''
思路：一次遍历
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def removeVowels(self, s: str) -> str:
        ans = []
        for c in s:
            if c not in 'aeiou':
                ans.append(c)
        return ''.join(ans)


s = Solution()
print(s.removeVowels("leetcodeisacommunityforcoders") == 'ltcdscmmntyfrcdrs')
print(s.removeVowels('aeiou'))
