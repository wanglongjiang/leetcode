'''
水果成篮

在一排树中，第 i 棵树产生 tree[i] 型的水果。
你可以从你选择的任何树开始，然后重复执行以下步骤：

把这棵树上的水果放进你的篮子里。如果你做不到，就停下来。
移动到当前树右侧的下一棵树。如果右边没有树，就停下来。
请注意，在选择一颗树后，你没有任何选择：你必须执行步骤 1，然后执行步骤 2，然后返回步骤 1，然后执行步骤 2，依此类推，直至停止。

你有两个篮子，每个篮子可以携带任何数量的水果，但你希望每个篮子只携带一种类型的水果。

用这个程序你能收集的水果树的最大总量是多少？

 

示例 1：

输入：[1,2,1]
输出：3
解释：我们可以收集 [1,2,1]。

示例 2：
输入：[0,1,2,2]
输出：3
解释：我们可以收集 [1,2,2]
如果我们从第一棵树开始，我们将只能收集到 [0, 1]。

示例 3：
输入：[1,2,3,2,2]
输出：4
解释：我们可以收集 [2,3,2,2]
如果我们从第一棵树开始，我们将只能收集到 [1, 2]。

示例 4：
输入：[3,3,3,1,2,1,1,2,3,3,4]
输出：5
解释：我们可以收集 [1,2,1,1,2]
如果我们从第一棵树或第八棵树开始，我们将只能收集到 4 棵水果树。
 

提示：

1 <= tree.length <= 40000
0 <= tree[i] < tree.length
'''
from typing import List
'''
思路：滑动窗口
设left,right指针初始指向0，1
> 1. 向右移动right指针，扩大窗口范围，直至窗口内水果种类马上于3个，记录窗口大小
> 2. 向右移动left指针，缩小窗口范围，直至窗口内水果只剩1种
> 3. 重复上述1.2.，直至遍历完成

复杂度：
> 时间复杂度：O(n)
> 空间复杂度：O(1)
'''


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        n = len(tree)
        left, right = 0, 0
        a, b = tree[0], -1  # 存放2种水果
        ac, bc = 0, 0  # 每个水果的数量
        ans = 0
        while right < n:
            while right < n and a == tree[right]:  # 扩大窗口范围，直至出现第2种水果
                ac += 1
                right += 1
            if right < n:
                b = tree[right]  # 第2种水果放到b里面
            while right < n and (a == tree[right] or b == tree[right]):  # 扩大窗口范围，直至出现第3种水果
                if a == tree[right]:
                    ac += 1
                else:
                    bc += 1
                right += 1
            ans = max(ans, right - left)
            while ac > 0 and bc > 0:  # 减少窗口范围，直至窗口内只剩一种水果
                if a == tree[left]:
                    ac -= 1
                else:
                    bc -= 1
                left += 1
            if ac == 0:  # 确保b存放新水果
                a = b
                ac = bc
                b = -1
                bc = 0
        return ans


s = Solution()
print(s.totalFruit([1, 2, 1]))
print(s.totalFruit([0, 1, 2, 2]))
print(s.totalFruit([1, 2, 3, 2, 2]))
print(s.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
