'''
大餐计数
大餐 是指 恰好包含两道不同餐品 的一餐，其美味程度之和等于 2 的幂。

你可以搭配 任意 两道餐品做一顿大餐。

给你一个整数数组 deliciousness ，其中 deliciousness[i] 是第 i​​​​​​​​​​​​​​ 道餐品的美味程度，返回你可以用数组中的餐品做出的不同 大餐 的数量。
结果需要对 109 + 7 取余。

注意，只要餐品下标不同，就可以认为是不同的餐品，即便它们的美味程度相同。

 

示例 1：

输入：deliciousness = [1,3,5,7,9]
输出：4
解释：大餐的美味程度组合为 (1,3) 、(1,7) 、(3,5) 和 (7,9) 。
它们各自的美味程度之和分别为 4 、8 、8 和 16 ，都是 2 的幂。
示例 2：

输入：deliciousness = [1,1,1,3,3,3,7]
输出：15
解释：大餐的美味程度组合为 3 种 (1,1) ，9 种 (1,3) ，和 3 种 (1,7) 。
 

提示：

1 <= deliciousness.length <= 10^5
0 <= deliciousness[i] <= 2^20

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-good-meals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
from collections import Counter
from math import factorial
'''
思路：数学 哈希
如果想要成为大餐，任意2个的组合deliciousness[i]+deliciousness[j]必须是2的幂，如果采用暴力组合的模式，需要n^2，会超时。
题目中给出了deliciousness[i]的范围是0..2^20，故任意2个数的和都会<=2^21。
可以先统计每个数值的个数并记录到哈希表counter中，
然后遍历每个数值a，用2^1..2^20分别减去a，得到b，如果b在counter中存在，则这2个数字构成的大餐组合数是a的个数*b的个数。
特别的，当a=b时，需要按照组合公式计算：a的个数!/2(a的个数-2)!

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        counter = Counter(deliciousness)
        ans, ans1, m = 0, 0, 10**9 + 7  # ans为数值与其他数值的组合，ans1为数值与其自身的组合
        for a, count in counter.items():
            for i in range(0, 22):
                b = (1 << i) - a
                if b in counter and a != b:
                    ans = (ans + counter[a] * counter[b]) % m
            if a and a & (a - 1) == 0 and counter[a] > 1:  # 数值与其自身能构成2的幂，需要用组合公式计算其自身构成的组合数
                ans1 = (ans1 + factorial(counter[a]) // (2 * factorial(counter[a] - 2))) % m
        return ans // 2 + ans1  # ans除以2的原因是因为a与b，b与a的组合重复计算了


s = Solution()
print(
    s.countPairs([
        2160, 1936, 3, 29, 27, 5, 2503, 1593, 2, 0, 16, 0, 3860, 28908, 6, 2, 15, 49, 6246, 1946, 23, 105, 7996, 196, 0, 2, 55, 457, 5, 3, 924, 7268, 16, 48, 4,
        0, 12, 116, 2628, 1468
    ]))
print(s.countPairs([149, 107, 1, 63, 0, 1, 6867, 1325, 5611, 2581, 39, 89, 46, 18, 12, 20, 22, 234]))
print(s.countPairs(deliciousness=[1, 3, 5, 7, 9]))
print(s.countPairs([1, 1, 1, 3, 3, 3, 7]))
