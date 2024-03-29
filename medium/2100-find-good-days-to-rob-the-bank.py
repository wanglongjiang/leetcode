'''
2100. 适合打劫银行的日子
你和一群强盗准备打劫银行。给你一个下标从 0 开始的整数数组 security ，其中 security[i] 是第 i 天执勤警卫的数量。日子从 0 开始编号。同时给你一个整数 time 。

如果第 i 天满足以下所有条件，我们称它为一个适合打劫银行的日子：

第 i 天前和后都分别至少有 time 天。
第 i 天前连续 time 天警卫数目都是非递增的。
第 i 天后连续 time 天警卫数目都是非递减的。
更正式的，第 i 天是一个合适打劫银行的日子当且仅当：security[i - time] >= security[i - time + 1] >= ... >= security[i] <= ... <= security[i + time - 1] <= security[i + time].

请你返回一个数组，包含 所有 适合打劫银行的日子（下标从 0 开始）。返回的日子可以 任意 顺序排列。

 

示例 1：

输入：security = [5,3,3,3,5,6,2], time = 2
输出：[2,3]
解释：
第 2 天，我们有 security[0] >= security[1] >= security[2] <= security[3] <= security[4] 。
第 3 天，我们有 security[1] >= security[2] >= security[3] <= security[4] <= security[5] 。
没有其他日子符合这个条件，所以日子 2 和 3 是适合打劫银行的日子。
示例 2：

输入：security = [1,1,1,1,1], time = 0
输出：[0,1,2,3,4]
解释：
因为 time 等于 0 ，所以每一天都是适合打劫银行的日子，所以返回每一天。
示例 3：

输入：security = [1,2,3,4,5,6], time = 2
输出：[]
解释：
没有任何一天的前 2 天警卫数目是非递增的。
所以没有适合打劫银行的日子，返回空数组。
示例 4：

输入：security = [1], time = 5
输出：[]
解释：
没有日子前面和后面有 5 天时间。
所以没有适合打劫银行的日子，返回空数组。

1 <= security.length <= 105
0 <= security[i], time <= 105
'''

from typing import List
'''
思路：双指针+哈希
设一个哈希表hash
1、遍历security数组，用双指针检查所有长度为time+1的非递增子数组，将数组的末尾坐标right记录到hash中
2、遍历security数组，用双指针检查所有长度为time+1的非递增子数组，如果数组的开头坐标left在hash中存在，则该坐标适合打劫

双指针检查非递增（非递减）子数组的方法：
设2个指针left、right，初始值均为0，
如果security[right+1]<=security[right],向右移动right指针
    当right-left==time时，将此时的right记录到hash中，然后left+=1
否则left、right指针从right+1开始
时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        if time == 0:  # 特殊情况，每天都适合打劫
            return [i for i in range(n)]
        ans = []
        hash = set()
        left, right = 0, 0
        while right < n - 1:  # 第1次遍历找到所有长度为time+1的非递增子数组
            if security[right + 1] <= security[right]:
                right += 1
                if right - left == time:
                    hash.add(right)
                    left += 1
            else:
                left, right = right + 1, right + 1
        left, right = 0, 0
        while right < n - 1:  # 第2次遍历找到所有长度为time+1的非递减子数组
            if security[right + 1] >= security[right]:
                right += 1
                if right - left == time:
                    if left in hash:
                        ans.append(left)
                    left += 1
            else:
                left, right = right + 1, right + 1
        return ans
