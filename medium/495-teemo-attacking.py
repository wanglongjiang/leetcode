'''
提莫攻击
在《英雄联盟》的世界中，有一个叫 “提莫” 的英雄，他的攻击可以让敌方英雄艾希（编者注：寒冰射手）进入中毒状态。现在，给出提莫对艾希的攻击时间序列和提莫攻击的中毒持续时间，你需要输出艾希的中毒状态总时长。

你可以认为提莫在给定的时间点进行攻击，并立即使艾希处于中毒状态。

 

示例1:

输入: [1,4], 2
输出: 4
原因: 第 1 秒初，提莫开始对艾希进行攻击并使其立即中毒。中毒状态会维持 2 秒钟，直到第 2 秒末结束。
第 4 秒初，提莫再次攻击艾希，使得艾希获得另外 2 秒中毒时间。
所以最终输出 4 秒。
示例2:

输入: [1,2], 2
输出: 3
原因: 第 1 秒初，提莫开始对艾希进行攻击并使其立即中毒。中毒状态会维持 2 秒钟，直到第 2 秒末结束。
但是第 2 秒初，提莫再次攻击了已经处于中毒状态的艾希。
由于中毒状态不可叠加，提莫在第 2 秒初的这次攻击会在第 3 秒末结束。
所以最终输出 3 。
 

提示：

你可以假定时间序列数组的总长度不超过 10000。
你可以假定提莫攻击时间序列中的数字和提莫攻击的中毒持续时间都是非负整数，并且不超过 10,000,000。
'''
from typing import List
'''
思路：数组
设变量endTime为上次攻击后中毒效果结束时间。totalTime为上次攻击后预计总的中毒时间。
截止当前攻击时间curTime会收到的总攻击时间为：
if curTime>=endTime: # 如果当前时间大于等于上次攻击后结束时间，那么本次攻击不会对总中毒时间造成影响
    totalTime = totalTime + duration
else: # 如果当前时间早于上次中毒结束时间，本次会影响总中毒时间，需要减掉重叠的时间
    totalTime = totalTime - (endTime-curTime) + duration
按照上面的分析，遍历所有攻击时间，累计总中毒时间

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        totalTime, endTime = 0, 0
        for curTime in timeSeries:
            if curTime >= endTime:  # 如果当前时间大于等于上次攻击后结束时间，那么本次攻击不会对总中毒时间造成影响
                totalTime = totalTime + duration
            else:  # 如果当前时间早于上次中毒结束时间，本次会影响总中毒时间，需要减掉重叠的时间
                totalTime = totalTime - (endTime - curTime) + duration
            endTime = curTime + duration
        return totalTime


s = Solution()
print(s.findPoisonedDuration([1, 4], 2))
print(s.findPoisonedDuration([1, 2], 2))
