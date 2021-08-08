'''
剑指 Offer II 019. 最多删除一个字符得到回文
给定一个非空字符串 s，请判断如果 最多 从字符串中删除一个字符能否得到一个回文字符串。

 

示例 1:

输入: s = "aba"
输出: true
示例 2:

输入: s = "abca"
输出: true
解释: 可以删除 "c" 字符 或者 "b" 字符
示例 3:

输入: s = "abc"
输出: false
 

提示:

1 <= s.length <= 105
s 由小写英文字母组成
 

注意：本题与主站 680 题相同： https://leetcode-cn.com/problems/valid-palindrome-ii/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/RQku0D
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：双指针
设left,right指针，初始指向字符串2端。
将left,right同时向中间移动。
> 如果s[left]==s[right]，继续移动
> 如果s[left]!=s[right]，
>> 如果s[left+1]==s[right]，将left向中间移动一步，继续对比
>> 如果s[left]==s[right-1]，将right向中间移动一步，继续对比
>> 如果上述条件不满足，说明无论如何移动，字符都不匹配，返回false
> 上述单独移动left、right的过程只能进行一次，如果发生第次，返回false

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        deleted = False
        while left <= right:
            if s[left] != s[right]:
                if deleted:
                    return False
                if s[left + 1] == s[right]:
                    left += 1
                    deleted = True
                elif s[left] == s[right - 1]:
                    right -= 1
                    deleted = True
                else:
                    return False
            else:
                left += 1
                right -= 1
        return True
