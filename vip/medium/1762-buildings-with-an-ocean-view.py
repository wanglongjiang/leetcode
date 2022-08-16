'''
1762. 能看到海景的建筑物
有 n 座建筑物。给你一个大小为 n 的整数数组 heights 表示每一个建筑物的高度。

建筑物的右边是海洋。如果建筑物可以无障碍地看到海洋，则建筑物能看到海景。确切地说，如果一座建筑物右边的所有建筑都比它 矮 时，就认为它能看到海景。

返回能看到海景建筑物的下标列表（下标 从 0 开始 ），并按升序排列。



示例 1：

输入：heights = [4,2,3,1]
输出：[0,2,3]
解释：1 号建筑物看不到海景，因为 2 号建筑物比它高
示例 2：

输入：heights = [4,3,2,1]
输出：[0,1,2,3]
解释：所有的建筑物都能看到海景。
示例 3：

输入：heights = [1,3,2,4]
输出：[3]
解释：只有 3 号建筑物能看到海景。
示例 4：

输入：heights = [2,2,2,2]
输出：[3]
解释：如果建筑物右边有相同高度的建筑物则无法看到海景。


提示：

1 <= heights.length <= 10^5
1 <= heights[i] <= 10^9
'''
from typing import List
'''
思路：栈
从右向左遍历数组，如果当前元素大于栈顶元素，则当前元素下标入栈。
遍历完成后，栈中的下标即为结果

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stk = []
        stk.append(len(heights) - 1)  # 最右边的肯定能看到海，加入栈
        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > heights[stk[-1]]:  # 如果比当前栈顶的楼高，可以看到海
                stk.append(i)
        return stk[::-1]  # 栈中元素需要逆序


s = Solution()
print(s.findBuildings([4, 2, 3, 1]))
print(s.findBuildings([4, 3, 2, 1]))
print(s.findBuildings([1, 3, 2, 4]))
print(s.findBuildings([2, 2, 2, 2]))
