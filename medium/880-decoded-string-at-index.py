'''
索引处的解码字符串

给定一个编码字符串 S。请你找出 解码字符串 并将其写入磁带。解码时，从编码字符串中 每次读取一个字符 ，并采取以下步骤：

如果所读的字符是字母，则将该字母写在磁带上。
如果所读的字符是数字（例如 d），则整个当前磁带总共会被重复写 d-1 次。
现在，对于给定的编码字符串 S 和索引 K，查找并返回解码字符串中的第 K 个字母。

 

示例 1：

输入：S = "leet2code3", K = 10
输出："o"
解释：
解码后的字符串为 "leetleetcodeleetleetcodeleetleetcode"。
字符串中的第 10 个字母是 "o"。
示例 2：

输入：S = "ha22", K = 5
输出："h"
解释：
解码后的字符串为 "hahahaha"。第 5 个字母是 "h"。
示例 3：

输入：S = "a2345678999999999999999", K = 1
输出："a"
解释：
解码后的字符串为 "a" 重复 8301530446056247680 次。第 1 个字母是 "a"。
 

提示：

2 <= S.length <= 100
S 只包含小写字母与数字 2 到 9 。
S 以字母开头。
1 <= K <= 10^9
题目保证 K 小于或等于解码字符串的长度。
解码后的字符串保证少于 2^63 个字母。
'''
'''
思路：栈
将每段字母+数字构成的部分作为一个分组，该分组长度由3部分构成：
(内部长度+字符长度)*重复次数，每读到1个分组，就判断当前K是否小于等于分组长度
如果K>分组长度，需要将上面的信息入栈，继续读入
否则，将  子串长度 mod K，得到字符在（内部字符串+字符串）中的索引，如果索引>内部字符串的长度，需要出栈进入内部字符串继续查找
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        stack = []
        i = 0
        n = len(S)
        while i < n:
            chars = ''
            while i < n and not S[i].isdigit():  # 读入所有的连续字母
                chars += S[i]
                i += 1
            num = 1
            while i < n and S[i].isdigit():  # 重复次数为所有连续数字相乘
                num *= int(S[i])
                i += 1
            innerLen = 0 if not stack else stack[-1][-1]
            unitLen = len(chars) + innerLen
            totalLen = unitLen * num
            stack.append((innerLen, chars, num, totalLen))  # 将内部长度，当前字符串，重复次数，总长度入栈
            if totalLen >= K:  # 如果当前总长度已大于K，退出读取，进入下面的定位过程
                break
        # 定位字母
        while stack:
            innerLen, chars, num, totalLen = stack.pop()
            unitLen = innerLen + len(chars)
            if K > unitLen:
                K = K % unitLen
            if K == 0:
                return chars[-1]
            if K > innerLen:  # K超过内部字符串长度，在当前字符串中定位
                return chars[K - innerLen - 1]
            # K没有超过内部字符串长度，需要在内部字符串中查找


s = Solution()
print(s.decodeAtIndex("a23", 6))
print(s.decodeAtIndex("vzpp636m8y", 2920) == 'z')
print(s.decodeAtIndex("ixm5xmgo78", 711) == 'x')
print(s.decodeAtIndex(S="leet2code3", K=10) == 'o')
print(s.decodeAtIndex(S="ha22", K=5) == 'h')
print(s.decodeAtIndex(S="a2345678999999999999999", K=1) == 'a')
