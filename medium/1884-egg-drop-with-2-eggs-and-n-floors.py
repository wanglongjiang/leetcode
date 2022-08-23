'''
1884. 鸡蛋掉落-两枚鸡蛋
给你 2 枚相同 的鸡蛋，和一栋从第 1 层到第 n 层共有 n 层楼的建筑。

已知存在楼层 f ，满足 0 <= f <= n ，任何从 高于 f 的楼层落下的鸡蛋都 会碎 ，从 f 楼层或比它低 的楼层落下的鸡蛋都 不会碎 。

每次操作，你可以取一枚 没有碎 的鸡蛋并把它从任一楼层 x 扔下（满足 1 <= x <= n）。如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎，则可以在之后的操作中 重复使用 这枚鸡蛋。

请你计算并返回要确定 f 确切的值 的 最小操作次数 是多少？

 

示例 1：

输入：n = 2
输出：2
解释：我们可以将第一枚鸡蛋从 1 楼扔下，然后将第二枚从 2 楼扔下。
如果第一枚鸡蛋碎了，可知 f = 0；
如果第二枚鸡蛋碎了，但第一枚没碎，可知 f = 1；
否则，当两个鸡蛋都没碎时，可知 f = 2。
示例 2：

输入：n = 100
输出：14
解释：
一种最优的策略是：
- 将第一枚鸡蛋从 9 楼扔下。如果碎了，那么 f 在 0 和 8 之间。将第二枚从 1 楼扔下，然后每扔一次上一层楼，在 8 次内找到 f 。总操作次数 = 1 + 8 = 9 。
- 如果第一枚鸡蛋没有碎，那么再把第一枚鸡蛋从 22 层扔下。如果碎了，那么 f 在 9 和 21 之间。将第二枚鸡蛋从 10 楼扔下，然后每扔一次上一层楼，在 12 次内找到 f 。总操作次数 = 2 + 12 = 14 。
- 如果第一枚鸡蛋没有再次碎掉，则按照类似的方法从 34, 45, 55, 64, 72, 79, 85, 90, 94, 97, 99 和 100 楼分别扔下第一枚鸡蛋。
不管结果如何，最多需要扔 14 次来确定 f 。
 

提示：

1 <= n <= 1000
'''
'''
数学
假设对于 n 层楼计算并返回要确定 f 确切的值的最小操作次数为 M ， 我们可以有以下结论：

第一次操作必然选择在 x ≤ M 层，这里使用反证法：当 x > M ，如果第一次操作后鸡蛋破碎，则转入第2枚鸡蛋任务，需要 x - 1 次操作逐层验证，总操作次数为 1 + (x - 1) = x > M ，违背总操作次数为 M 的假设
第 k 次操作第1枚鸡蛋的覆盖层数必须小于等于 M - k + 1 ，原因同 1
综合(1, 2)的限制，可以得出 M 次操作可以覆盖的最大楼层数量为 Sum = M + (M - 1) + (M - 2) + ... + 1 = (M + 1) * M / 2
得到关系：(M + 1) * M / 2 ≥ n，则满足条件的 M 最小值即为最小操作次数，用数学方法求解即可

'''
from math import ceil, sqrt


class Solution:
    def twoEggDrop(self, n: int) -> int:
        return ceil((-1.0 + sqrt(n * 8 + 1)) / 2)