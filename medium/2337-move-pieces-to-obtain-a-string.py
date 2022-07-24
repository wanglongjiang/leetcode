'''
2337. 移动片段得到字符串
给你两个字符串 start 和 target ，长度均为 n 。每个字符串 仅 由字符 'L'、'R' 和 '_' 组成，其中：

字符 'L' 和 'R' 表示片段，其中片段 'L' 只有在其左侧直接存在一个 空位 时才能向 左 移动，
而片段 'R' 只有在其右侧直接存在一个 空位 时才能向 右 移动。
字符 '_' 表示可以被 任意 'L' 或 'R' 片段占据的空位。
如果在移动字符串 start 中的片段任意次之后可以得到字符串 target ，返回 true ；否则，返回 false 。

 

示例 1：

输入：start = "_L__R__R_", target = "L______RR"
输出：true
解释：可以从字符串 start 获得 target ，需要进行下面的移动：
- 将第一个片段向左移动一步，字符串现在变为 "L___R__R_" 。
- 将最后一个片段向右移动一步，字符串现在变为 "L___R___R" 。
- 将第二个片段向右移动散步，字符串现在变为 "L______RR" 。
可以从字符串 start 得到 target ，所以返回 true 。
示例 2：

输入：start = "R_L_", target = "__LR"
输出：false
解释：字符串 start 中的 'R' 片段可以向右移动一步得到 "_RL_" 。
但是，在这一步之后，不存在可以移动的片段，所以无法从字符串 start 得到 target 。
示例 3：

输入：start = "_R", target = "R_"
输出：false
解释：字符串 start 中的片段只能向右移动，所以无法从字符串 start 得到 target 。
 

提示：

n == start.length == target.length
1 <= n <= 105
start 和 target 由字符 'L'、'R' 和 '_' 组成
'''
'''
思路：脑筋急转弯
首先，无论怎么移动，由于 L 和 R 无法互相穿过对方，那么去掉 _ 后的剩余字符应该是相同的，否则返回 false。
然后用双指针遍历 \textit{start}[i]start[i] 和 \textit{target}[j]target[j]，分类讨论：

如果当前字符为 L 且 i<ji<j，那么这个 L 由于无法向右移动，返回 false；
如果当前字符为 R 且 i>ji>j，那么这个 R 由于无法向左移动，返回 false。
遍历完，若中途没有返回 false 就返回 true。

时间复杂度：O(n)
空间复杂度：O(1)
'''

from typing import Counter


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace('_', '') != target.replace('_', ''): return False
        j = 0
        for i, c in enumerate(start):
            if c == '_': continue
            while target[j] == '_':
                j += 1
            if i != j and (c == 'L') == (i < j): return False
            j += 1
        return True


s = Solution()
print(s.canChange("R_L__R__R_", "_L______RR"))
print(s.canChange("_L__R__RL", "L_____RLR"))
print(s.canChange(start="R_L_", target="__LR"))
