'''
面试题 17.04. 消失的数字
数组nums包含从0到n的所有整数，但其中缺了一个。请编写代码找出那个缺失的整数。你有办法在O(n)时间内完成吗？

注意：本题相对书上原题稍作改动

示例 1：

输入：[3,0,1]
输出：2
 

示例 2：

输入：[9,6,4,2,3,5,7,0,1]
输出：8
'''
from typing import List
from functools import reduce
'''
思路：位运算
利用a^b^b = a的特性
1. 先计算1..n的异或值
2. 然后计算nums整个数组的异或值
3. 将上面2个异或值进行异或，得到的数字就是缺少的数字

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(lambda a, b: a ^ b, nums) ^ reduce(lambda a, b: a ^ b, range(len(nums) + 1))
