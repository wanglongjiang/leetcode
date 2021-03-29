'''
亲密字符串
给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回 true ；否则返回 false 。

交换字母的定义是取两个下标 i 和 j （下标从 0 开始），只要 i!=j 就交换 A[i] 和 A[j] 处的字符。
例如，在 "abcd" 中交换下标 0 和下标 2 的元素可以生成 "cbad" 。


提示：

0 <= A.length <= 20000
0 <= B.length <= 20000
A 和 B 仅由小写字母构成。
'''
'''
思路：1次遍历
亲密字符串必须长度相同，
最多有两个字母不同，如果只有1个字符不同也不行
如果所有字符相同，必须有重复字符
'''


class Solution:
    def buddyStrings(self, a: str, b: str) -> bool:
        if len(a) != len(b):
            return False
        diff = 0
        diffA, diffB = None, None
        hasDuplicate = False
        charset = set()
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1
                if diff > 2:
                    return False
                if diff == 1:
                    diffA, diffB = a[i], b[i]
                else:
                    if diffA != b[i] or diffB != a[i]:
                        return False
            else:
                if not hasDuplicate:
                    if a[i] in charset:
                        hasDuplicate = True
                    else:
                        charset.add(a[i])
        if diff == 1:
            return False
        if diff == 2:
            return True
        return hasDuplicate


s = Solution()
print(s.buddyStrings(a="ab", b="ba"))
print(s.buddyStrings(a="ab", b="ab"))
print(s.buddyStrings(a="aa", b="aa"))
print(s.buddyStrings(a="aaaaaaabc", b="aaaaaaacb"))
print(s.buddyStrings(a="", b="aa"))
print(s.buddyStrings(a="", b=""))
