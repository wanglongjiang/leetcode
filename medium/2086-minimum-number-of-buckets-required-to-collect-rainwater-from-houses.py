'''
2086. 从房屋收集雨水需要的最少水桶数
给你一个下标从 0 开始的字符串 street 。street 中每个字符要么是表示房屋的 'H' ，要么是表示空位的 '.' 。

你可以在 空位 放置水桶，从相邻的房屋收集雨水。位置在 i - 1 或者 i + 1 的水桶可以收集位置为 i 处房屋的雨水。
一个水桶如果相邻两个位置都有房屋，那么它可以收集 两个 房屋的雨水。

在确保 每个 房屋旁边都 至少 有一个水桶的前提下，请你返回需要的 最少 水桶数。如果无解请返回 -1 。

 

示例 1：

输入：street = "H..H"
输出：2
解释：
我们可以在下标为 1 和 2 处放水桶。
"H..H" -> "HBBH"（'B' 表示放置水桶）。
下标为 0 处的房屋右边有水桶，下标为 3 处的房屋左边有水桶。
所以每个房屋旁边都至少有一个水桶收集雨水。
示例 2：

输入：street = ".H.H."
输出：1
解释：
我们可以在下标为 2 处放置一个水桶。
".H.H." -> ".HBH."（'B' 表示放置水桶）。
下标为 1 处的房屋右边有水桶，下标为 3 处的房屋左边有水桶。
所以每个房屋旁边都至少有一个水桶收集雨水。
示例 3：

输入：street = ".HHH."
输出：-1
解释：
没有空位可以放置水桶收集下标为 2 处的雨水。
所以没有办法收集所有房屋的雨水。
示例 4：

输入：street = "H"
输出：-1
解释：
没有空位放置水桶。
所以没有办法收集所有房屋的雨水。
示例 5：

输入：street = "."
输出：0
解释：
没有房屋需要收集雨水。
所以需要 0 个水桶。
 

提示：

1 <= street.length <= 105
street[i] 要么是 'H' ，要么是 '.' 。
'''
'''
思路：贪心
如果开头或结尾有连续的2个房间，不能收集所有雨水；
如果有连续的3个房价，不能收集；
其余情况可以收集，怎样达到最少水桶的目的呢，可以尽量延迟水桶的放置地点。


时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def minimumBuckets(self, street: str) -> int:
        n = len(street)
        if n == 1:
            return 0 if street == '.' else -1
        if (street[0] == 'H' and street[1] == 'H') or (street[-1] == 'H' and street[-2] == 'H'):
            return -1
        if street.find('HHH') > 0:
            return -1
        ans = 0
        preHouseNeedBucket = False  # 上一个房间是否需要桶
        preIsBucket = False  # 上个位置是否有桶
        for i in range(n):
            if street[i] == '.':
                if preHouseNeedBucket:  # 上一个房间需要桶，在本空位需要放置1个
                    ans += 1
                    preHouseNeedBucket = False
                    preIsBucket = True
                else:
                    preIsBucket = False
            else:
                if preIsBucket:  # 上一个位置是桶，本房间可以不放置水桶
                    preIsBucket = False
                else:  # 上一个位置不是桶，本房间需要一个桶，延迟到下一个空位进行满足
                    if preHouseNeedBucket:  # 上个房间就没有满足，需要先满足上个房间
                        ans += 1
                    preHouseNeedBucket = True
        if preHouseNeedBucket:  # 最后一个房间未放置水桶，需要放上1个
            ans += 1
        return ans


s = Solution()
assert s.minimumBuckets(".HH.H.H.H..") == 3
print(s.minimumBuckets("H..H"))
print(s.minimumBuckets(".H.H."))
print(s.minimumBuckets(".HHH."))
print(s.minimumBuckets("H"))
print(s.minimumBuckets("."))
