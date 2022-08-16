'''
1940. 排序数组之间的最长公共子序列
给定一个由整数数组组成的数组arrays，其中arrays[i]是严格递增排序的，返回一个表示所有数组之间的最长公共子序列的整数数组。

子序列是从另一个序列派生出来的序列，删除一些元素或不删除任何元素，而不改变其余元素的顺序。

示例1:

输入: arrays = [[1,3,4],
               [1,4,7,9]]
输出: [1,4]
解释: 这两个数组中的最长子序列是[1,4]。
示例 2:

输入: arrays = [[2,3,6,8],
               [1,2,3,5,6,7,10],
               [2,3,4,6,9]]
输出: [2,3,6]
解释: 这三个数组中的最长子序列是[2,3,6]。
示例 3:

输入: arrays = [[1,2,3,4,5],
               [6,7,8]]
输出: []
解释: 这两个数组之间没有公共子序列。


限制条件:

2 <= arrays.length <= 100
1 <= arrays[i].length <= 100
1 <= arrays[i][j] <= 100
arrays[i] 是严格递增排序.
'''
from typing import List
'''
思路：计数
因为1 <= arrays[i][j] <= 100，且arrays[i] 严格递增，可以设置一个大小为100的数组counter。
遍历arrays[i]的每个元素，在counter中计数，
最后遍历counter，如果某个元素在所有的arrays[i]中都存在，它的数量是n=len(arrays)

时间复杂度：O(mn)
空间复杂度：O(1)，需要的辅助空间为固定值101
'''


class Solution:
    def longestCommomSubsequence(self, arrays: List[List[int]]) -> List[int]:
        counter = [0] * 101
        for arr in arrays:
            for num in arr:
                counter[num] += 1  # 计数
        n = len(arrays)
        return list(map(lambda p: p[0], filter(lambda p: p[1] == n, enumerate(counter))))  # 过滤出计数为n的数值


s = Solution()
print(s.longestCommomSubsequence([[1, 3, 4], [1, 4, 7, 9]]))
print(s.longestCommomSubsequence([[2, 3, 6, 8], [1, 2, 3, 5, 6, 7, 10], [2, 3, 4, 6, 9]]))
print(s.longestCommomSubsequence([[1, 2, 3, 4, 5], [6, 7, 8]]))
