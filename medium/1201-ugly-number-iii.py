'''
丑数 III

给你四个整数：n 、a 、b 、c ，请你设计一个算法来找出第 n 个丑数。

丑数是可以被 a 或 b 或 c 整除的 正整数 。
'''
'''
思路：
lcm = min(a,b,c)*n #求最小公倍数
if lcm> a*b
    skip += lcm//(a*b)
if lcm> a*c
    skip += lcm//(a*c)
if lcm> b*c
    skip += lcm//(b*c)
if lcm> a*b*c
    skip -= lcm//(a*b*c)
x=(n-skip)
从lcm开始，找x个数
dp[i] = min(pa*a,pb*b,pc*c,pi*c)
TODO
'''


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        pa = pb = pc = 0

        for i in range(1, n + 1):
            numa, numb, numc = dp[pa] * a, dp[pb] * b, dp[pc] * c
            dp[i] = min(numa, numb, numc)
            if dp[i] == numa:
                pa += 1
            if dp[i] == numb:
                pb += 1
            if dp[i] == numc:
                pc += 1

        return dp[n]


s = Solution()
print(s.nthUglyNumber(n=5, a=2, b=11, c=13))
print(s.nthUglyNumber(n=3, a=2, b=3, c=5))
print(s.nthUglyNumber(n=4, a=2, b=3, c=4))
print(s.nthUglyNumber(n=1000000000, a=2, b=217983653, c=336916467))
