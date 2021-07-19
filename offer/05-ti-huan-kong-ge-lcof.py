'''
剑指 Offer 05. 替换空格

请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

 

示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."
 

限制：

0 <= s 的长度 <= 10000
'''
'''
思路1，直接连结字符串
时间复杂度：O(n)

思路2，用list进行缓存，最后连结成字符串
时间复杂度：O(n)
'''


class Solution:
    # 思路1，直接连结字符串，考验编译器的优化
    def replaceSpace1(self, s: str) -> str:
        ans = ''
        for i in range(len(s)):
            ans += '%20' if s[i] == ' ' else s[i]
        return ans

    # 思路2，用list辅助
    def replaceSpace(self, s: str) -> str:
        li = []
        for i in range(len(s)):
            li.append('%20' if s[i] == ' ' else s[i])
        return ''.join(li)
