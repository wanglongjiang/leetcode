'''
面试题 01.09. 字符串轮转
字符串轮转。给定两个字符串s1和s2，请编写代码检查s2是否为s1旋转而成（比如，waterbottle是erbottlewat旋转后的字符串）。

示例1:

 输入：s1 = "waterbottle", s2 = "erbottlewat"
 输出：True
示例2:

 输入：s1 = "aa", s2 = "aba"
 输出：False
提示：

字符串长度在[0, 100000]范围内。
说明:

你能只调用一次检查子串的方法吗？
'''
'''
思路：字符串
字符串s1.s2如果互为轮转，那么s1=xy,s2=yx
s1+s1=xyxy
在xyxy中查找yx，index>-1

时间复杂度：O(n^2)，有可能超时啊。。。

'''


class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return len(s1) == len(s2) and (s1 + s1).find(s2) != -1
