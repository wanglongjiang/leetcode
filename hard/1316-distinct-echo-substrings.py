'''
不同的循环子字符串
给你一个字符串 text ，请你返回满足下述条件的 不同 非空子字符串的数目：

可以写成某个字符串与其自身相连接的形式（即，可以写为 a + a，其中 a 是某个字符串）。
例如，abcabc 就是 abc 和它自身连接形成的。

 

 

示例 1：

输入：text = "abcabcabc"
输出：3
解释：3 个子字符串分别为 "abcabc"，"bcabca" 和 "cabcab" 。
示例 2：

输入：text = "leetcodeleetcode"
输出：2
解释：2 个子字符串为 "ee" 和 "leetcodeleetcode" 。
 

提示：

1 <= text.length <= 2000
text 只包含小写英文字母。
'''
'''
思路：滚动哈希
遍历从1..n//2的字符串长度，当前字符串长度为sublen
对于text的所有长度为sublen的子字符串，计算其哈希值hashcode，并将子字符串最左侧索引i存入hashmap
在存入前检查hashmap中有没有与hashcode相同的，如果有，其对应的索引j+sublen是否等于i，如果相等，找到一个循环字符串

时间复杂度：O(n^2)
空间复杂度：O(n)
'''


class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        b = 100000007  # 哈希的基数
        m = 2**64  # 模
        ans = 0
        for sublen in range(1, n // 2 + 1):
            firsthash, secondhash = 0, 0
            hashset = set()
            t = 1
            for i in range(sublen):
                t = (t * b) % m
                firsthash = (firsthash * b + ord(text[i])) % m  # 计算前面的子串hash
                secondhash = (secondhash * b + ord(text[i + sublen])) % m  # 计算后面的子串hash
            for i in range(n - 2 * sublen + 1):
                if firsthash == secondhash and firsthash not in hashset:  # 连续2子串相同hash值，累计
                    hashset.add(firsthash)  # 已经匹配过一次循环字符串的，加入哈希表，防止再次匹配
                    ans += 1
                if i < (n - 2 * sublen):
                    firsthash = (firsthash * b - ord(text[i]) * t + ord(text[i + sublen])) % m
                    secondhash = (secondhash * b - ord(text[i + sublen]) * t + ord(text[i + 2 * sublen])) % m
        return ans


s = Solution()
print(s.distinctEchoSubstrings('abcabcabc'))
print(s.distinctEchoSubstrings('leetcodeleetcode'))
