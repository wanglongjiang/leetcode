'''
替换后的最长重复字符

给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次.
在执行上述操作后，找到包含重复字母的最长子串的长度。

注意：字符串长度 和 k 不会超过 10^4。

 

示例 1：
输入：s = "ABAB", k = 2
输出：4
解释：用两个'A'替换为两个'B',反之亦然。

示例 2：
输入：s = "AABABBA", k = 1
输出：4
解释：
将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
子串 "BBBB" 有最长重复字母, 答案为 4。
'''
'''
思路：滑动窗口
设left,right指针，2个指针构成滑动窗口，统计窗内的字符数，记录到charCount[26]，总字符数total = right-left
如果总字符数-最多的字符计数<=k，向右移动right指针，扩大窗口范围，直至满足：总字符串-最多的字符计数>k
如果总字符串-最多的字符计数>k，向右移动left指针，直至满足：总字符数-最多的字符计数=k

复杂度：
> 时间复杂度：O(n)，稍微精确一点是O(26n)
> 空间复杂度：O(1)，需要长度为26的数组进行计数
'''


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        left, right, n = 0, 0, len(s)
        charCount = [0] * 26
        base = ord('A')
        ans = 0

        def getMostCount():
            return max(charCount)

        while right < n:
            while right - left - getMostCount() <= k and right < n:  # 向右移动指针直至滑动窗口内超过k个需要替换的字符
                charCount[ord(s[right]) - base] += 1
                right += 1
            if right - left - getMostCount() > k:
                ans = max(ans, right - left - 1)
            else:
                ans = max(ans, right - left)
            while right - left - getMostCount() > k:  # 缩小窗口，直至滑动窗口内不超过k个需要替换的字符
                charCount[ord(s[left]) - base] -= 1
                left += 1
        return ans


s = Solution()
print(s.characterReplacement(s="ABAB", k=2))
print(s.characterReplacement(s="AABABBA", k=1))
