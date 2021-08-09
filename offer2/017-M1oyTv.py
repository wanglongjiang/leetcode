'''
剑指 Offer II 017. 含有所有字符的最短字符串
给定两个字符串 s 和 t 。返回 s 中包含 t 的所有字符的最短子字符串。如果 s 中不存在符合条件的子字符串，则返回空字符串 "" 。

如果 s 中存在多个符合条件的子字符串，返回任意一个。

 

注意： 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。

 

示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最短子字符串 "BANC" 包含了字符串 t 的所有字符 'A'、'B'、'C'
示例 2：

输入：s = "a", t = "a"
输出："a"
示例 3：

输入：s = "a", t = "aa"
输出：""
解释：t 中两个字符 'a' 均应包含在 s 的子串中，因此没有符合条件的子字符串，返回空字符串。
 

提示：

1 <= s.length, t.length <= 10^5
s 和 t 由英文字母组成
 

进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？

 

注意：本题与主站 76 题相似（本题答案不唯一）：https://leetcode-cn.com/problems/minimum-window-substring/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/M1oyTv
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：滑动窗口
1、先遍历t，得到所有字符的字典dt，key为字符，val为字符出行的次数
2、遍历s，设置left，right2个指针：
    2.1首先向右移动right指针，直至left，right之间的字典wdt涵盖dt，或right-left<子串最小长度（初始为s的长度-1）时退出
    2.2然后向右移动left，如果保持涵盖dt，缩小最小长度，直至不满足涵盖dt，将此时的最小长度、子串左右坐标记录下来
    回到上面过程2.1继续执行
时间复杂度：O(m+n)，s的长度为m，t的长度为n
空间复杂度：O(n)，需要字典维护t中字符的个数
'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        dt = {}
        for c in t:
            if c in dt:
                dt[c] += 1
            else:
                dt[c] = 1
        wdt = dict.fromkeys(dt.keys(), 0)

        # 检查滑动窗口内的字符是否涵盖t内的字符
        def contains():
            if len(dt) > len(wdt):
                return False
            for item in dt.items():
                if item[1] > wdt[item[0]]:
                    return False
            return True

        left, right = 0, 0
        substr = ''
        minLen = float('inf')
        while right < n:
            while not contains() and right < n:  # 移动右指针，直至覆盖dt
                while right < n and s[right] not in dt:  # 进入窗口的字符不在dt内，跳过
                    right += 1
                if right < n:
                    wdt[s[right]] += 1
                right += 1
            if not contains():
                return substr
            while contains():  # 移动左指针，直至不再覆盖dt
                while s[left] not in dt:  # 移出窗口的字符不在dt内，跳过
                    left += 1
                wdt[s[left]] -= 1
                left += 1
            if minLen > (right - left):  # 子串长度小于以往的子串长度，更新最短字符串
                minLen = right - left
                substr = s[left - 1:right]
        return substr
