'''
剑指 Offer II 098. 路径的数目
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

 

示例 1：



输入：m = 3, n = 7
输出：28
示例 2：

输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下
示例 3：

输入：m = 7, n = 3
输出：28
示例 4：

输入：m = 3, n = 3
输出：6
 

提示：

1 <= m, n <= 100
题目数据保证答案小于等于 2 * 109
 

注意：本题与主站 62 题相同： https://leetcode-cn.com/problems/unique-paths/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/2AoeFn
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
解题思路：数学
数学中的组合公式
一个m*n的网络，想要移动到右下角，可以看成是m-1个向下指令与n-1个的向右指令的组合
组合公式为=(m-1+n-1)!/(m-1)!*(n-1)!

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m, n = (m - 1, n - 1) if m > n else (n - 1, m - 1)
        nFac, sumFac = 1, 1
        for i in range(1, n + 1):
            nFac *= i
            sumFac *= m + i
        return sumFac // nFac
