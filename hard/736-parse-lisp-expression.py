'''
Lisp 语法解析
给定一个类似 Lisp 语句的表达式 expression，求出其计算结果。

表达式语法如下所示:

表达式可以为整数，let 语法，add 语法，mult 语法，或赋值的变量。表达式的结果总是一个整数。
(整数可以是正整数、负整数、0)
let 语法表示为 (let v1 e1 v2 e2 ... vn en expr), 其中 let语法总是以字符串 "let"来表示，接下来会跟随一个或多个交替变量或表达式，也就是说，
第一个变量 v1被分配为表达式 e1 的值，第二个变量 v2 被分配为表达式 e2 的值，以此类推；最终 let 语法的值为 expr表达式的值。
add 语法表示为 (add e1 e2)，其中 add 语法总是以字符串 "add"来表示，该语法总是有两个表达式e1、e2, 该语法的最终结果是 e1 表达式的值与 e2 表达式的值之和。
mult 语法表示为 (mult e1 e2) ，其中 mult 语法总是以字符串"mult"表示， 该语法总是有两个表达式 e1、e2，该语法的最终结果是 e1 表达式的值与 e2 表达式的值之积。
在该题目中，变量的命名以小写字符开始，之后跟随0个或多个小写字符或数字。为了方便，"add"，"let"，"mult"会被定义为"关键字"，不会在表达式的变量命名中出现。
最后，要说一下作用域的概念。计算变量名所对应的表达式时，在计算上下文中，首先检查最内层作用域（按括号计），然后按顺序依次检查外部作用域。
我们将保证每一个测试的表达式都是合法的。有关作用域的更多详细信息，请参阅示例。
 

示例：

输入: (add 1 2)
输出: 3

输入: (mult 3 (add 2 3))
输出: 15

输入: (let x 2 (mult x 5))
输出: 10

输入: (let x 2 (mult x (let x 3 y 4 (add x y))))
输出: 14
解释:
表达式 (add x y), 在获取 x 值时, 我们应当由最内层依次向外计算, 首先遇到了 x=3, 所以此处的 x 值是 3.


输入: (let x 3 x 2 x)
输出: 2
解释: let 语句中的赋值运算按顺序处理即可

输入: (let x 1 y 2 x (add x y) (add x y))
输出: 5
解释:
第一个 (add x y) 计算结果是 3，并且将此值赋给了 x 。
第二个 (add x y) 计算结果就是 3+2 = 5 。

输入: (let x 2 (add (let x 3 (let x 4 x)) x))
输出: 6
解释:
(let x 4 x) 中的 x 的作用域仅在()之内。所以最终做加法操作时，x 的值是 2 。

输入: (let a1 3 b2 (add a1 1) b2)
输出: 4
解释:
变量命名时可以在第一个小写字母后跟随数字.
 

注意:

我们给定的 expression 表达式都是格式化后的：表达式前后没有多余的空格，表达式的不同部分(关键字、变量、表达式)之间仅使用一个空格分割，
并且在相邻括号之间也没有空格。我们给定的表达式均为合法的且最终结果为整数。
我们给定的表达式长度最多为 2000 (表达式也不会为空，因为那不是一个合法的表达式)。
最终的结果和中间的计算结果都将是一个 32 位整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/parse-lisp-expression
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路1，递归向下分析 栈
设栈varChains为当前作用域的变量表，每个let表达式会生成一个作用域。
遍历expression中的单词，
1. 如果是空格，跳过
2. 如果是let，进入let处理
> let首先期待变量声明： 变量名，表达式 成对出现，表达式有可能是let、add、mult或者整数，如果是let、add、mult需要递归处理
> 最后let需要一个表达式，表达式有可能是let、add、mult或者整数，如果是let、add、mult需要递归处理

3. 如果是add，进入add处理
> 期待2个表达式，表达式有可能是let、add、mult或者整数，如果是let、add、mult需要递归处理

4. 如果是mult，进入mult处理
> 期待2个表达式，表达式有可能是let、add、mult或者整数，如果是let、add、mult需要递归处理

5. 如果是整数，返回整数结果

时间复杂度：O(n^2)，字符串只需要遍历一次，但搜索最近的作用域的变量，需要向上搜索，每次搜索最坏可能需要O(h)，h为let函数的嵌套深度
空间复杂度：O(n)
'''


class Solution:
    def evaluate(self, expression: str) -> int:
        import re
        # 将表达式拆分成数字、函数名、变量名、右括号的序列
        terms = []
        for term in filter(lambda term: len(term) > 0, re.split(r'\(|\s', expression)):
            if term[-1] != ')':
                terms.append(term)
            else:
                terms.append(term[:term.find(')')])
                for i in range(term.count(')')):
                    terms.append(')')
        varChains = []
        self.i = 0

        # 读取下一个单词
        def nextTerm():
            self.term = terms[self.i]
            self.i += 1
            return terms[self.i - 1]

        def hasNext():
            return self.i < len(terms)

        def nextIsBracket():
            return terms[self.i] == ')'

        # 回退一个单词
        def backTerm():
            self.i -= 1
            self.term = terms[self.i]

        # 计算表达式
        def expr():
            term = nextTerm()
            if term == 'let':
                return let()
            elif term == 'add':
                return add()
            elif term == 'mult':
                return mult()
            elif isVar(term):
                return getVarVal(term)
            else:
                return int(term)

        # 计算let表达式
        def let():
            term = nextTerm()
            varChains.append({})  # 声明一个新的变量作用域
            while isVar(term) and hasNext() and not nextIsBracket():  # 当变量名后面有下一个表达式，且表达式不是右括号，认为是变量声明
                varChains[-1][term] = expr()
                term = nextTerm()
            backTerm()  # 将最后的表达式回退，以便expr计算表达式的值
            val = expr()
            varChains.pop()  # 抛弃新添加的变量作用域
            nextTerm()  # 跳过右括号
            return val

        # 计算add表达式
        def add():
            val = expr() + expr()
            nextTerm()  # 跳过右括号
            return val

        # 计算mult表达式
        def mult():
            val = expr() * expr()
            nextTerm()  # 跳过右括号
            return val

        # 判断是否为变量名
        def isVar(term):
            return term[0].islower() and term != 'add' and term != 'mult' and term != 'let'

        # 取得变量值
        def getVarVal(term):
            for i in range(len(varChains) - 1, -1, -1):  # 从最内层的作用域开始，向上搜索变量值
                if term in varChains[i]:
                    return varChains[i][term]

        # 计算整个表达式的值
        return expr()


s = Solution()
print(s.evaluate('(let x 2 (add (let x 3 (let x 4 x)) x))') == 6)
print(s.evaluate('(mult 3 (add 2 3))') == 15)
print(s.evaluate('(add 1 2)') == 3)
print(s.evaluate('(let x 2 (mult x 5))') == 10)
print(s.evaluate('(let x 2 (mult x (let x 3 y 4 (add x y))))') == 14)
print(s.evaluate('(let x 3 x 2 x)') == 2)
print(s.evaluate('(let x 1 y 2 x (add x y) (add x y))') == 5)
print(s.evaluate('(let a1 3 b2 (add a1 1) b2) ') == 4)
