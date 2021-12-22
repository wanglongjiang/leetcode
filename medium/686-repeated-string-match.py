'''
686. 重复叠加字符串匹配
给定两个字符串 a 和 b，寻找重复叠加字符串 a 的最小次数，使得字符串 b 成为叠加后的字符串 a 的子串，如果不存在则返回 -1。

注意：字符串 "abc" 重复叠加 0 次是 ""，重复叠加 1 次是 "abc"，重复叠加 2 次是 "abcabc"。

 

示例 1：

输入：a = "abcd", b = "cdabcdab"
输出：3
解释：a 重复叠加三遍后为 "abcdabcdabcd", 此时 b 是其子串。
示例 2：

输入：a = "a", b = "aa"
输出：2
示例 3：

输入：a = "a", b = "a"
输出：1
示例 4：

输入：a = "abc", b = "wxyz"
输出：-1
 

提示：

1 <= a.length <= 10^4
1 <= b.length <= 10^4
a 和 b 由小写英文字母组成
'''
'''
思路：字符串
如果b<=a的长度，在a内能搜索到b，返回1；否则a最多叠加2次，再搜索，如果能找到，返回2；否则返回-1
如果b>a的长度，且b是a的重复叠加子串，那么b的内容为：a的后缀+a重复x次+a的前缀，返回x+(1 if 前缀存在)+(1 if 后缀存在)

时间复杂度：O(n^2)，最坏情况下是O(n^2)
空间复杂度：O(1)
'''


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if len(a) >= len(b): # 如果b<=a的长度，在a内能搜索到b，返回1；否则a最多叠加2次，再搜索，如果能找到，返回2；否则返回-1
            if a.find(b)>=0:
                return 1
            if (a+a).find(b)>=0:
                return 2
            return -1
        begin = b.find(a)
        if begin >= 0: # 在b中能够找到a
            ans = 1 # 能找到a，最少重复1次
            if begin >= len(a):  # b开始预留的长度超过a，无法匹配
                return -1
            if begin > 0:
                if b[:begin] != a[len(a) - begin:]:  # 不是a的后缀，无法匹配
                    return -1
                ans += 1  # 与a的后缀能匹配，重复次数+1
            i = begin + len(a)
            while i + len(a) < len(b) and b[i:i + len(a)] == a:  # 跳过中间的重复子
                i += len(a)
                ans += 1  # 重复次数+1
            if i + len(a) < len(b):  # 剩余部分超过a的长度，无法匹配
                return -1
            if i < len(b):
                if not a.startswith(b[i:]):  # b剩余部分不是a的前缀，无法匹配
                    return -1
                ans += 1
            return ans
        else: # 在b中找不到a
            if len(b)>=2*len(a): # b的长度是a的2倍及以上，按照定义，不能匹配
                return -1
            for i in range(1,len(b)-1): # 遍历b的所有拆分成2个字符串的方案，判断是否能拆分成a的后缀和前缀
                if a.endswith(b[:i]) and a.startswith(b[i:]):
                    return 2
            return -1

s=Solution()
print(s.repeatedStringMatch(a = "abcd", b = "cdabcdab"))        
print(s.repeatedStringMatch(a = "a", b = "aa"))
print(s.repeatedStringMatch(a = "a", b = "a"))
print(s.repeatedStringMatch(a = "abc", b = "wxyz"))
