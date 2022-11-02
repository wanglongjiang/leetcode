'''
1016. 子串能表示从 1 到 N 数字的二进制串
给定一个二进制字符串 s 和一个正整数 n，如果对于 [1, n] 范围内的每个整数，其二进制表示都是 s 的 子字符串 ，就返回 true，否则返回 false 。

子字符串 是字符串中连续的字符序列。

 

示例 1：

输入：s = "0110", n = 3
输出：true
示例 2：

输入：s = "0110", n = 4
输出：false
 

提示：

1 <= s.length <= 1000
s[i] 不是 '0' 就是 '1'
1 <= n <= 109
'''
'''
思路：数学
可以遍历s的所有子串，又因为n<=10^9，子串的最大长度为30
所以共有len(s)*30个子串，最多有这么多个数字。
将这些子串转为数字，在一个长度为n的数组中进行标记。
如果有未出现的数字，则返回false
如果所有数字都出现了，返回true

时间复杂度：O(n+len(s))
空间复杂度：O(n)
'''


class Solution:
    def queryString(self, s: str, n: int) -> bool:
        m = len(s)
        if m * 30 < n:
            return False
        marked = [0] * (n + 1)
        for i in range(m):
            for j in range(i + 1, min(i + 30, m + 1)):
                num = int(s[i:j], 2)
                if num <= n:
                    marked[num] = 1
        return all(marked[1:])


s = Solution()
print(s.queryString(s="0110", n=3))
print(s.queryString(s="0110", n=4))
