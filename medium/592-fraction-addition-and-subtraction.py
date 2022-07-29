'''
592. 分数加减运算
给定一个表示分数加减运算的字符串 expression ，你需要返回一个字符串形式的计算结果。 

这个结果应该是不可约分的分数，即最简分数。 如果最终结果是一个整数，例如 2，你需要将它转换成分数形式，其分母为 1。
所以在上述例子中, 2 应该被转换为 2/1。

 

示例 1:

输入: expression = "-1/2+1/2"
输出: "0/1"
 示例 2:

输入: expression = "-1/2+1/2+1/3"
输出: "1/3"
示例 3:

输入: expression = "1/3-1/2"
输出: "-1/6"
 

提示:

输入和输出字符串只包含 '0' 到 '9' 的数字，以及 '/', '+' 和 '-'。 
输入和输出分数格式均为 ±分子/分母。如果输入的第一个分数或者输出的分数是正数，则 '+' 会被省略掉。
输入只包含合法的最简分数，每个分数的分子与分母的范围是  [1,10]。 如果分母是1，意味着这个分数实际上是一个整数。
输入的分数个数范围是 [1,10]。
最终结果的分子与分母保证是 32 位整数范围内的有效整数。
'''
'''
思路：数学
遍历一次输入，依次读入一组：符号，分子，分母，与初始值相加或相减，然后将分子分母分别除以2个数的最大公约数进行化简

时间复杂度:O(n)
空间复杂度:O(1)
'''

from math import gcd


class Solution:
    def fractionAddition(self, expression: str) -> str:
        num, den = 0, 1  # 初始分子分母为0和1
        expression = expression if expression[0] == '-' else '+' + expression  # 为方便计算，前面添加一个-
        i, n = 0, len(expression)
        while i < n:
            op = expression[i]
            i += 1
            j = i
            while expression[j] != '/':
                j += 1
            nextnum = int(expression[i:j])  # 读取下一个分子
            j += 1  # 跳过/
            i = j
            while j < n and expression[j] != '+' and expression[j] != '-':
                j += 1
            nextden = int(expression[i:j])  # 读取下一个分母
            i = j
            num = num * nextden + (nextnum * den if op == '+' else -nextnum * den)  # 计算新的分子
            den = den * nextden  # 计算新的分母
            g = gcd(num, den)  # 计算分子分母的最大公约数
            num //= g  # 简化
            den //= g  # 简化
        return str(num) + '/' + str(den)


s = Solution()
print(s.fractionAddition("-1/2+1/2"))
print(s.fractionAddition("-1/2+1/2+1/3"))
print(s.fractionAddition("1/3-1/2"))
