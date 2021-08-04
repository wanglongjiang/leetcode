'''
比较含退格的字符串
给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。

注意：如果对空文本输入退格字符，文本继续为空。

 

示例 1：

输入：S = "ab#c", T = "ad#c"
输出：true
解释：S 和 T 都会变成 “ac”。
示例 2：

输入：S = "ab##", T = "c#d#"
输出：true
解释：S 和 T 都会变成 “”。
示例 3：

输入：S = "a##c", T = "#a#c"
输出：true
解释：S 和 T 都会变成 “c”。
示例 4：

输入：S = "a#c", T = "b"
输出：false
解释：S 会变成 “c”，但 T 仍然是 “b”。
 

提示：

1 <= S.length <= 200
1 <= T.length <= 200
S 和 T 只含有小写字母以及字符 '#'。
 

进阶：

你可以用 O(N) 的时间复杂度和 O(1) 的空间复杂度解决该问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/backspace-string-compare
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：从右向左遍历
设指针ps,pt，初始分别指向s、t的最右侧字符
> 1. 向左移动ps指针，
>> 遇到'#'，设变量delCount为需要删除的字符数，delCount+1
>> 遇到普通字符，如果delCount>0，跳过该字符，delCount-1
>> 遇到普通字符，如果delCount=0，停止移动ps指针
> 2. 向左移动pt指针，
>> 遇到'#'，设变量delCount为需要删除的字符数，delCount+1
>> 遇到普通字符，如果delCount>0，跳过该字符，delCount-1
>> 遇到普通字符，如果delCount=0，停止移动pt指针
> 3. ps和pt指向的字符如果相同，重复上述1.2.；如果指向的字符不相同，返回False

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ps, pt = len(s) - 1, len(t) - 1
        while ps >= 0 and pt >= 0:
            delCount = 0
            while ps >= 0 and (s[ps] == '#' or delCount > 0):  # 向左移动ps指针，直至遇到可以输出的字符
                if s[ps] == '#':
                    delCount += 1
                else:
                    delCount -= 1
                ps -= 1
            delCount = 0
            while pt >= 0 and (t[pt] == '#' or delCount > 0):  # 向左移动pt指针，直至遇到可以输出的字符
                if t[pt] == '#':
                    delCount += 1
                else:
                    delCount -= 1
                pt -= 1
            if ps == -1 and pt == -1:  # 2个指针都移动到了字符串开头，字符串遍历完，返回true
                return True
            if ps == -1 or pt == -1:  # 只有1个指针遍历完，肯定无法匹配
                return False
            if s[ps] != t[pt]:  # 当前字符不相同，返回false
                return False
            ps -= 1  # 当前字符相同，移动指针
            pt -= 1  # 当前字符相同，移动指针
        return True
