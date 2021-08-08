'''
剑指 Offer II 032. 有效的变位词
给定两个字符串 s 和 t ，编写一个函数来判断它们是不是一组变位词（字母异位词）。

注意：若 s 和 t 中每个字符出现的次数都相同且字符顺序不完全相同，则称 s 和 t 互为变位词（字母异位词）。

 

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
示例 3:

输入: s = "a", t = "a"
输出: false
 

提示:

1 <= s.length, t.length <= 5 * 10^4
s and t 仅包含小写字母
 

进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

 

注意：本题与主站 242 题相似（字母异位词定义不同）：https://leetcode-cn.com/problems/valid-anagram/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dKk3P7
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：计数
设计一个长度26的数组counter，统计s内各个字母出现的频率，然后再遍历t内所有字符，出现的字符在counter内减掉
中间如果出现-1，不是字母异位词。
时间复杂度：O(s+t)
空间复杂度：O(1)
进阶，如果是unicode字符，可以用map实现

'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = [0] * 26
        for c in s:
            counter[ord(c) - ord('a')] += 1
        for c in t:
            i = ord(c) - ord('a')
            counter[i] -= 1
            if counter[i] < 0:
                return False
        return True
