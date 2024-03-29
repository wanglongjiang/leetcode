'''
2019. 解出数学表达式的学生分数
给你一个字符串 s ，它 只 包含数字 0-9 ，加法运算符 '+' 和乘法运算符 '*' ，
这个字符串表示一个 合法 的只含有 个位数数字 的数学表达式（比方说 3+5*2）。
有 n 位小学生将计算这个数学表达式，并遵循如下 运算顺序 ：

按照 从左到右 的顺序计算 乘法 ，然后
按照 从左到右 的顺序计算 加法 。
给你一个长度为 n 的整数数组 answers ，表示每位学生提交的答案。你的任务是给 answer 数组按照如下 规则 打分：

如果一位学生的答案 等于 表达式的正确结果，这位学生将得到 5 分。
否则，如果答案由 一处或多处错误的运算顺序 计算得到，那么这位学生能得到 2 分。
否则，这位学生将得到 0 分。
请你返回所有学生的分数和。

 

示例 1：



输入：s = "7+3*1*2", answers = [20,13,42]
输出：7
解释：如上图所示，正确答案为 13 ，因此有一位学生得分为 5 分：[20,13,42] 。
一位学生可能通过错误的运算顺序得到结果 20 ：7+3=10，10*1=10，10*2=20 。所以这位学生得分为 2 分：[20,13,42] 。
所有学生得分分别为：[2,5,0] 。所有得分之和为 2+5+0=7 。
示例 2：

输入：s = "3+5*2", answers = [13,0,10,13,13,16,16]
输出：19
解释：表达式的正确结果为 13 ，所以有 3 位学生得到 5 分：[13,0,10,13,13,16,16] 。
学生可能通过错误的运算顺序得到结果 16 ：3+5=8，8*2=16 。所以两位学生得到 2 分：[13,0,10,13,13,16,16] 。
所有学生得分分别为：[5,0,0,5,5,2,2] 。所有得分之和为 5+0+0+5+5+2+2=19 。
示例 3：

输入：s = "6+0*1", answers = [12,9,6,4,8,6]
输出：10
解释：表达式的正确结果为 6 。
如果一位学生通过错误的运算顺序计算该表达式，结果仍为 6 。
根据打分规则，运算顺序错误的学生也将得到 5 分（因为他们仍然得到了正确的结果），而不是 2 分。
所有学生得分分别为：[0,0,5,0,0,5] 。所有得分之和为 10 分。
 

提示：

3 <= s.length <= 31
s 表示一个只包含 0-9 ，'+' 和 '*' 的合法表达式。
表达式中所有整数运算数字都在闭区间 [0, 9] 以内。
1 <= 数学表达式中所有运算符数目（'+' 和 '*'） <= 15
测试数据保证正确表达式结果在范围 [0, 1000] 以内。
n == answers.length
1 <= n <= 104
0 <= answers[i] <= 1000
'''
from typing import List
'''
思路：动态规划 栈
首先用栈计算出表达式正确的值
然后用动态规划计算出所有可能的解：
设二维数组dp[len(s)][len(s)]，dp[i][j]保存集合set，它的意思是子表达式s[i..j]的所有可能解
状态转移方程为dp[i][j]=dp[i][k-1]的每个元素*或+dp[k+1][j]的每个元素，k为i,j之间运算符的索引

时间复杂度：O(len(s)^3*max(answer)+m)
空间复杂度：O(len(s)^2*max(answer))
'''


class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        # 计算实际的值
        opd = []
        i, n = 0, len(s)
        while i < n:
            if s[i] == '*':
                i += 1
                opd.append(opd.pop() * int(s[i]))
            elif s[i] != '+':
                opd.append(int(s[i]))
            i += 1
        real = sum(opd)
        # 动态规划计算所有可能的解
        dp = [[set() for _ in range(n)] for _ in range(n)]
        for i in range(0, n, 2):
            dp[i][i].add(int(s[i]))  # 初始化长度为1的子表达式值
        for width in range(3, n + 1, 2):  # 遍历所有子表达式的宽度
            for left in range(0, n - width + 1, 2):  # 子表达式的左边界
                right = left + width - 1  # 子表达式的右边界
                for mid in range(left + 1, right, 2):  # 切分子表达式的操作符下标
                    if s[mid] == '+':  # 计算dp[left][mid-1]、dp[mid+1][right]2个集合中所有元素的和
                        for a in dp[left][mid - 1]:
                            for b in dp[mid + 1][right]:
                                if a + b <= 1000:  # 剪枝，可以筛掉很多
                                    dp[left][right].add(a + b)
                    else:  # 计算dp[left][mid-1]、dp[mid+1][right]2个集合中所有元素的乘积
                        for a in dp[left][mid - 1]:
                            for b in dp[mid + 1][right]:
                                if a * b <= 1000:  # 剪枝，可以筛掉很多，不加这个筛选会超时
                                    dp[left][right].add(a * b)
        all = dp[0][n - 1]
        # 计算结果
        return sum(5 if a == real else (2 if a in all else 0) for a in answers)


s = Solution()
print(
    s.scoreOfStudents("2+2*8+6*6+8*4+2*2+2*8+4+4*4+6+4", [
        413, 252, 172, 472, 252, 724, 695, 796, 39, 252, 444, 596, 448, 544, 628, 932, 724, 252, 784, 676, 820, 908, 420, 252, 840, 252, 765, 943, 888, 577,
        600, 252, 540, 825, 179, 772, 252, 768, 692, 748, 792, 252, 304, 252, 825, 712, 864, 640, 587, 592, 252, 252, 252, 732, 252, 416, 933, 528, 976, 556,
        940, 252, 444, 684, 223, 252
    ]))
print(
    s.scoreOfStudents("4+4*4+2*6+8*4+8*6+6*2+6*8+4*2+4", [
        413, 252, 172, 472, 252, 724, 695, 796, 39, 252, 444, 596, 448, 544, 628, 932, 724, 252, 784, 676, 820, 908, 420, 252, 840, 252, 765, 943, 888, 577,
        600, 252, 540, 825, 179, 772, 252, 768, 692, 748, 792, 252, 304, 252, 825, 712, 864, 640, 587, 592, 252, 252, 252, 732, 252, 416, 933, 528, 976, 556,
        940, 252, 444, 684, 223, 252
    ]))
print(
    s.scoreOfStudents("6*3+3*3*3+9*6+6*6*9+3*9+9*6+9*3", [
        413, 252, 172, 472, 252, 724, 695, 796, 39, 252, 444, 596, 448, 544, 628, 932, 724, 252, 784, 676, 820, 908, 420, 252, 840, 252, 765, 943, 888, 577,
        600, 252, 540, 825, 179, 772, 252, 768, 692, 748, 792, 252, 304, 252, 825, 712, 864, 640, 587, 592, 252, 252, 252, 732, 252, 416, 933, 528, 976, 556,
        940, 252, 444, 684, 223, 252
    ]))
print(
    s.scoreOfStudents("7+7+7+7*7+7*7+7*7+7*7+7*7+7*7+7",
                      [322, 742, 700, 448, 322, 994, 742, 910, 952, 448, 322, 138, 700, 322, 700, 588, 322, 406, 76, 952, 322]))
print(s.scoreOfStudents(s="7+3*1*2", answers=[20, 13, 42]))
print(s.scoreOfStudents(s="3+5*2", answers=[13, 0, 10, 13, 13, 16, 16]))
print(s.scoreOfStudents(s="6+0*1", answers=[12, 9, 6, 4, 8, 6]))
