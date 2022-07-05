'''
1424. 对角线遍历 II
给你一个列表 nums ，里面每一个元素都是一个整数列表。请你依照下面各图的规则，按顺序返回 nums 中对角线上的整数。

 

示例 1：



输入：nums = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,4,2,7,5,3,8,6,9]
示例 2：



输入：nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
输出：[1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
示例 3：

输入：nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
输出：[1,4,2,5,3,8,6,9,7,10,11]
示例 4：

输入：nums = [[1,2,3,4,5,6]]
输出：[1,2,3,4,5,6]
 

提示：

1 <= nums.length <= 10^5
1 <= nums[i].length <= 10^5
1 <= nums[i][j] <= 10^9
nums 中最多有 10^5 个数字。
'''

from typing import List
'''
思路：排序
图中的对角线方向上的坐标和是相同的也就是同一对角线上的i+j相等，先输出左边的对角线，然后输出右边的，同一对角线上先输出j比较小的
根据题意，可以将矩阵的一个元素转化为三元组(i+j,j,数值)，然后排序，最后输出

时间复杂度：O(nlogn)，n为nums中所有元素的个数
空间复杂度：O(n)
'''


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                arr.append((i + j, j, nums[i][j]))
        return [item[2] for item in sorted(arr)]
