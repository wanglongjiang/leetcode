'''
猜数字大小
猜数字游戏的规则如下：

每轮游戏，我都会从 1 到 n 随机选择一个数字。 请你猜选出的是哪个数字。
如果你猜错了，我会告诉你，你猜测的数字比我选出的数字是大了还是小了。
你可以通过调用一个预先定义好的接口 int guess(int num) 来获取猜测结果，返回值一共有 3 种可能的情况（-1，1 或 0）：

-1：我选出的数字比你猜的数字小 pick < num
1：我选出的数字比你猜的数字大 pick > num
0：我选出的数字和你猜的数字一样。恭喜！你猜对了！pick == num
返回我选出的数字。

1 <= n <= 231 - 1
1 <= pick <= n
'''


def guess(num: int) -> int:
    pass


'''
思路：二分查找
时间复杂度：O(logn)
空间复杂度：O(1)
'''


class Solution:
    def guessNumber(self, n: int) -> int:
        low, hight = 1, n
        while low <= hight:
            mid = (low + hight) // 2
            res = guess(mid)
            if res == 0:
                return mid
            if res == 1:
                low = mid + 1
            else:
                hight = mid - 1
