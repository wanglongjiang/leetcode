'''
剑指 Offer II 016. 不含重复字符的最长子字符串
给定一个字符串 s ，请你找出其中不含有重复字符的 最长连续子字符串 的长度。

 

示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子字符串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子字符串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0
 

提示：

0 <= s.length <= 5 * 10^4
s 由英文字母、数字、符号和空格组成
 

注意：本题与主站 3 题相同： https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/wtcaE1
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：哈希 滑动窗口
设2个指针，形成滑动窗口，窗口内子串没有重复字符
当新的字符进入窗口会造成重复字符时，移动左边的指针，否则移动右边的指针

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        maxLen = 0
        strlen = len(s)
        end = -1
        map = set()
        for i in range(strlen):
            if i != 0:
                map.remove(s[i - 1])
            while end + 1 < strlen and s[end + 1] not in map:
                map.add(s[end + 1])
                end += 1
            maxLen = max(maxLen, end - i + 1)
        return maxLen
