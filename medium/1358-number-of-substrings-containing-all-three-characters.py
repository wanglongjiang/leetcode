'''
1358. 包含所有三种字符的子字符串数目
给你一个字符串 s ，它只包含三种字符 a, b 和 c 。

请你返回 a，b 和 c 都 至少 出现过一次的子字符串数目。

 

示例 1：

输入：s = "abcabc"
输出：10
解释：包含 a，b 和 c 各至少一次的子字符串为 "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" 和 "abc" (相同字符串算多次)。
示例 2：

输入：s = "aaacb"
输出：3
解释：包含 a，b 和 c 各至少一次的子字符串为 "aaacb", "aacb" 和 "acb" 。
示例 3：

输入：s = "abc"
输出：1
 

提示：

3 <= s.length <= 5 x 10^4
s 只包含字符 a，b 和 c 。
'''
'''
思路：滑动窗口
设2个指针left,right，使其构成的滑动窗口内包含a,b,c全部字符，每移动一次滑动窗口，就累加以left开头的子串数量

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n, right = len(s), 0
        a, b, c = 0, 0, 0
        ans = 0
        for left in range(n):
            # 当窗口内的字符不满足时，扩大窗口
            while right < n and not (a > 0 and b > 0 and c > 0):
                a += s[right] == 'a'
                b += s[right] == 'b'
                c += s[right] == 'c'
                right += 1
            if a > 0 and b > 0 and c > 0:
                ans += n - right + 1
            # 缩小窗口
            a -= s[left] == 'a'
            b -= s[left] == 'b'
            c -= s[left] == 'c'
            left += 1
        return ans


s = Solution()
print(s.numberOfSubstrings("acbbcac"))
print(s.numberOfSubstrings("aaacb"))
print(s.numberOfSubstrings("abcabc"))
