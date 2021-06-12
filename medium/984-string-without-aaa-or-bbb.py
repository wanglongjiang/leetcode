'''
不含 AAA 或 BBB 的字符串
给定两个整数 A 和 B，返回任意字符串 S，要求满足：

S 的长度为 A + B，且正好包含 A 个 'a' 字母与 B 个 'b' 字母；
子串 'aaa' 没有出现在 S 中；
子串 'bbb' 没有出现在 S 中。
 

示例 1：

输入：A = 1, B = 2
输出："abb"
解释："abb", "bab" 和 "bba" 都是正确答案。
示例 2：

输入：A = 4, B = 1
输出："aabaa"
 

提示：

0 <= A <= 100
0 <= B <= 100
对于给定的 A 和 B，保证存在满足要求的 S。
'''
'''
思路：贪心算法
如果a>b or b>a 则连续输出2个a或2个b然后接另外一个字符，直至a==b
然后交替输出a,b

时间复杂度：O(a+b)
空间复杂度：O(a+b)
'''


class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = []
        while a > 0 or b > 0:
            if a > b and a > 1 and b > 0:
                ans.append('aa')
                a -= 2
                ans.append('b')
                b -= 1
            elif b > a and a > 0 and b > 1:
                ans.append('bb')
                b -= 2
                ans.append('a')
                a -= 1
            else:
                if a > 0:
                    ans.append('a')
                    a -= 1
                if b > 0:
                    ans.append('b')
                    b -= 1
        return ''.join(ans)
