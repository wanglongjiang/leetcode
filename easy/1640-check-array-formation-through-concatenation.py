'''
1640. 能否连接形成数组
给你一个整数数组 arr ，数组中的每个整数 互不相同 。另有一个由整数数组构成的数组 pieces，其中的整数也 互不相同 。请你以 任意顺序 连接 pieces 中的数组以形成 arr 。
但是，不允许 对每个数组 pieces[i] 中的整数重新排序。

如果可以连接 pieces 中的数组形成 arr ，返回 true ；否则，返回 false 。

 

示例 1：

输入：arr = [15,88], pieces = [[88],[15]]
输出：true
解释：依次连接 [15] 和 [88]
示例 2：

输入：arr = [49,18,16], pieces = [[16,18,49]]
输出：false
解释：即便数字相符，也不能重新排列 pieces[0]
示例 3：

输入：arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
输出：true
解释：依次连接 [91]、[4,64] 和 [78]
 

提示：

1 <= pieces.length <= arr.length <= 100
sum(pieces[i].length) == arr.length
1 <= pieces[i].length <= arr.length
1 <= arr[i], pieces[i][j] <= 100
arr 中的整数 互不相同
pieces 中的整数 互不相同（也就是说，如果将 pieces 扁平化成一维数组，数组中的所有整数互不相同）
'''
from typing import List
'''
思路：哈希表
1、将arr中的元素及下标加入哈希表；
2、遍历pieces，如果是单个元素，判断其在哈希表中是否存在，如果是多个元素，除判断是否在哈希表中存在之外，还需要下标是连续递增的；

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        hashmap = {arr[i]: i for i in range(len(arr))}
        for p in pieces:
            if len(p) == 1:
                if p[0] not in hashmap:
                    return False
            else:
                preIndex = -1
                for num in p:
                    if num not in hashmap:
                        return False
                    if preIndex >= 0 and hashmap[num] - preIndex != 1:
                        return False
                    preIndex = hashmap[num]
        return True


s = Solution()
assert s.canFormArray([1, 2, 3], [[2], [1, 3]]) == False
assert s.canFormArray(arr=[15, 88], pieces=[[88], [15]])
assert s.canFormArray(arr=[49, 18, 16], pieces=[[16, 18, 49]]) == False
assert s.canFormArray(arr=[91, 4, 64, 78], pieces=[[78], [4, 64], [91]])
