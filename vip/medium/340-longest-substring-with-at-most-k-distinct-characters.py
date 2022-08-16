'''
340. 至多包含 K 个不同字符的最长子串
给定一个字符串 s ，找出 至多 包含 k 个不同字符的最长子串 T。



示例 1:

输入: s = "eceba", k = 2
输出: 3
解释: 则 T 为 "ece"，所以长度为 3。
示例 2:

输入: s = "aa", k = 1
输出: 2
解释: 则 T 为 "aa"，所以长度为 2。


提示：

1 <= s.length <= 5 * 10^4
0 <= k <= 50
'''
'''
思路：滑动窗口 计数
left,right构成滑动窗口，窗口内的字符数用一个哈希表进行计数。
当加入下一个字符要超过k种时，需要移动left指针，并将移出的字符从哈希表中删除。
当窗口内的字符不超过k种时，需要移动right指针，将移入的字符加入哈希表。

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        counter = {}
        n = len(s)
        left, right = 0, 0
        ans = float('-inf')
        while right < n:
            if len(counter) == k and s[right] in counter or len(counter) < k:
                if s[right] not in counter:
                    counter[s[right]] = 1
                else:
                    counter[s[right]] += 1
                right += 1
                ans = max(ans, right - left)
            else:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
        return ans


s = Solution()
print(s.lengthOfLongestSubstringKDistinct(s="eceba", k=2))
print(s.lengthOfLongestSubstringKDistinct(s="aa", k=1))
