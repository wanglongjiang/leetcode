'''
给定数字能组成的最大时间
给定一个由 4 位数字组成的数组，返回可以设置的符合 24 小时制的最大时间。

24 小时格式为 "HH:MM" ，其中 HH 在 00 到 23 之间，MM 在 00 到 59 之间。最小的 24 小时制时间是 00:00 ，而最大的是 23:59 。从 00:00 （午夜）开始算起，过得越久，时间越大。

以长度为 5 的字符串，按 "HH:MM" 格式返回答案。如果不能确定有效时间，则返回空字符串。

 

示例 1：

输入：arr = [1,2,3,4]
输出："23:41"
解释：有效的 24 小时制时间是 "12:34"，"12:43"，"13:24"，"13:42"，"14:23"，"14:32"，"21:34"，"21:43"，"23:14" 和 "23:41" 。
这些时间中，"23:41" 是最大时间。
示例 2：

输入：arr = [5,5,5,5]
输出：""
解释：不存在有效的 24 小时制时间，因为 "55:55" 无效。
示例 3：

输入：arr = [0,0,0,0]
输出："00:00"
示例 4：

输入：arr = [0,0,1,0]
输出："10:00"
 

提示：

arr.length == 4
0 <= arr[i] <= 9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-time-for-given-digits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：回溯 枚举
遍历所有数字的组合，然后在其中找到合法的最大时间。
TODO
时间复杂度：O(1)，最大排列数是4!
空间复杂度：O(1)，所有排列时4!
'''


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        coms = []

        # 回溯生成所有时间的组合
        def backtrack(index):
            for i in range(index + 1, 4):
                arr[index], arr[i] = arr[i], arr[index]
                coms.append(arr.copy())
                backtrack(index + 1)
                arr[index], arr[i] = arr[i], arr[index]

        backtrack(0)
        ans = None
        for com in coms:
            if com[0] * 10 + com[1] < 24 and com[2] * 10 + com[3] < 60:  # 在合法的时间里找到最大的
                time = str(com[0]) + str(com[1]) + ':' + str(com[2]) + str(com[3])
                if not ans or time > ans:
                    ans = time
        return ans if ans else ''


s = Solution()
print(s.largestTimeFromDigits([2, 0, 0, 4]))
print(s.largestTimeFromDigits([1, 2, 3, 4]))
print(s.largestTimeFromDigits([5, 5, 5, 5]))
print(s.largestTimeFromDigits([0, 0, 0, 0]))
print(s.largestTimeFromDigits([0, 0, 1, 0]))
