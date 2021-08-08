'''
剑指 Offer II 042. 最近请求次数
写一个 RecentCounter 类来计算特定时间范围内最近的请求。

请实现 RecentCounter 类：

RecentCounter() 初始化计数器，请求数为 0 。
int ping(int t) 在时间 t 添加一个新请求，其中 t 表示以毫秒为单位的某个时间，并返回过去 3000 毫秒内发生的所有请求数（包括新请求）。确切地说，返回在 [t-3000, t] 内发生的请求数。
保证 每次对 ping 的调用都使用比之前更大的 t 值。

 

示例：

输入：
inputs = ["RecentCounter", "ping", "ping", "ping", "ping"]
inputs = [[], [1], [100], [3001], [3002]]
输出：
[null, 1, 2, 3, 3]

解释：
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1]，范围是 [-2999,1]，返回 1
recentCounter.ping(100);   // requests = [1, 100]，范围是 [-2900,100]，返回 2
recentCounter.ping(3001);  // requests = [1, 100, 3001]，范围是 [1,3001]，返回 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002]，范围是 [2,3002]，返回 3
 

提示：

1 <= t <= 109
保证每次对 ping 调用所使用的 t 值都 严格递增
至多调用 ping 方法 104 次
 

注意：本题与主站 933 题相同： https://leetcode-cn.com/problems/number-of-recent-calls/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/H8086Q
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from collections import deque
import bisect
'''
思路1，二分查找
将所有请求保存下来，然后用二分查找查找时间范围内的索引

时间复杂度：单次ping为O(logn)
空间复杂度：O(n)

思路2，队列
将每次ping都加入队列尾部，然后检查队列头部的是否超过时间范围，如果超过，删除

时间复杂度：单次ping最坏情况下是O(3000)，最好是O(1)
空间复杂度：O(3000)
'''


# 思路1，二分查找
class RecentCounter1:
    def __init__(self):
        self.pings = []

    def ping(self, t: int) -> int:
        self.pings.append(t)
        return len(self.pings) - bisect.bisect_left(self.pings, t - 3000)


# 思路2，队列
class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)
