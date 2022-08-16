'''
1417. 重新格式化字符串
给你一个混合了数字和字母的字符串 s，其中的字母均为小写英文字母。

请你将该字符串重新格式化，使得任意两个相邻字符的类型都不同。也就是说，字母后面应该跟着数字，而数字后面应该跟着字母。

请你返回 重新格式化后 的字符串；如果无法按要求重新格式化，则返回一个 空字符串 。

 

示例 1：

输入：s = "a0b1c2"
输出："0a1b2c"
解释："0a1b2c" 中任意两个相邻字符的类型都不同。 "a0b1c2", "0a1b2c", "0c2a1b" 也是满足题目要求的答案。
示例 2：

输入：s = "leetcode"
输出：""
解释："leetcode" 中只有字母，所以无法满足重新格式化的条件。
示例 3：

输入：s = "1229857369"
输出：""
解释："1229857369" 中只有数字，所以无法满足重新格式化的条件。
示例 4：

输入：s = "covid2019"
输出："c2o0v1i9d"
示例 5：

输入：s = "ab123"
输出："1a2b3"
 

提示：

1 <= s.length <= 500
s 仅由小写英文字母和/或数字组成。
'''
'''
思路：双指针
设2个指针，分别指向数字，字母，将数字、字母交替输出到结果中

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def reformat(self, s: str) -> str:
        ans = []
        char, num, n = 0, 0, len(s)
        while True:
            while char < n and s[char].isdigit():
                char += 1
            if char < n:
                ans.append(s[char])
                char += 1
            else:
                break
            while num < n and not s[num].isdigit():
                num += 1
            if num < n:
                ans.append(s[num])
                num += 1
            else:
                break
        while char < n and s[char].isdigit():  # 尝试将指针移动到最后
            char += 1
        while num < n and not s[num].isdigit():  # 尝试将指针移动到最后
            char += 1
            num += 1
        if char == n and num == n - 1:  # 数字比字母多一个
            return s[num] + ''.join(ans)
        elif char == n and num == n:  # 数字与字母一样多，或者字母多一个
            return ''.join(ans)
        return ''


s = Solution()
print(s.reformat("covid2019"))
print(s.reformat("ab123"))
