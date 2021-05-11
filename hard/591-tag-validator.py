'''
标签验证器
给定一个表示代码片段的字符串，你需要实现一个验证器来解析这段代码，并返回它是否合法。合法的代码片段需要遵守以下的所有规则：

代码必须被合法的闭合标签包围。否则，代码是无效的。
闭合标签（不一定合法）要严格符合格式：<TAG_NAME>TAG_CONTENT</TAG_NAME>。其中，<TAG_NAME>是起始标签，</TAG_NAME>是结束标签。
起始和结束标签中的 TAG_NAME 应当相同。当且仅当 TAG_NAME 和 TAG_CONTENT 都是合法的，闭合标签才是合法的。
合法的 TAG_NAME 仅含有大写字母，长度在范围 [1,9] 之间。否则，该 TAG_NAME 是不合法的。
合法的 TAG_CONTENT 可以包含其他合法的闭合标签，cdata （请参考规则7）和任意字符（注意参考规则1）除了不匹配的<、
不匹配的起始和结束标签、不匹配的或带有不合法 TAG_NAME 的闭合标签。否则，TAG_CONTENT 是不合法的。
一个起始标签，如果没有具有相同 TAG_NAME 的结束标签与之匹配，是不合法的。反之亦然。不过，你也需要考虑标签嵌套的问题。
一个<，如果你找不到一个后续的>与之匹配，是不合法的。并且当你找到一个<或</时，所有直到下一个>的前的字符，都应当被解析为
 TAG_NAME（不一定合法）。
cdata 有如下格式：<![CDATA[CDATA_CONTENT]]>。CDATA_CONTENT 的范围被定义成 <![CDATA[ 和后续的第一个 ]]>之间的字符。
CDATA_CONTENT 可以包含任意字符。cdata 的功能是阻止验证器解析CDATA_CONTENT，所以即使其中有一些字符可以被解析为标签
（无论合法还是不合法），也应该将它们视为常规字符。
合法代码的例子:

输入: "<DIV>This is the first line <![CDATA[<div>]]></DIV>"

输出: True

解释:

代码被包含在了闭合的标签内： <DIV> 和 </DIV> 。

TAG_NAME 是合法的，TAG_CONTENT 包含了一些字符和 cdata 。

即使 CDATA_CONTENT 含有不匹配的起始标签和不合法的 TAG_NAME，它应该被视为普通的文本，而不是标签。

所以 TAG_CONTENT 是合法的，因此代码是合法的。最终返回True。


输入: "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"

输出: True

解释:

我们首先将代码分割为： start_tag|tag_content|end_tag 。

start_tag -> "<DIV>"

end_tag -> "</DIV>"

tag_content 也可被分割为： text1|cdata|text2 。

text1 -> ">>  ![cdata[]] "

cdata -> "<![CDATA[<div>]>]]>" ，其中 CDATA_CONTENT 为 "<div>]>"

text2 -> "]]>>]"


start_tag 不是 "<DIV>>>" 的原因参照规则 6 。
cdata 不是 "<![CDATA[<div>]>]]>]]>" 的原因参照规则 7 。
不合法代码的例子:

输入: "<A>  <B> </A>   </B>"
输出: False
解释: 不合法。如果 "<A>" 是闭合的，那么 "<B>" 一定是不匹配的，反之亦然。

输入: "<DIV>  div tag is not closed  <DIV>"
输出: False

输入: "<DIV>  unmatched <  </DIV>"
输出: False

输入: "<DIV> closed tags with invalid tag name  <b>123</b> </DIV>"
输出: False

输入: "<DIV> unmatched tags with invalid tag name  </1234567890> and <CDATA[[]]>  </DIV>"
输出: False

输入: "<DIV>  unmatched start tag <B>  and unmatched end tag </C>  </DIV>"
输出: False
注意:

为简明起见，你可以假设输入的代码（包括提到的任意字符）只包含数字, 字母, '<','>','/','!','[',']'和' '。
'''
'''
思路：自顶向下的语法分析
按照编译原理里面自顶向下的语法分析进行分析。
一个合法的标签由：<标签开始>标签内容</结束标签>构成，
可以写成3个函数tagStart(),tagContent(),tagEnd()，分别对这3部分进行匹配
tagStart()的匹配逻辑是：必须由'<'开头，中间是1..9个大写字母，以'>'结尾，合法的标签返回值是字符串
tagEnd()的匹配逻辑是：必须由'</'开头，中间是1.。9个大写字母，这几个字母构成的字符串必须与上面的tagStart的返回值相同，最后以'>'结尾
tagContent()的匹配逻辑是：如果不是'<'，跳过，作为普通文本；如果遇到了'<'，有3种可能：1、标签开始 2、标签结束 3、<![CDATA
    对于1、标签开始，需要递归匹配tagStart()tagConten()tagEnd()。
    对于2、标签结束，直接返回，由上一层的tagEnd()进行匹配
    对于3、CDATA，需要匹配知道第1个']]>'
按照上面的描述，写出3个函数即可。
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def isValid(self, code: str) -> bool:
        n = len(code)
        i = 0

        # 读取标签开始
        def tagStart():
            nonlocal i
            if i >= n:
                return False
            if code[i] != '<':  # 代码开始必须是闭合标签
                return False
            i += 1
            # 闭合标签开始
            tagname = ''
            while i < n and code[i].isupper():  # 匹配所有大写字母
                tagname += code[i]
                i += 1
            if len(tagname) == 0 or len(tagname) > 9:  # 长度需要<=9
                return False
            if i >= n or code[i] != '>':
                return False
            i += 1
            return tagname

        # 读取标签结束
        def tagEnd(startTag):
            nonlocal i
            if i + len(startTag) + 2 >= n:
                return False
            if code[i:i + 2] != '</':  # 代码开始必须是闭合标签
                return False
            i += 2
            # 闭合标签开始
            tagname = ''
            while i < n and code[i].isupper():  # 匹配所有大写字母
                tagname += code[i]
                i += 1
            if len(tagname) == 0 or len(tagname) > 9:  # 长度需要<=9
                return False
            if i >= n or code[i] != '>':
                return False
            i += 1
            return startTag == tagname

        # 读取tagContent
        def tagContent():
            nonlocal i
            if i >= n:
                return False
            while i < n and code[i] != '<':
                i += 1
            if i + 1 >= n:  # '<'后面必须有字符
                return False
            if code[i + 1] == '/':  # tag关闭
                return True
            if i + 9 <= n and code[i:i + 9] == '<![CDATA[':
                while i + 2 < n and code[i:i + 3] != ']]>':
                    i += 1
                if i + 3 >= n:  # <![CDATA[ 必须有配对的']]>'
                    return False
                i += 3
                if not tagContent():  # <![CDATA[ ]]> ，之后可能是任意内容
                    return False
            else:  # '<'开头的，如果不是CDATA,必须是闭合标签，之后可能是任意内容
                startTag = tagStart()
                if not startTag:
                    return False
                if not tagContent():
                    return False
                if not tagEnd(startTag):
                    return False
                if not tagContent():
                    return False
            return True

        # 开始匹配，合法的标签，必须由下面3部分构成
        startTag = tagStart()
        if not startTag:
            return False
        if not tagContent():
            return False
        if not tagEnd(startTag):
            return False
        return i == n  # 必须匹配完成所有字符


s = Solution()
print(s.isValid("<A"))
print(s.isValid("<DIV>This is the first line <![CDATA[<div>]]></DIV>"))
print(s.isValid("<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"))
print(s.isValid("<A>  <B> </A>   </B>"))
print(s.isValid("<DIV>  div tag is not closed  <DIV>"))
print(s.isValid("<DIV>  unmatched <  </DIV>"))
print(s.isValid("<DIV> closed tags with invalid tag name  <b>123</b> </DIV>"))
print(s.isValid("<DIV> unmatched tags with invalid tag name  </1234567890> and <CDATA[[]]>  </DIV>"))
print(s.isValid("<DIV>  unmatched start tag <B>  and unmatched end tag </C>  </DIV>"))
