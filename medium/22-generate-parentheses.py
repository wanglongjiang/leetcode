'''
括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例 1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
'''
from typing import List
'''
思路：动态规划，遍历上一级所有的组合，将自身加入上一级每个组合的右括号之前
'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parenTable = []
        unionSet = set()
        for i in range(n):
            comList = []
            parenTable.append(comList)
            if i == 0:
                comList.append('()')
                continue
            preComList = parenTable[i - 1]
            for preCom in preComList:
                for i in range(len(preCom)):
                    if preCom[i] == ')':
                        com = preCom[:i] + '()' + preCom[i:]
                        if com not in unionSet:
                            comList.append(com)
                            unionSet.add(com)
                com = preCom + '()'
                if com not in unionSet:
                    comList.append(com)
                    unionSet.add(com)
        return parenTable[n - 1]


s = Solution()
print(s.generateParenthesis(1))
print(s.generateParenthesis(2))
print(s.generateParenthesis(3))
print(s.generateParenthesis(4))
print(s.generateParenthesis(8))
