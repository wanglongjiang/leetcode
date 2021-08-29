'''
1118. 一月有多少天
指定年份 Y 和月份 M，请你帮忙计算出该月一共有多少天。



示例 1：

输入：Y = 1992, M = 7
输出：31
示例 2：

输入：Y = 2000, M = 2
输出：29
示例 3：

输入：Y = 1900, M = 2
输出：28


提示：

1583 <= Y <= 2100
1 <= M <= 12
'''
'''
思路：日期计算
2月需要计算闰年，其他月份天数固定
时间复杂度：O(1)
'''


class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        if month == 2:
            return 29 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 28
        return 31 if month in {1, 3, 5, 7, 8, 10, 12} else 30


s = Solution()
print(s.numberOfDays(1900, 2))
print(s.numberOfDays(1992, 7))
print(s.numberOfDays(2000, 2))
