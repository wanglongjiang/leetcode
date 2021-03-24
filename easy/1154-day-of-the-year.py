'''
一年中的第几天
给你一个按 YYYY-MM-DD 格式表示日期的字符串 date，请你计算并返回该日期是当年的第几天。

通常情况下，我们认为 1 月 1 日是每年的第 1 天，1 月 2 日是每年的第 2 天，依此类推。每个月的天数与现行公元纪年法（格里高利历）一致。
'''


class Solution:
    def dayOfYear(self, date: str) -> int:
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        leapDays = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        year, month, day = int(date[:4]), int(date[5:7]), int(date[8:])
        if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
            return sum(leapDays[:month]) + day
        else:
            return sum(days[:month]) + day


s = Solution()
print(s.dayOfYear("2019-01-09"))
print(s.dayOfYear("2019-02-10"))
print(s.dayOfYear("2003-03-01"))
print(s.dayOfYear("2004-03-01"))
