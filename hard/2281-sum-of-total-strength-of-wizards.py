'''
2281. 巫师的总力量和
作为国王的统治者，你有一支巫师军队听你指挥。

给你一个下标从 0 开始的整数数组 strength ，其中 strength[i] 表示第 i 位巫师的力量值。对于连续的一组巫师（也就是这些巫师的力量值是 strength 的 子数组），总力量 定义为以下两个值的 乘积 ：

巫师中 最弱 的能力值。
组中所有巫师的个人力量值 之和 。
请你返回 所有 巫师组的 总 力量之和。由于答案可能很大，请将答案对 109 + 7 取余 后返回。

子数组 是一个数组里 非空 连续子序列。

 

示例 1：

输入：strength = [1,3,1,2]
输出：44
解释：以下是所有连续巫师组：
- [1,3,1,2] 中 [1] ，总力量值为 min([1]) * sum([1]) = 1 * 1 = 1

- [1,3,1,2] 中 [1,3] ，总力量值为 min([1,3]) * sum([1,3]) = 1 * 4 = 4
- [1,3,1,2] 中 [3] ，总力量值为 min([3]) * sum([3]) = 3 * 3 = 9

- [1,3,1,2] 中 [3,1] ，总力量值为 min([3,1]) * sum([3,1]) = 1 * 4 = 4
- [1,3,1,2] 中 [1,3,1] ，总力量值为 min([1,3,1]) * sum([1,3,1]) = 1 * 5 = 5
- [1,3,1,2] 中 [1] ，总力量值为 min([1]) * sum([1]) = 1 * 1 = 1

- [1,3,1,2] 中 [3,1,2] ，总力量值为 min([3,1,2]) * sum([3,1,2]) = 1 * 6 = 6
- [1,3,1,2] 中 [1,3,1,2] ，总力量值为 min([1,3,1,2]) * sum([1,3,1,2]) = 1 * 7 = 7
- [1,3,1,2] 中 [1,2] ，总力量值为 min([1,2]) * sum([1,2]) = 1 * 3 = 3
- [1,3,1,2] 中 [2] ，总力量值为 min([2]) * sum([2]) = 2 * 2 = 4
所有力量值之和为 1 + 9 + 1 + 4 + 4 + 4 + 3 + 5 + 6 + 7 = 44 。
示例 2：

输入：strength = [5,4,6]
输出：213
解释：以下是所有连续巫师组：
- [5,4,6] 中 [5] ，总力量值为 min([5]) * sum([5]) = 5 * 5 = 25
- [5,4,6] 中 [4] ，总力量值为 min([4]) * sum([4]) = 4 * 4 = 16
- [5,4,6] 中 [6] ，总力量值为 min([6]) * sum([6]) = 6 * 6 = 36
- [5,4,6] 中 [5,4] ，总力量值为 min([5,4]) * sum([5,4]) = 4 * 9 = 36
- [5,4,6] 中 [4,6] ，总力量值为 min([4,6]) * sum([4,6]) = 4 * 10 = 40
- [5,4,6] 中 [5,4,6] ，总力量值为 min([5,4,6]) * sum([5,4,6]) = 4 * 15 = 60
所有力量值之和为 25 + 16 + 36 + 36 + 40 + 60 = 213 。
 

提示：

1 <= strength.length <= 105
1 <= strength[i] <= 109
'''

from itertools import accumulate
from typing import List
'''
思路：数学 前缀和
数组长度为10^5，暴力计算需要O(n^2)肯定超时了。
经过仔细观察，设截止第i个下标，以第i下标为末尾的子数组最大力量和为power[i]。
    当strength[i]>=min(strength[0..i-1])时：
        power[i] = power[i-1]+strength[i]*minNum*i+ strength[i] * strength[i]+ preFix , minNum 即为min(strength[0..i-1])
    power[i-1]+strength[i]*minNum*i 这段含义是，以当前巫师截止的子数组等于上一个巫师截止的子数组+strength[i]*minNum，这里对乘法进行了分解
    strength[i] * strength[i] 这段含义是当前巫师的最小子数组是自身乘以自身
    preFix 是上一个巫师的修正，因为上一个巫师的最小子数组也是自身乘以自身，不是乘以最小值。具体公式见代码

    当strength[i]<min(strength[0..i-1])时：
    此时power[i-1]不再是power[i]的子部分，因为minNum发生变动了，需要更改minNum，公式变成：
        power[i] = power[i-1]/minNum*newMinNum+strength[i]*newMinNum*i+strength[i] * strength[i]+preFix

时间复杂度：O(n)
空间复杂度：O(1)，经过优化可以将power数组优化掉，只用1个变量保存power[i-1]
'''


class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        n = len(strength)
        # left[i] 为左侧严格小于 strength[i] 的最近元素位置（不存在时为 -1）
        # right[i] 为右侧小于等于 strength[i] 的最近元素位置（不存在时为 n）
        left, right, st = [-1] * n, [n] * n, []
        for i, v in enumerate(strength):
            while st and strength[st[-1]] >= v:
                right[st.pop()] = i
            if st: left[i] = st[-1]
            st.append(i)

        ss = list(accumulate(accumulate(strength, initial=0), initial=0))  # 前缀和的前缀和

        ans = 0
        for i, v in enumerate(strength):
            l, r = left[i] + 1, right[i] - 1  # [l, r]  左闭右闭
            tot = (i - l + 1) * (ss[r + 2] - ss[i + 1]) - (r - i + 1) * (ss[i + 1] - ss[l])
            ans += v * tot  # 累加贡献
        return ans % (10**9 + 7)


s = Solution()
print(s.totalStrength([14, 9, 14]))
print(s.totalStrength([14, 9, 14, 3]) == 1478)
print(s.totalStrength([1, 3, 1]))
print(s.totalStrength([1, 3, 1, 2]))
print(s.totalStrength([5, 4, 6]))
