'''
1318. 或运算的最小翻转次数
给你三个正整数 a、b 和 c。

你可以对 a 和 b 的二进制表示进行位翻转操作，返回能够使按位或运算   a OR b == c  成立的最小翻转次数。

「位翻转操作」是指将一个数的二进制表示任何单个位上的 1 变成 0 或者 0 变成 1 。



示例 1：



输入：a = 2, b = 6, c = 5
输出：3
解释：翻转后 a = 1 , b = 4 , c = 5 使得 a OR b == c
示例 2：

输入：a = 4, b = 2, c = 7
输出：1
示例 3：

输入：a = 1, b = 2, c = 3
输出：0


提示：

1 <= a <= 10^9
1 <= b <= 10^9
1 <= c <= 10^9
'''
'''
思路：位运算
依次比较a、b、c的各位，
当c的当前位是1时，a和b的当前位只需要有1个为1即可，否则需要翻转一次
当c的当前位是0时，a和b必须都是0

时间复杂度：O(1)
空间复杂度：O(1)
'''


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        for i in range(31):
            if (c >> i) & 1:  # c当前位为1
                if (a >> i) & 1 == 0 and (b >> i) & 1 == 0:
                    ans += 1
            else:  # c当前位为0
                if (a >> i) & 1:
                    ans += 1
                if (b >> i) & 1:
                    ans += 1
        return ans


s = Solution()
print(s.minFlips(a=2, b=6, c=5))
print(s.minFlips(a=4, b=2, c=7))
print(s.minFlips(a=1, b=2, c=3))
