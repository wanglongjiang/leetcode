'''
LCP 18. 早餐组合
小扣在秋日市集选择了一家早餐摊位，一维整型数组 staple 中记录了每种主食的价格，一维整型数组 drinks 中记录了每种饮料的价格。小扣的计划选择一份主食和一款饮料，且花费不超过 x 元。
请返回小扣共有多少种购买方案。

注意：答案需要以 1e9 + 7 (1000000007) 为底取模，如：计算初始结果为：1000000008，请返回 1
'''
from typing import List
'''
思路：动态规划。
思路1，暴力查找，需要2重循环，时间复杂度O(n*n)，达到10^10，时间太久。空间复杂度O(1)
思路2，对输入进行排序，第2重查找时使用二分查找，时间复杂度O(n*logn)，为10^7，时间也很长。空间复杂度O(1)
思路3，动态规划。
开辟一个大小为x的辅助数组drinkNums，里面记录价格小于等于下标的饮料数量。初始值都为0。
1、遍历drinks，将响应的数量累计到drinkNums。
2、遍历drinkNums，把元素都累加左边的元素值，因为后面的价格能买的起前面的饮料。
3、遍历staple，对于staple[i]，目标饮料价格为target=x-staple[i]，访问drinkNums[target]，这是饮料的数量。把所有饮料数量累计，即为结果。
'''


class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        drinkNums = [0] * (x + 1)
        # 1、遍历drinks，饮料计数
        for cost in drinks:
            drinkNums[cost] += 1
        # 2、对drinkNums进行动态规划
        for i in range(1, x + 1):
            drinkNums[i] += drinkNums[i - 1]
        # 3、计算组合
        comNum = 0
        for cost in staple:
            if x > cost:
                comNum += drinkNums[x - cost]
        return comNum % 1000000007


s = Solution()
print(s.breakfastNumber(staple=[10, 20, 5], drinks=[5, 5, 2], x=15))
print(s.breakfastNumber(staple=[2, 1, 1], drinks=[8, 9, 5, 1], x=9))
