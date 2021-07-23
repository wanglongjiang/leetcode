'''
检查是否区域内所有整数都被覆盖
给你一个二维整数数组 ranges 和两个整数 left 和 right 。每个 ranges[i] = [starti, endi] 表示一个从 starti 到 endi 的 闭区间 。

如果闭区间 [left, right] 内每个整数都被 ranges 中 至少一个 区间覆盖，那么请你返回 true ，否则返回 false 。

已知区间 ranges[i] = [starti, endi] ，如果整数 x 满足 starti <= x <= endi ，那么我们称整数x 被覆盖了。

 

示例 1：

输入：ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
输出：true
解释：2 到 5 的每个整数都被覆盖了：
- 2 被第一个区间覆盖。
- 3 和 4 被第二个区间覆盖。
- 5 被第三个区间覆盖。
示例 2：

输入：ranges = [[1,10],[10,20]], left = 21, right = 21
输出：false
解释：21 没有被任何一个区间覆盖。
 

提示：

1 <= ranges.length <= 50
1 <= starti <= endi <= 50
1 <= left <= right <= 50

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-if-all-the-integers-in-a-range-are-covered
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：数组 哈希
遍历每一个区间，如果与left,right有重叠，将left,right之间重叠部分去掉
即，如果range[i][0]<=left<=range[i][1]，将left修改为range[i][1]+1
如果range[i][0]<=right<=range[i][1]，将right修改为range[i][0]-1
如果出现left>right,则left和right之间的所有整数都被覆盖。

时间复杂度：O(n),n为ranges.length
空间复杂度：O(1)

嗯，上面的算法有漏洞。用哈希筛选吧。
把left..right之间的所有整数加入哈希表，然后遍历所有区间，将处于区间范围内的整数删掉。
时间复杂度：O(n*m),n为ranges.length,m为ranges[i]的平均大小
空间复杂度：O(n)
'''


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for r in ranges:
            if r[0] <= left <= r[1]:
                left = r[1] + 1
            if r[0] <= right <= r[1]:
                right = r[0] - 1
            if left > right:
                return True
        allnum = set(range(left, right + 1))
        for r in ranges:
            for i in range(r[0], r[1] + 1):
                if i in allnum:
                    allnum.remove(i)
        return len(allnum) == 0


s = Solution()
print(s.isCovered([[2, 2], [3, 3], [1, 1]], 1, 3))
