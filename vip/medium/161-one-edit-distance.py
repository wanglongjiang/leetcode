'''
161. 相隔为 1 的编辑距离
给定两个字符串 s 和 t，判断他们的编辑距离是否为 1。

注意：

满足编辑距离等于 1 有三种可能的情形：

往 s 中插入一个字符得到 t
从 s 中删除一个字符得到 t
在 s 中替换一个字符得到 t
示例 1：

输入: s = "ab", t = "acb"
输出: true
解释: 可以将 'c' 插入字符串 s 来得到 t。
示例 2:

输入: s = "cab", t = "ad"
输出: false
解释: 无法通过 1 步操作使 s 变为 t。
示例 3:

输入: s = "1203", t = "1213"
输出: true
解释: 可以将字符串 s 中的 '0' 替换为 '1' 来得到 t。
'''
'''
思路：模拟
首先同时遍历2个字符，找到第1个不同的字符
然后尝试：
1. 跳过s的当前字符，对比剩下的字符串是否相同
2. 跳过t的当前字符，对比剩下的字符串是否相同
3. 跳过s、t的当前字符，对比剩下的字符串是否相同
如果满足上面条件之一，则编辑距离为1，否则返回False

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)

        def cmp(i, j):  # 对比2个字符串的i,j之后的部分
            while i < m and j < n:
                if s[i] != t[j]:
                    return False
                i += 1
                j += 1
            return i == m and j == n

        for i in range(min(m, n)):
            if s[i] != t[i]:
                if cmp(i, i + 1):
                    return True
                if cmp(i + 1, i):
                    return True
                if cmp(i + 1, i + 1):
                    return True
                return False
        return False


s = Solution()
print(s.isOneEditDistance(s="ab", t="acb"))
print(s.isOneEditDistance(s="cab", t="ad"))
print(s.isOneEditDistance(s="1203", t="1213"))
