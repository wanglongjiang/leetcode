'''
791. 自定义字符串排序
字符串S和 T 只包含小写字符。在S中，所有字符只会出现一次。

S 已经根据某种规则进行了排序。我们要根据S中的字符顺序对T进行排序。更具体地说，如果S中x在y之前出现，那么返回的字符串中x也应出现在y之前。

返回任意一种符合条件的字符串T。

示例:
输入:
S = "cba"
T = "abcd"
输出: "cbad"
解释:
S中出现了字符 "a", "b", "c", 所以 "a", "b", "c" 的顺序应该是 "c", "b", "a".
由于 "d" 没有在S中出现, 它可以放在T的任意位置. "dcba", "cdba", "cbda" 都是合法的输出。
注意:

S的最大长度为26，其中没有重复的字符。
T的最大长度为200。
S和T只包含小写字符。
'''
'''
思路：哈希
以order中的字符为key，list为val，创建哈希表
然后遍历s，将出现在order中的字符加入哈希表

最后按照order中的顺序将list拼接起来

时间复杂度：O(m+n)
空间复杂度：O(m+n)
'''


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hashtab = {}
        for char in order:
            hashtab[char] = []
        other = []
        for char in s:
            if char in hashtab:
                hashtab[char].append(char)
            else:
                other.append(char)
        ans = ''
        for char in order:
            ans += ''.join(hashtab[char])
        ans += ''.join(other)
        return ans
