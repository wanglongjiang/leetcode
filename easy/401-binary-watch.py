'''
二进制手表

二进制手表顶部有 4 个 LED 代表 小时（0-11），底部的 6 个 LED 代表 分钟（0-59）。每个 LED 代表一个 0 或 1，最低位在右侧。

例如，下面的二进制手表读取 "3:25" 。


（图源：WikiMedia - Binary clock samui moon.jpg ，许可协议：Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0) ）

给你一个整数 turnedOn ，表示当前亮着的 LED 的数量，返回二进制手表可以表示的所有可能时间。你可以 按任意顺序 返回答案。

小时不会以零开头：

例如，"01:00" 是无效的时间，正确的写法应该是 "1:00" 。
分钟必须由两位数组成，可能会以零开头：

例如，"10:2" 是无效的时间，正确的写法应该是 "10:02" 。
 

示例 1：

输入：turnedOn = 1
输出：["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
示例 2：

输入：turnedOn = 9
输出：[]
 

解释：

0 <= turnedOn <= 10
'''
from typing import List
'''
思路：回溯
用一个迭代将亮的灯分成2组：小时和分钟
设小时分到a个亮灯，那么需要在[8,4,2,1]里面选择a个数的组合，a个数的和不能大于11
分钟分到b个亮灯，那么需要在[32,16,8,4,2,1]里面选择b个数的组合，b个数的和不能大于59
2部分的组合数相乘即为这次分组的时间组合

时间复杂度：O(n!)
'''


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        hours, mintues = [8, 4, 2, 1], [32, 16, 8, 4, 2, 1]

        def selectHours(index, needNum, selected: List, selectedHours: List):
            if needNum == len(selected):
                hour = sum(selected)
                if hour < 12:
                    selectedHours.append(hour)
                return
            for i in range(index, len(hours)):
                selected.append(hours[i])
                selectHours(i + 1, needNum, selected, selectedHours)
                selected.pop()

        def selectMinus(index, needNum, selected: List, selectedMinus: List):
            if needNum == len(selected):
                minu = sum(selected)
                if minu < 60:
                    selectedMinus.append(minu)
                return
            for i in range(index, len(mintues)):
                selected.append(mintues[i])
                selectMinus(i + 1, needNum, selected, selectedMinus)
                selected.pop()

        ans = []
        for i in range(turnedOn + 1):
            hourList, minusList = [], []
            hourNum, minusNum = i, turnedOn - i
            if hourNum == 0:
                hourList = [0]
            else:
                selectHours(0, hourNum, [], hourList)
            if minusNum == 0:
                minusList = [0]
            else:
                selectMinus(0, minusNum, [], minusList)
            if not hourList or not minusList:
                continue
            for h in hourList:
                for m in minusList:
                    ans.append(str(h) + ':' + str(m).zfill(2))
        return ans


s = Solution()
print(s.readBinaryWatch(0))
print(s.readBinaryWatch(1))
print(s.readBinaryWatch(2))
print(s.readBinaryWatch(3))
print(s.readBinaryWatch(4))
print(s.readBinaryWatch(5))
print(s.readBinaryWatch(6))
print(s.readBinaryWatch(7))
print(s.readBinaryWatch(8))
print(s.readBinaryWatch(9))
print(s.readBinaryWatch(10))
