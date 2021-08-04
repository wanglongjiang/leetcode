'''
旋转字符串
给定两个字符串, A 和 B。

A 的旋转操作就是将 A 最左边的字符移动到最右边。 例如, 若 A = 'abcde'，在移动一次之后结果就是'bcdea' 。
如果在若干次旋转操作之后，A 能变成B，那么返回True。

示例 1:
输入: A = 'abcde', B = 'cdeab'
输出: true

示例 2:
输入: A = 'abcde', B = 'abced'
输出: false
注意：

A 和 B 长度不超过 100。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路1，暴力搜索
将字符串s切分成任意2个子串a,b，然后对比goal的2部分是否由b,a构成
时间复杂度：O(n^2)
空间复杂度：O(1)

思路2，KMP字符串搜索
如果s,goal是旋转字符串，构成他们的分别是a,b
那么s=ab，goal=ba
把字符串s与其自身连结一次，得到s+s=abab。
如果goal在s+s中存在，则为旋转字符串
字符串查找可以用kmp算法

时间复杂度：O(n)，kmp算法搜索字符串需要O(n)时间，但题目中的字符集没有给出，构造kmp的DFA有可能需要高大256的常数，达到O(256n)
空间复杂度：O(n)

思路4，拼接后正则表达式
按照思路2，构造一个s+s字符串，然后用正则表达式查找

时间复杂度：O(n)
空间复杂度：O(n)

思路4，拼接后直接搜索
按照思路2，构造一个s+s字符串，然后直接搜索

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    # 思路3
    def rotateString(self, s: str, goal: str) -> bool:
        s = s + s
        return s.find(goal) != -1

    # 思路4
    def rotateString4(self, s: str, goal: str) -> bool:
        import re
        return re.search(goal, s + s) is not None
