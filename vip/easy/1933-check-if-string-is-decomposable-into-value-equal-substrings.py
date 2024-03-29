'''
1933. 判断字符串是否可分解为值均等的子串
一个字符串的所有字符都是一样的，被称作等值字符串。

举例，"1111" 和 "33" 就是等值字符串。
相比之下，"123"就不是等值字符串。
规则：给出一个数字字符串s，将字符串分解成一些等值字符串，如果有且仅有一个等值子字符串长度为2，其他的等值子字符串的长度都是3.

如果能够按照上面的规则分解字符串s，就返回真，否则返回假。

子串就是原字符串中连续的字符序列。



示例 1：

输入: s = "000111000"
输出: false
解释:  s只能被分解长度为3的等值子字符串。
示例 2：

输入: s = "00011111222"
输出: true
解释: s 能被分解为 ["000","111","11","222"].
示例 3：

输入: s = "01110002223300"
输出: false
解释: 一个不能被分解的原因是在开头有一个0.


提示:

1 <= s.length <= 1000
s 仅包含数字。
'''
'''
思路：遍历字符串，如果等长字符串长度n%3==1，无法切割成3、2的组合，返回false
如果n%3==2，如果之前还有长度为2的字符串，返回false
如果n%3==0，无影响

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def isDecomposable(self, s: str) -> bool:
        hasTwo = False
        preChar, count = None, 3
        for char in s:
            if char != preChar:
                if count % 3 == 2:
                    if hasTwo:
                        return False
                    hasTwo = True
                elif count % 3 == 1:
                    return False
                count = 1
                preChar = char
            else:
                count += 1
        if count % 3 == 2:
            if hasTwo:
                return False
            hasTwo = True
        elif count % 3 == 1:
            return False
        return hasTwo


s = Solution()
print(s.isDecomposable('000111000'))
print(s.isDecomposable('00011111222'))
print(s.isDecomposable('01110002223300'))
