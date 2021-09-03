'''
至多包含两个不同字符的最长子串
给定一个字符串 s ，找出 至多 包含两个不同字符的最长子串 t ，并返回该子串的长度。

示例 1:

输入: "eceba"
输出: 3
解释: t 是 "ece"，长度为3。
示例 2:

输入: "ccaabbb"
输出: 5
解释: t 是 "aabbb"，长度为5。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-with-at-most-two-distinct-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：滑动窗口
设left，right指针，初始均指向0
char1,char2变量分别存放窗口内2个不同的字符
1. 向右移动right指针，如果right指针指向的字符是2个已知字符，字符个数+1，停止移动right指针
2. 向右移动left指针，直至某个字符在窗口内不存在，将该变量charX修改为right指针指向的字符

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left, right = 0, 0
        n = len(s)
        char1, char2 = None, None
        char1Count, char2Count = 0, 0
        ans = 0
        while right < n:
            # right指针指向的字符属于2个字符之一，增加个数，循环直至出行第3个字符为止
            while right < n and (not char1 or char1 == s[right] or not char2 or char2 == s[right]):
                if not char1:
                    char1 = s[right]
                    char1Count = 1
                elif char1 == s[right]:
                    char1Count += 1
                elif not char2:
                    char2 = s[right]
                    char2Count = 1
                else:
                    char2Count += 1
                right += 1
            ans = max(ans, right - left)  # 更新结果
            if right == n:  # 已遍历完成，退出
                break
            # 从左往右移出窗口内的字符，直至窗口内只有1种字符
            while left < right and char1Count > 0 and char2Count > 0:
                if char1 == s[left]:
                    char1Count -= 1
                else:
                    char2Count -= 1
                left += 1
            # 更改2个字符之一
            if char1 == 0:
                char1 = s[right]
                char1Count = 1
            else:
                char2 = s[right]
                char2Count = 1
        return ans


s = Solution()
print(s.lengthOfLongestSubstringTwoDistinct('eceba'))
print(s.lengthOfLongestSubstringTwoDistinct('ccaabbb'))
