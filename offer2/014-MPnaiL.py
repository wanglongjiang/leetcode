'''
剑指 Offer II 014. 字符串中的变位词
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的某个变位词。

换句话说，第一个字符串的排列之一是第二个字符串的 子串 。

 

示例 1：

输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").
示例 2：

输入: s1= "ab" s2 = "eidboaoo"
输出: False
 

提示：

1 <= s1.length, s2.length <= 10^4
s1 和 s2 仅包含小写字母
 

注意：本题与主站 567 题相同： https://leetcode-cn.com/problems/permutation-in-string/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/MPnaiL
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：滑动窗口计数
与438题类似，因为输入都是小写字母，可以使用长度为26的数组存储s1的各字母计数
然后使用滑动窗口遍历s2，判断滑动窗内的计数是否与s1的计数相同
时间复杂度：O(26*n)
空间复杂度：O(1)
'''


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        base = ord('a')
        if n2 < n1:
            return False
        pcount = [0] * 26
        for c in s1:
            pcount[ord(c) - base] += 1
        scount = [0] * 26
        for i in range(n1):
            scount[ord(s2[i]) - base] += 1
        if scount == pcount:
            return True
        i = 0
        while i + n1 < n2:
            scount[ord(s2[i]) - base] -= 1
            scount[ord(s2[i + n1]) - base] += 1
            i += 1
            if scount == pcount:
                return True
        return False
