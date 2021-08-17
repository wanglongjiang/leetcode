'''
学生出勤记录 I
给定一个字符串来代表一个学生的出勤记录，这个记录仅包含以下三个字符：

'A' : Absent，缺勤
'L' : Late，迟到
'P' : Present，到场
如果一个学生的出勤记录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。

你需要根据这个学生的出勤记录判断他是否会被奖赏。

示例 1:

输入: "PPALLP"
输出: True
示例 2:

输入: "PPALLL"
输出: False
'''
'''
思路：遍历字符串
设置2个变量，acount,lcount，分别记录a出现的次数和l连续出现的次数
如果acount>1或者lcount>2则返回false

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def checkRecord(self, s: str) -> bool:
        acnt, lcnt = 0, 0
        for c in s:
            if c == 'A':
                acnt += 1
                lcnt = 0
                if acnt > 1:
                    return False
            elif c == 'L':
                lcnt += 1
                if lcnt > 2:
                    return False
            else:
                lcnt = 0
        return True


s = Solution()
print(s.checkRecord("LALL"))
