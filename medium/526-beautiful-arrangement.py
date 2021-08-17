'''
优美的排列
假设有从 1 到 N 的 N 个整数，如果从这 N 个数字中成功构造出一个数组，使得数组的第 i 位 (1 <= i <= N) 满足如下两个条件中的一个，
我们就称这个数组为一个优美的排列。条件：

第 i 位的数字能被 i 整除
i 能被第 i 位上的数字整除
现在给定一个整数 N，请问可以构造多少个优美的排列？

示例1:

输入: 2
输出: 2
解释:

第 1 个优美的排列是 [1, 2]:
  第 1 个位置（i=1）上的数字是1，1能被 i（i=1）整除
  第 2 个位置（i=2）上的数字是2，2能被 i（i=2）整除

第 2 个优美的排列是 [2, 1]:
  第 1 个位置（i=1）上的数字是2，2能被 i（i=1）整除
  第 2 个位置（i=2）上的数字是1，i（i=2）能被 1 整除
说明:

N 是一个正整数，并且不会超过15。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/beautiful-arrangement
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：回溯 状态压缩
1..N的数字，每次尝试占用一个，回溯查找。
因为N最大是15，可以用15个bit来表示

时间复杂度：O(n!)
空间复杂度：O(n)
'''


class Solution:
    def countArrangement(self, n: int) -> int:
        finish = (1 << n) - 1  # 最低n位全是1的终止状态

        def backtrack(idx, status):
            if status == finish:
                return 1
            ans = 0
            for i in range(n):
                if (1 << i) & status == 0 and ((i + 1) % idx == 0 or idx % (i + 1) == 0):
                    ans += backtrack(idx + 1, (1 << i) | status)
            return ans

        return backtrack(1, 0)


s = Solution()
print(s.countArrangement(2))
print(s.countArrangement(1))
print(s.countArrangement(3))
print(s.countArrangement(15))
