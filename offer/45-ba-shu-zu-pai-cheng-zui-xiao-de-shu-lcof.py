'''
剑指 Offer 45. 把数组排成最小的数

输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

 

示例 1:

输入: [10,2]
输出: "102"
示例 2:

输入: [3,30,34,5,9]
输出: "3033459"
 

提示:

0 < nums.length <= 100
说明:

输出结果可能非常大，所以你需要返回一个字符串而不是整数
拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0
'''
from typing import List
'''
思路：排序
转换输入为字符串数组，对字符串排序
排序对比不能简单对比字符串,需要连结起来对比
如果a+b>b+a则排序后b要在前面

与 179.[最大数](medium/179-largest-number.py) 类似

时间复杂度:O(n^2),因为输入规模较小使用冒泡排序
空间复杂度:O(n)
'''


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        n = len(nums)
        strs = [str(i) for i in nums]  # 转成字符串
        # 冒泡排序
        for i in range(0, n - 1):
            for j in range(n - 1, i, -1):
                s1, s2 = strs[j] + strs[j - 1], strs[j - 1] + strs[j]
                if s1 < s2:
                    strs[j], strs[j - 1] = strs[j - 1], strs[j]
        ans = ''.join(strs)
        if len(ans) > 1 and ans[0] == '0':
            ans = '0'
        return ans


s = Solution()
print(s.minNumber([10, 2]))
print(s.minNumber([3, 30, 34, 5, 9]))
