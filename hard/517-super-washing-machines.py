'''
超级洗衣机

假设有 n 台超级洗衣机放在同一排上。开始的时候，每台洗衣机内可能有一定量的衣服，也可能是空的。

在每一步操作中，你可以选择任意 m （1 ≤ m ≤ n） 台洗衣机，与此同时将每台洗衣机的一件衣服送到相邻的一台洗衣机。

给定一个非负整数数组代表从左至右每台洗衣机中的衣物数量，请给出能让所有洗衣机中剩下的衣物的数量相等的最少的操作步数。
如果不能使每台洗衣机中衣物的数量相等，则返回 -1。

 

示例 1：

输入: [1,0,5]

输出: 3

解释:
第一步:    1     0 <-- 5    =>    1     1     4
第二步:    1 <-- 1 <-- 4    =>    2     1     3
第三步:    2     1 <-- 3    =>    2     2     2
示例 2：

输入: [0,3,0]

输出: 2

解释:
第一步:    0 <-- 3     0    =>    1     2     0
第二步:    1     2 --> 0    =>    1     1     1
示例 3:

输入: [0,2,0]

输出: -1

解释:
不可能让所有三个洗衣机同时剩下相同数量的衣物。
 

提示：

n 的范围是 [1, 10000]。
在每台超级洗衣机中，衣物数量的范围是 [0, 1e5]。
'''
from typing import List
'''
思路：数组 脑筋急转弯
首先查看衣服的总量是否是洗衣机数量的整数倍，如果不是，肯定无法分开，返回-1
我们把衣服看成是流动的水，水要从高（数量多）的地方流动到低（数量少）的地方，达到平均值之后，停止流动。
同时，水的流动速度受限：
- 水从高地往外流动的时候，会向缺水的2个方向流动，每个方向每次最多减少1;
- 水的洼地要从水多的地方补水，每个方向每次最多补充1
- 水的高峰（单个洗衣机）往外流动的时候，虽然2个方向都可以流动，但每次只能朝一个方向流动，故其需要的流动次数最少也是高峰-平均值

具体算法如下：
1. 合计衣服的总量，计算出其平均量avg。如果总量total/数量n不能整除，返回-1；
2. 设变量totalDiff为0，用于保存截止到当前元素，之前累计的差；ans为0，为当前最少操作次数，也是返回结果；
3. 遍历machines，
    > 如果totalDiff=0，之前的衣服不需要移动，totalDiff = machines[i]-avg，然后ans=max(ans, totalDiff)，意思是当前的位置的衣服差额全部需要从后面补充
    > 如果totalDiff>0, 说明之前的衣服需要向前分流，设diff=machines[i]-avg，
        >> 如果diff>0，前面的衣服需要累加，totalDiff+=diff，然后ans=max(ans, totalDiff)
        >> 如果diff<0，前面的衣服需要减少，totalDiff+=diff，然后ans=max(ans, abs(totalDiff))
        >> 如果diff=0，没有变化
    > 如果totalDiff<0，说明之前的衣服缺少，需要从前面补充，设diff=machines[i]-avg，
        >> 如果diff<0，需要补充更多，totalDiff+=diff，然后ans=max(ans, totalDiff)
        >> 如果diff>0，当前位置需要补充前面缺少的，ans=max(ans, diff)先执行这个赋值的原因是单个洗衣机高出平均值的，每次最多减少一个，然后totalDiff+=diff
        >> 如果diff=0，没有变化
4. 执行完3.遍历之后，最后结果就是ans

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total, n = sum(machines), len(machines)  # 计算合计
        avg, remainder = divmod(total, n)  # 计算平均值
        if remainder > 0:
            return -1
        totalDiff, ans = 0, 0  # 当前累计差额，结果
        for machine in machines:  # 遍历所有洗衣机，算法说明见上面的说明，代码已经经过合并
            diff = machine - avg
            if totalDiff >= 0 or diff < 0:
                totalDiff += diff
                ans = max(ans, abs(totalDiff))
            else:
                ans = max(ans, diff)
                totalDiff += diff
        return ans


s = Solution()
print(s.findMinMoves([1, 0, 5]))
print(s.findMinMoves([0, 3, 0]))
print(s.findMinMoves([0, 2, 0]))
