'''
从相邻元素对还原数组
存在一个由 n 个不同元素组成的整数数组 nums ，但你已经记不清具体内容。好在你还记得 nums 中的每一对相邻元素。

给你一个二维整数数组 adjacentPairs ，大小为 n - 1 ，其中每个 adjacentPairs[i] = [ui, vi] 表示元素 ui 和 vi 在 nums 中相邻。

题目数据保证所有由元素 nums[i] 和 nums[i+1] 组成的相邻元素对都存在于 adjacentPairs 中，存在形式可能是 [nums[i], nums[i+1]] ，
也可能是 [nums[i+1], nums[i]] 。这些相邻元素对可以 按任意顺序 出现。

返回 原始数组 nums 。如果存在多种解答，返回 其中任意一个 即可。

 

示例 1：

输入：adjacentPairs = [[2,1],[3,4],[3,2]]
输出：[1,2,3,4]
解释：数组的所有相邻元素对都在 adjacentPairs 中。
特别要注意的是，adjacentPairs[i] 只表示两个元素相邻，并不保证其 左-右 顺序。
示例 2：

输入：adjacentPairs = [[4,-2],[1,4],[-3,1]]
输出：[-2,4,1,-3]
解释：数组中可能存在负数。
另一种解答是 [-3,1,4,-2] ，也会被视作正确答案。
示例 3：

输入：adjacentPairs = [[100000,-100000]]
输出：[100000,-100000]
 

提示：

nums.length == n
adjacentPairs.length == n - 1
adjacentPairs[i].length == 2
2 <= n <= 10^5
-10^5 <= nums[i], ui, vi <= 10^5
题目数据保证存在一些以 adjacentPairs 作为元素对的数组 nums

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/restore-the-array-from-adjacent-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
from collections import defaultdict
'''
思路：哈希
1. 遍历一次数组，将num与其对应的邻居放入哈希表中，key为num,val为[邻居们]
2. 从只有1个数对的元素出发，找到其相邻元素，拼接到结果中

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for pair in adjacentPairs:
            g[pair[0]].append(pair[1])
            g[pair[1]].append(pair[0])
        for num, li in g.items():
            if len(li) == 1:  # 找到已有1个邻居的元素，把它作为第1个元素
                ans = []
                ans.append(num)  # 第1个元素加入结果
                while g:
                    li = g[ans[-1]]  # 找到结果中最近加入的元素的邻居
                    del g[ans[-1]]  # 把最近的元素从哈希表中删除
                    for num in li:  # 遍历邻居
                        if num in g:  # 只有邻居在哈希表中才加入结果。最近一个元素是被上一个元素加入结果的，上一个元素已经从哈希表中删除，避免了重复添加。
                            ans.append(num)
                return ans


s = Solution()
print(s.restoreArray([[2, 1], [3, 4], [3, 2]]))
print(s.restoreArray([[4, -2], [1, 4], [-3, 1]]))
print(s.restoreArray([[100000, -100000]]))