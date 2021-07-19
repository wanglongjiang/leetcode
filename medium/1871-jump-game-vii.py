'''
跳跃游戏 VII

给你一个下标从 0 开始的二进制字符串 s 和两个整数 minJump 和 maxJump 。一开始，你在下标 0 处，且该位置的值一定为 '0' 。当同时满足如下条件时，你可以从下标 i 移动到下标 j 处：

i + minJump <= j <= min(i + maxJump, s.length - 1) 且
s[j] == '0'.
如果你可以到达 s 的下标 s.length - 1 处，请你返回 true ，否则返回 false 。

 

示例 1：

输入：s = "011010", minJump = 2, maxJump = 3
输出：true
解释：
第一步，从下标 0 移动到下标 3 。
第二步，从下标 3 移动到下标 5 。
示例 2：

输入：s = "01101110", minJump = 2, maxJump = 3
输出：false
 

提示：

2 <= s.length <= 10^5
s[i] 要么是 '0' ，要么是 '1'
s[0] == '0'
1 <= minJump <= maxJump < s.length

'''
'''
思路：BFS
每次跳跃将minJump到maxJump之间的为'0'的坐标都加入下一次跳跃的坐标。
TODO 超时
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        q, nextq = [], []
        visited = [False] * n
        q.append(0)
        while q:
            i = q.pop()
            if i == n - 1:
                return True
            for j in range(i + minJump, min(i + maxJump + 1, n)):
                if s[j] == '0' and not visited[j]:
                    visited[j] = True
                    nextq.append(j)
            if not q:
                q, nextq = nextq, q
        return False


s = Solution()
print(s.canReach(s="011010", minJump=2, maxJump=3))
print(s.canReach(s="01101110", minJump=2, maxJump=3))
