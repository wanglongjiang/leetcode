'''
剑指 Offer II 035. 最小时间差
给定一个 24 小时制（小时:分钟 "HH:MM"）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。

 

示例 1：

输入：timePoints = ["23:59","00:00"]
输出：1
示例 2：

输入：timePoints = ["00:00","23:59","00:00"]
输出：0
 

提示：

2 <= timePoints <= 2 * 104
timePoints[i] 格式为 "HH:MM"
 

注意：本题与主站 539 题相同： https://leetcode-cn.com/problems/minimum-time-difference/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/569nqc
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：桶排序
有2种方法，
第1种是常规排序，对时间按照字符串进行排序，然后两两对比挨着的2个时间差
第2种是桶排序，设一个长度为24*60的数组，每个桶代表该时间是否出现，每读到一个时间，将其对应的桶设置为1
如果已经是1，说明有重复的时间，返回0
遍历每2个时间的间隔。

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        m = [0] * 60 * 24
        minTime, maxTime = float('inf'), float('-inf')
        for t in timePoints:
            i = int(t[:2]) * 60 + int(t[3:])
            if m[i]:
                return 0
            m[i] = 1
            minTime = min(i, minTime)
            maxTime = max(i, maxTime)
        ans = minTime + 24 * 60 - maxTime
        preTime = minTime
        for i in range(minTime + 1, maxTime + 1):
            if m[i]:
                ans = min(ans, i - preTime)
                preTime = i
        return ans
