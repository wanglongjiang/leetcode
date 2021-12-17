'''
1518. 换酒问题
小区便利店正在促销，用 numExchange 个空酒瓶可以兑换一瓶新酒。你购入了 numBottles 瓶酒。

如果喝掉了酒瓶中的酒，那么酒瓶就会变成空的。

请你计算 最多 能喝到多少瓶酒。

 

示例 1：



输入：numBottles = 9, numExchange = 3
输出：13
解释：你可以用 3 个空酒瓶兑换 1 瓶酒。
所以最多能喝到 9 + 3 + 1 = 13 瓶酒。
示例 2：



输入：numBottles = 15, numExchange = 4
输出：19
解释：你可以用 4 个空酒瓶兑换 1 瓶酒。
所以最多能喝到 15 + 3 + 1 = 19 瓶酒。
示例 3：

输入：numBottles = 5, numExchange = 5
输出：6
示例 4：

输入：numBottles = 2, numExchange = 3
输出：2
 

提示：

1 <= numBottles <= 100
2 <= numExchange <= 100
'''
'''
思路：模拟
模拟换酒瓶的过程，迭代替换，直至换不到酒为止

时间复杂度：O(logn)
空间复杂度：O(1)
'''


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles  # 初始的酒全部能喝到
        while numBottles >= numExchange:
            d, r = divmod(numBottles, numExchange)
            numBottles = d + r  # 能换到的酒+剩余的酒瓶，也就是所有的酒瓶
            ans += d  # 能换到d瓶酒，可以喝
        return ans


s = Solution()
print(s.numWaterBottles(9, 3))
print(s.numWaterBottles(15, 4))
print(s.numWaterBottles(5, 5))
print(s.numWaterBottles(2, 3))
