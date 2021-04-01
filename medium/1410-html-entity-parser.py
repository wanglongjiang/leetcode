'''
HTML 实体解析器
「HTML 实体解析器」 是一种特殊的解析器，它将 HTML 代码作为输入，并用字符本身替换掉所有这些特殊的字符实体。

HTML 里这些特殊字符和它们对应的字符实体包括：

双引号：字符实体为 &quot; ，对应的字符是 " 。
单引号：字符实体为 &apos; ，对应的字符是 ' 。
与符号：字符实体为 &amp; ，对应对的字符是 & 。
大于号：字符实体为 &gt; ，对应的字符是 > 。
小于号：字符实体为 &lt; ，对应的字符是 < 。
斜线号：字符实体为 &frasl; ，对应的字符是 / 。
给你输入字符串 text ，请你实现一个 HTML 实体解析器，返回解析器解析后的结果。
'''
'''
思路：字典树
1、将"&quot;", "&apos;", "&amp;", "&gt;", "&lt;", "&frasl;"构造字典树
2、遍历text，查找字典树中的最长长缀，将其加入结果
'''


class Solution:
    def entityParser(self, text: str) -> str:
        n = len(text)
        trieCount, trieSize, charsetSize = 0, 40, 28
        trie = [[0] * charsetSize for _ in range(trieSize)]
        finishIds = {}
        semiSign, andSign, aAscii = ord(';'), ord('&'), ord('a')
        it = iter(['"', "'", '&', '>', '<', '/'])

        # 构造字典树
        def insert(word):
            nonlocal trieCount
            nodeId = 0
            for i in range(len(word)):
                ascii = ord(word[i])
                c = ascii - aAscii
                if ascii == semiSign:
                    c = 26
                elif ascii == andSign:
                    c = 27
                if trie[nodeId][c]:
                    nodeId = trie[nodeId][c]
                else:
                    trieCount += 1
                    trie[nodeId][c] = trieCount
                    nodeId = trieCount
            finishIds[nodeId] = (next(it), len(word))

        for word in ["&quot;", "&apos;", "&amp;", "&gt;", "&lt;", "&frasl;"]:
            insert(word)

        # 查找函数，返回最长长缀长度
        def match(start):
            nodeid = 0
            i = start
            for i in range(start, n):
                ascii = ord(text[i])
                c = ascii - aAscii
                if ascii == semiSign:
                    c = 26
                elif ascii == andSign:
                    c = 27
                if c >= 0 and c < 28 and trie[nodeid][c]:
                    nodeid = trie[nodeid][c]
                    if nodeid in finishIds:
                        se = finishIds[nodeid]
                        ans.append(se[0])
                        return se[1]
                else:
                    break
            if not nodeid:  # 未匹配字典中任何字符，前进1个
                ans.append(text[i])
                return 1
            return i - start - 1

        ans = []
        i = 0
        while i < n:
            i += match(i)
        return ''.join(ans)


s = Solution()
print(s.entityParser("&amp; is an HTML entity but &ambassador; is not."))
print(s.entityParser("and I quote: &quot;...&quot;"))
print(s.entityParser("Stay home! Practice on Leetcode :)"))
print(s.entityParser("x &gt; y &amp;&amp; x &lt; y is always false"))
print(s.entityParser("leetcode.com&frasl;problemset&frasl;all"))
