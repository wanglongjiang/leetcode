'''
823. 带因子的二叉树
给出一个含有不重复整数元素的数组 arr ，每个整数 arr[i] 均大于 1。

用这些整数来构建二叉树，每个整数可以使用任意次数。其中：每个非叶结点的值应等于它的两个子结点的值的乘积。

满足条件的二叉树一共有多少个？答案可能很大，返回 对 10^9 + 7 取余 的结果。



示例 1:

输入: arr = [2, 4]
输出: 3
解释: 可以得到这些二叉树: [2], [4], [4, 2, 2]
示例 2:

输入: arr = [2, 4, 5, 10]
输出: 7
解释: 可以得到这些二叉树: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].


提示：

1 <= arr.length <= 1000
2 <= arr[i] <= 10^9
arr 中的所有值 互不相同
'''
from typing import List
'''
思路：动态规划
一个数值的子节点只能是其因子，可以用动态规划，先求因子的二叉树数量，所有因子的二叉树之和就是一个数值的二叉树数量。
首先将数组进行排序。
然后设数组dp[n]，dp[i]的含义是以arr[i]为根节点的二叉树数量
状态转移方程为：
dp[i] = sum(dp[j]+dp[k])+1，arr[j]和arr[k]都是arr[i]的因子，最后+1是只有arr[i]自身的二叉树

时间复杂度：O(n^2)
空间复杂度：O(n)
'''


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        m = 10**9 + 7
        arr.sort()
        idxMap = {}  # 保存所有数值和其在arr中的索引，便于后面快速定位因子
        for i, v in enumerate(arr):
            idxMap[v] = i
        dp = [1] * len(arr)  # 初始化为1，每个数值最少可以形成1个二叉树
        for i in range(len(arr)):
            for j in range(i):  # 遍历所有小于arr[i]的数，检查其是否为因子
                d, r = divmod(arr[i], arr[j])
                if arr[j] > d:
                    break
                if r == 0 and d in idxMap:  # 如果找到因子，二叉树数量需要加上2个因子的二叉树数量
                    if d == arr[j] and dp[j] == 1:  # 两个因子相同，形成的二叉树只有1个
                        dp[i] = (dp[i] + dp[j]) % m
                    else:
                        dp[i] = (dp[i] + dp[j] + dp[idxMap[d]]) % m
        return sum(dp) % m


s = Solution()
print(s.numFactoredBinaryTrees([2, 4, 5, 10]))
print(s.numFactoredBinaryTrees([2, 4]))
