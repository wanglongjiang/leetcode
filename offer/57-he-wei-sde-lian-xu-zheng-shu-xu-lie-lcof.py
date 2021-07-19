'''
剑指 Offer 57 - II. 和为s的连续正数序列
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

 

示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
 

限制：

1 <= target <= 10^5
'''
from typing import List
'''
思路：滑动窗口
设left,right2个指针，2个指针构成窗口，
当窗口内序列和大于target，向右移动left指针，减少窗口内的和
当窗口内序列和小于target，向右移动right指针，增加窗口内的和
当窗口内序列和等于target，输出序列,向右移动left指针，减少窗口内的和

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        ans = []
        left, right = 1, 2
        total = 3
        while right + right - 1 <= target:
            if total == target:
                if right > left:
                    ans.append(list(range(left, right + 1)))
                    total -= left
                    left += 1
                else:
                    break
            elif total < target:
                right += 1
                total += right
            elif total > target:
                total -= left
                left += 1
        return ans


s = Solution()
print(s.findContinuousSequence(9))
print(s.findContinuousSequence(15))
