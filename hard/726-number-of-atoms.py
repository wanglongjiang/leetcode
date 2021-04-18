'''
原子的数量

给定一个化学式formula（作为字符串），返回每种原子的数量。

原子总是以一个大写字母开始，接着跟随0个或任意个小写字母，表示原子的名字。

如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。例如，H2O 和 H2O2 是可行的，
但 H1O2 这个表达是不可行的。

两个化学式连在一起是新的化学式。例如 H2O2He3Mg4 也是化学式。

一个括号中的化学式和数字（可选择性添加）也是化学式。例如 (H2O2) 和 (H2O2)3 是化学式。

给定一个化学式，输出所有原子的数量。格式为：第一个（按字典序）原子的名子，跟着它的数量（如果数量大于 1），
然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。
注意:

所有原子的第一个字母为大写，剩余字母都是小写。
formula的长度在[1, 1000]之间。
formula只包含字母、数字和圆括号，并且题目中给定的是合法的化学式。
'''
'''
思路：使用递归解析化学式

依次读入词元term（可能为原子名，左括号，右括号，数字）
如果是原子名，设置为当前原子atom，并将原子数+1
如果是整数n，将当前原子数+(n-1)
如果是左括号，进入递归处理，将递归程序返回值subCounter记录下来，并读入下一个词元，如果词元是数值m，将subCounter*m更新到当前计数器
如果是右括号，将当前计数器返回上一级

时间复杂度：O(n)，一次遍历
空间复杂度：O(n)，需要使用计数器累计所有原子数
'''


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        self.i = 0
        n = len(formula)

        # 词法分析，读取下一个词元
        def nextTerm():
            if self.i == n:
                return None
            if formula[self.i].isupper():  # 原子名
                j = self.i + 1
                while j < n and formula[j].islower():
                    j += 1
                start = self.i
                self.i = j
                return formula[start:j]
            if formula[self.i].isdigit():  # 数字
                j = self.i + 1
                while j < n and formula[j].isdigit():
                    j += 1
                start = self.i
                self.i = j
                return int(formula[start:j])
            if formula[self.i] == '(':
                self.i += 1
                return '('
            if formula[self.i] == ')':
                self.i += 1
                return ')'

        import collections

        # 原子表达式解析
        def expr():
            counter = collections.Counter()
            term = nextTerm()
            atom = None
            while term:
                if isinstance(term, int):  # 如果是数值，需要将当前原子数增加
                    counter[atom] += term - 1
                    term = nextTerm()
                elif term == '(':
                    subcounter = expr()  # 如果是左括号，进入子表达式处理
                    term = nextTerm()
                    if isinstance(term, int):  # 如果子表达式后面跟着数值，需要将子表达式计数器乘以数值
                        for a, c in subcounter.most_common():
                            subcounter[a] = c * term
                        term = nextTerm()
                    counter.update(subcounter)  # 将子表达式的计数器更新到当前计数器里面
                elif term == ')':  # 如果是右括号，将当前表达式的计数器返回给上级
                    return counter
                else:  # 如果是原子，计数器中增加1个原子
                    atom = term
                    counter[atom] += 1
                    term = nextTerm()
            return counter

        # 对计数器中的原子按照字典序进行排序后输出
        counter = expr()
        ans = []
        for atom, count in sorted(counter.most_common(), key=lambda item: item[0]):
            ans.append(atom)
            if count > 1:
                ans.append(str(count))
        return ''.join(ans)


s = Solution()
print(s.countOfAtoms("H2O"))
print(s.countOfAtoms("Mg(OH)2"))
print(s.countOfAtoms("K4(ON(SO3)2)2"))
