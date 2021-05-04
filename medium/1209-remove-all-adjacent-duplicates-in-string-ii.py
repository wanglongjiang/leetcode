'''
删除字符串中的所有相邻重复项 II
给你一个字符串 s，「k 倍重复项删除操作」将会从 s 中选择 k 个相邻且相等的字母，并删除它们，
使被删去的字符串的左侧和右侧连在一起。

你需要对 s 重复进行无限次这样的删除操作，直到无法继续为止。

在执行完所有删除操作后，返回最终得到的字符串。

本题答案保证唯一。

示例 1：

输入：s = "abcd", k = 2
输出："abcd"
解释：没有要删除的内容。
示例 2：

输入：s = "deeedbbcccbdaa", k = 3
输出："aa"
解释：
先删除 "eee" 和 "ccc"，得到 "ddbbbdaa"
再删除 "bbb"，得到 "dddaa"
最后删除 "ddd"，得到 "aa"
示例 3：

输入：s = "pbbcggttciiippooaais", k = 2
输出："ps"


提示：

1 <= s.length <= 10^5
2 <= k <= 10^4
s 中只含有小写英文字母。
'''
'''
思路：栈
遍历s，对于每个字符，与栈顶元素对比，
    如果相同，且栈顶字符数为k-1，则将栈顶元素出栈
    如果相同，且栈顶字符数<k-1，将栈顶元素个数+1
    如果不相同，入栈，字符数为1
所有的字符都遍历完之后，将栈内元素输出到结果中
时间复杂度：O(n)，每个字符最多入栈1次
空间复杂度：O(n)
'''


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if not stack or stack[-1][0] != c:
                stack.append([c, 1])
            elif stack[-1][0] == c:
                if stack[-1][1] == k - 1:
                    stack.pop()
                else:
                    stack[-1][1] += 1
        ans = []
        for c, num in stack:
            ans.append(c * num)
        return ''.join(ans)


s = Solution()
print(s.removeDuplicates(s="abcd", k=2))
print(s.removeDuplicates("deeedbbcccbdaa", k=3))
print(s.removeDuplicates(s="pbbcggttciiippooaais", k=2))
