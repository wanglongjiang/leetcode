'''
2434. 使用机器人打印字典序最小的字符串
给你一个字符串 s 和一个机器人，机器人当前有一个空字符串 t 。执行以下操作之一，直到 s 和 t 都变成空字符串：

删除字符串 s 的 第一个 字符，并将该字符给机器人。机器人把这个字符添加到 t 的尾部。
删除字符串 t 的 最后一个 字符，并将该字符给机器人。机器人将该字符写到纸上。
请你返回纸上能写出的字典序最小的字符串。

 

示例 1：

输入：s = "zza"
输出："azz"
解释：用 p 表示写出来的字符串。
一开始，p="" ，s="zza" ，t="" 。
执行第一个操作三次，得到 p="" ，s="" ，t="zza" 。
执行第二个操作三次，得到 p="azz" ，s="" ，t="" 。
示例 2：

输入：s = "bac"
输出："abc"
解释：用 p 表示写出来的字符串。
执行第一个操作两次，得到 p="" ，s="c" ，t="ba" 。
执行第二个操作两次，得到 p="ab" ，s="c" ，t="" 。
执行第一个操作，得到 p="ab" ，s="" ，t="c" 。
执行第二个操作，得到 p="abc" ，s="" ，t="" 。
示例 3：

输入：s = "bdda"
输出："addb"
解释：用 p 表示写出来的字符串。
一开始，p="" ，s="bdda" ，t="" 。
执行第一个操作四次，得到 p="" ，s="" ，t="bdda" 。
执行第二个操作四次，得到 p="addb" ，s="" ，t="" 。
 

提示：

1 <= s.length <= 105
s 只包含小写英文字母。
'''
'''
思路：贪心 栈
设一个后缀数组postfix，postfix[i]保存postfix[i]之后最小的字符
然后遍历s，针对每个字符s[i]，如果s[i]>postfix[i+1]，说明后面还有更小的字符，需要入栈
否则需要出栈直至栈顶字符<=postfix[i+1]

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        postfix = ['z'] * (n + 1)
        postfix[-1] = s[-1]
        for i in range(n - 1, 0, -1):
            postfix[i] = min(postfix[i + 1], s[i])
        stk, ans = [], []
        for i in range(n):
            stk.append(s[i])
            while stk and stk[-1] <= postfix[i + 1]:
                ans.append(stk.pop())
        while stk:
            ans.append(stk.pop())
        return ''.join(ans)


s = Solution()
assert s.robotWithString("bac") == 'abc'
print(s.robotWithString("zza"))
assert s.robotWithString("bdda") == "addb"
