'''
花括号展开 II
如果你熟悉 Shell 编程，那么一定了解过花括号展开，它可以用来生成任意字符串。

花括号展开的表达式可以看作一个由 花括号、逗号 和 小写英文字母 组成的字符串，定义下面几条语法规则：

如果只给出单一的元素 x，那么表达式表示的字符串就只有 "x"。R(x) = {x}
例如，表达式 {"a"} 表示字符串 "a"。
而表达式 {"w"} 就表示字符串 "w"。
当两个或多个表达式并列，以逗号分隔时，我们取这些表达式中元素的并集。R({e_1,e_2,...}) = R(e_1) ∪ R(e_2) ∪ ...
例如，表达式 "{a,b,c}" 表示字符串 "a","b","c"。
而表达式 "{{a,b},{b,c}}" 也可以表示字符串 "a","b","c"。
要是两个或多个表达式相接，中间没有隔开时，我们从这些表达式中各取一个元素依次连接形成字符串。R(e_1 + e_2) = {a + b for (a, b) in R(e_1) × R(e_2)}
例如，表达式 "{a,b}{c,d}" 表示字符串 "ac","ad","bc","bd"。
表达式之间允许嵌套，单一元素与表达式的连接也是允许的。
例如，表达式 "a{b,c,d}" 表示字符串 "ab","ac","ad"​​​​​​。
例如，表达式 "a{b,c}{d,e}f{g,h}" 可以表示字符串 "abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"。
给出表示基于给定语法规则的表达式 expression，返回它所表示的所有字符串组成的有序列表。

假如你希望以「集合」的概念了解此题，也可以通过点击 “显示英文描述” 获取详情。

 

示例 1：

输入："{a,b}{c,{d,e}}"
输出：["ac","ad","ae","bc","bd","be"]
示例 2：

输入："{{a,z},a{b,c},{ab,z}}"
输出：["a","ab","ac","z"]
解释：输出中 不应 出现重复的组合结果。
 

提示：

1 <= expression.length <= 50
expression[i] 由 '{'，'}'，',' 或小写英文字母组成
给出的表达式 expression 用以表示一组基于题目描述中语法构造的字符串

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/brace-expansion-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：自顶向下的递归分析
遍历expression所有字符，
> 如果遇到字符，进入连结处理子程序，返回所有字符、集合的组合
> 如果遇到'{'，进入并集处理子程序，将内部所有的并集加入集合返回

时间复杂度：O(2^(n/3))最坏情况下能达到这个复杂度
空间复杂度：O(2^(n/3))
'''


class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        self.i, n = 0, len(expression)

        def term():
            return expression[self.i]

        def skip():
            self.i += 1

        def hasNext():
            return self.i < n

        # 求并集
        def union():
            skip()  # 跳过左括号
            unionSet = set()
            nextTerm = term()
            while hasNext() and nextTerm != '}':
                nextTerm = term()
                if nextTerm == '}':
                    break
                if nextTerm == ',':
                    skip()
                else:
                    unionSet.update(join())  # 递归处理连结
            skip()  # 跳过右括号
            return unionSet

        # 求连结
        def join():
            li = []
            while hasNext():
                nextTerm = term()
                if nextTerm == ',' or nextTerm == '}':
                    break
                if nextTerm == '{':
                    li.append(set())
                    li[-1].update(union())  # 递归处理并集
                else:
                    li.append(set(nextTerm))  # 将字符加入集合中
                    skip()
            # 生成li中的所有元素的组合
            while len(li) > 1:
                set1, set2, newset = li.pop(), li.pop(), set()
                for c1 in set1:
                    for c2 in set2:
                        newset.add(c2 + c1)
                li.append(newset)
            return li[-1]

        unionSet = set()
        while hasNext():
            if term() == ',':
                skip()
            else:
                unionSet.update(join())
        return list(sorted(unionSet))


s = Solution()
print(s.braceExpansionII("{a,b},x{c,{d,e}y}"))
print(s.braceExpansionII("{a,b}{c,{d,e}}"))
print(s.braceExpansionII("{{a,z},a{b,c},{ab,z}}"))
print(s.braceExpansionII('a{b,c,d}'))
print(s.braceExpansionII('a{b,c}{d,e}f{g,h}'))
print(s.braceExpansionII('{a,b}{c,d}'))
print(s.braceExpansionII('{{a,b},{b,c}}'))
print(s.braceExpansionII('{a,b,c}'))
