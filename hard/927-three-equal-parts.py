'''
927. 三等分
给定一个由 0 和 1 组成的数组 arr ，将数组分成  3 个非空的部分 ，使得所有这些部分表示相同的二进制值。

如果可以做到，请返回任何 [i, j]，其中 i+1 < j，这样一来：

arr[0], arr[1], ..., arr[i] 为第一部分；
arr[i + 1], arr[i + 2], ..., arr[j - 1] 为第二部分；
arr[j], arr[j + 1], ..., arr[arr.length - 1] 为第三部分。
这三个部分所表示的二进制值相等。
如果无法做到，就返回 [-1, -1]。

注意，在考虑每个部分所表示的二进制时，应当将其看作一个整体。例如，[1,1,0] 表示十进制中的 6，而不会是 3。
此外，前导零也是被允许的，所以 [0,1,1] 和 [1,1] 表示相同的值。

 

示例 1：

输入：arr = [1,0,1,0,1]
输出：[0,3]
示例 2：

输入：arr = [1,1,0,1,1]
输出：[-1,-1]
示例 3:

输入：arr = [1,1,0,0,1]
输出：[0,2]
 

提示：

3 <= arr.length <= 3 * 104
arr[i] 是 0 或 1
'''
from typing import List
'''
思路：数学
1、统计数组中的1的个数，如果不能被3整除，则不能划分。
2、将所有的1分成3等份，先不管前导0和后缀0，3个子数组从起始1到结尾1应该完全一样，否则3个数字肯定不同。
3、通过了上述2个检查后，影响3个数字大小的只剩了后缀0（前导0对数字大小无影响），而后缀0的多少取决于最后1个子数组。
因为数组末尾的0肯定属于最后一个子数组；而位于第1第2个之间的0可以变成第2的前导0，或第1个的后缀0；位于第2个和第3个之间的0也可以分别给2个数组。
所以，只要位于第1第2之间的0的数量，第2第3之间的0的数量不少于数组末尾的0的数量即可。

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        count, n = sum(arr), len(arr)
        if count == 0:
            return [0, 2]  # 全为0，可以随意划分，返回固定的一种
        if count % 3:
            return [-1, -1]  # 不能等分为3份
        count //= 3
        boundary = []  # 记录3个均以1开头和结尾的子数组边界
        subcount = 0
        for i in range(n):
            if arr[i]:
                subcount += 1
                if subcount == 1:
                    boundary.append([i])  # 记录左边界
                if subcount % count == 0:
                    boundary[-1].append(i)  # 记录右边界
                    subcount = 0
        # 检查3个边界内的内容是否一样
        if arr[boundary[0][0]:boundary[0][1]] != arr[boundary[1][0]:boundary[1][1]]:
            return [-1, -1]
        if arr[boundary[0][0]:boundary[0][1]] != arr[boundary[2][0]:boundary[2][1]]:
            return [-1, -1]
        # 检查前2个子数组的后缀0是否不少于最后一个子数组的后缀0
        postfix0 = n - 1 - boundary[2][1]
        if postfix0 > boundary[2][0] - boundary[1][1] - 1 or postfix0 > boundary[1][0] - boundary[0][1] - 1:
            return [-1, -1]
        return [boundary[0][1] + postfix0, boundary[1][1] + postfix0 + 1]


s = Solution()
assert s.threeEqualParts([1, 1, 1, 1, 1, 1, 0, 1, 1, 1]) == [2, 6]
s.threeEqualParts([1, 1, 1, 1, 1, 1, 0, 1, 1, 1])
assert s.threeEqualParts([1, 0, 1, 1, 0]) == [-1, -1]
assert s.threeEqualParts([1, 0, 1, 0, 1]) == [0, 3]
assert s.threeEqualParts([1, 1, 0, 1, 1]) == [-1, -1]
assert s.threeEqualParts([1, 1, 0, 0, 1]) == [0, 2]
