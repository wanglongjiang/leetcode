'''
2299. 强密码检验器 II
如果一个密码满足以下所有条件，我们称它是一个 强 密码：

它有至少 8 个字符。
至少包含 一个小写英文 字母。
至少包含 一个大写英文 字母。
至少包含 一个数字 。
至少包含 一个特殊字符 。特殊字符为："!@#$%^&*()-+" 中的一个。
它 不 包含 2 个连续相同的字符（比方说 "aab" 不符合该条件，但是 "aba" 符合该条件）。
给你一个字符串 password ，如果它是一个 强 密码，返回 true，否则返回 false 。

 

示例 1：

输入：password = "IloveLe3tcode!"
输出：true
解释：密码满足所有的要求，所以我们返回 true 。
示例 2：

输入：password = "Me+You--IsMyDream"
输出：false
解释：密码不包含数字，且包含 2 个连续相同的字符。所以我们返回 false 。
示例 3：

输入：password = "1aB!"
输出：false
解释：密码不符合长度要求。所以我们返回 false 。
 

提示：

1 <= password.length <= 100
password 包含字母，数字和 "!@#$%^&*()-+" 这些特殊字符。
'''
'''
思路：模拟
模拟题目要求，进行判断
时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        hasLower, hasUpper, hasNum, hasSpec = False, False, False, False
        prev = None
        for char in password:
            if prev == char:
                return False
            prev = char
            hasLower = hasLower or char.islower()
            hasUpper = hasUpper or char.isupper()
            hasNum = hasNum or char.isdigit()
            hasSpec = hasSpec or '!@#$%^&*()-+'.find(char) >= 0
        return hasLower and hasUpper and hasNum and hasSpec


s = Solution()
print(s.strongPasswordCheckerII("11A!A!Aa"))
