'''
剑指 Offer II 085. 生成匹配的括号
正整数 n 代表生成括号的对数，请设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]
 

提示：

1 <= n <= 8
 

注意：本题与主站 22 题相同： https://leetcode-cn.com/problems/generate-parentheses/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/IDBivT
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
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
