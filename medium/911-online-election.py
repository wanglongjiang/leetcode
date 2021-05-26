'''
在线选举

在选举中，第 i 张票是在时间为 times[i] 时投给 persons[i] 的。

现在，我们想要实现下面的查询函数： TopVotedCandidate.q(int t) 将返回在 t 时刻主导选举的候选人的编号。

在 t 时刻投出的选票也将被计入我们的查询之中。在平局的情况下，最近获得投票的候选人将会获胜。

示例：

输入：["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],
[12],[25],[15],[24],[8]]
输出：[null,0,1,1,0,0,1]
解释：
时间为 3，票数分布情况是 [0]，编号为 0 的候选人领先。
时间为 12，票数分布情况是 [0,1,1]，编号为 1 的候选人领先。
时间为 25，票数分布情况是 [0,1,1,0,0,1]，编号为 1 的候选人领先（因为最近的投票结果是平局）。
在时间 15、24 和 8 处继续执行 3 个查询。
 

提示：

1 <= persons.length = times.length <= 5000
0 <= persons[i] <= persons.length
times 是严格递增的数组，所有元素都在 [0, 10^9] 范围中。
每个测试用例最多调用 10000 次 TopVotedCandidate.q。
TopVotedCandidate.q(int t) 被调用时总是满足 t >= times[0]。
'''
from typing import List
import bisect
'''
思路:计数+二分查找
设置一个counter数组，用于对选票进行计数,counter[i]是第i个候选人获得的选票
设置一个win数组，win[i]用于存放time[i]时刻的领先人
1.在初始化方法里，
> 遍历times和persons数组，将counter[persons[i]]+1
> 然后将win[i]设置为当前领先人
2.在查询方法里，
> 用t查询time数组，查看t所在的坐标i
> 将win[i]加入结果集

时间复杂度：初始化函数为O(n)，单次查询为O(logn)
空间复杂度：O(n)
'''


class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        n = len(persons)
        counter = [0] * n
        self.win = [0] * n
        maxTicketNum, maxPersonNo = 0, 0
        for i in range(n):
            counter[persons[i]] += 1  # 票数加1
            if counter[persons[i]] >= maxTicketNum:  # 如果这个人的得票数>=最高票，更新最高票得主
                maxPersonNo = persons[i]
                maxTicketNum = counter[maxPersonNo]
            self.win[i] = maxPersonNo  # 该时刻胜利人为最高票得主

    def q(self, t: int) -> int:
        i = bisect.bisect_right(self.times, t)
        return self.win[i - 1]
