'''
2102. 序列顺序查询
一个观光景点由它的名字 name 和景点评分 score 组成，其中 name 是所有观光景点中 唯一 的字符串，score 是一个整数。
景点按照最好到最坏排序。景点评分 越高 ，这个景点越好。如果有两个景点的评分一样，那么 字典序较小 的景点更好。

你需要搭建一个系统，查询景点的排名。初始时系统里没有任何景点。这个系统支持：

添加 景点，每次添加 一个 景点。
查询 已经添加景点中第 i 好 的景点，其中 i 是系统目前位置查询的次数（包括当前这一次）。
比方说，如果系统正在进行第 4 次查询，那么需要返回所有已经添加景点中第 4 好的。
注意，测试数据保证 任意查询时刻 ，查询次数都 不超过 系统中景点的数目。

请你实现 SORTracker 类：

SORTracker() 初始化系统。
void add(string name, int score) 向系统中添加一个名为 name 评分为 score 的景点。
string get() 查询第 i 好的景点，其中 i 是目前系统查询的次数（包括当前这次查询）。
 

示例：

输入：
["SORTracker", "add", "add", "get", "add", "get", "add", "get", "add", "get", "add", "get", "get"]
[[], ["bradford", 2], ["branford", 3], [], ["alps", 2], [], ["orland", 2], [], ["orlando", 3], [], ["alpine", 2], [], []]
输出：
[null, null, null, "branford", null, "alps", null, "bradford", null, "bradford", null, "bradford", "orland"]

解释：
SORTracker tracker = new SORTracker() # 初始化系统
tracker.add("bradford", 2) # 添加 name="bradford" 且 score=2 的景点。
tracker.add("branford", 3) # 添加 name="branford" 且 score=3 的景点。
tracker.get()              # 从好带坏的景点为：branford ，bradford 。
                            # 注意到 branford 比 bradford 好，因为它的 评分更高 (3 > 2) 。
                            # 这是第 1 次调用 get() ，所以返回最好的景点："branford" 。
tracker.add("alps", 2)     # 添加 name="alps" 且 score=2 的景点。
tracker.get()              # 从好到坏的景点为：branford, alps, bradford 。
                            # 注意 alps 比 bradford 好，虽然它们评分相同，都为 2 。
                            # 这是因为 "alps" 字典序 比 "bradford" 小。
                            # 返回第 2 好的地点 "alps" ，因为当前为第 2 次调用 get() 。
tracker.add("orland", 2)   # 添加 name="orland" 且 score=2 的景点。
tracker.get()              # 从好到坏的景点为：branford, alps, bradford, orland 。
                            # 返回 "bradford" ，因为当前为第 3 次调用 get() 。
tracker.add("orlando", 3)  # 添加 name="orlando" 且 score=3 的景点。
tracker.get()              # 从好到坏的景点为：branford, orlando, alps, bradford, orland 。
                            # 返回 "bradford".
tracker.add("alpine", 2)   # 添加 name="alpine" 且 score=2 的景点。
tracker.get()              # 从好到坏的景点为：branford, orlando, alpine, alps, bradford, orland 。
                            # 返回 "bradford" 。
tracker.get()              # 从好到坏的景点为：branford, orlando, alpine, alps, bradford, orland 。
                            # 返回 "orland" 。
 

提示：

name 只包含小写英文字母，且每个景点名字互不相同。
1 <= name.length <= 10
1 <= score <= 105
任意时刻，调用 get 的次数都不超过调用 add 的次数。
总共 调用 add 和 get 不超过 4 * 104 
'''
from heapq import heappop, heappush, heappushpop, heapreplace
'''
思路：对顶堆
设置2个堆，一个最小堆minHeap，一个最大堆maxHeap
如果当前已经查询了count次
minHeap保存前count个景点，maxHeap保存之后的景点

当执行add时，
首先与minHeap的最小元素对比，如果大于minHeap最小元素，加入minHeap，同时将minHeap最小元素加入maxHeap
如果小于minHeap的最小元素，加入maxHeap

当执行get时，
返回maxHeap的最大元素，同时将其加入minHeap

因为需要对比成绩和名称，且在最小堆和最大堆里的比较方式相反，所以定义了2个辅助类MinNode和MaxNode

时间复杂度：每次执行add,时间复杂度为O(logn)，每次执行get，时间复杂度为O(logn)
空间复杂度：O(n)
'''


class MinNode:
    def __init__(self, name: int, score: str):
        self.name = name
        self.score = score

    def __lt__(self, other: object):
        if self.score == other.score:
            return self.name > other.name
        return self.score < other.score


class MaxNode:
    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score

    def __lt__(self, other):
        if self.score == other.score:
            return self.name < other.name
        return self.score > other.score


class SORTracker:
    def __init__(self):
        self.minHeap, self.maxHeap = [], []

    def add(self, name: str, score: int) -> None:
        minNode = heappushpop(self.minHeap, MinNode(name, score))
        heappush(self.maxHeap, MaxNode(minNode.name, minNode.score))

    def get(self) -> str:
        maxNode = heappop(self.maxHeap)
        heappush(self.minHeap, MinNode(maxNode.name, maxNode.score))
        return maxNode.name


tracker = SORTracker()

tracker.add("bradford", 2)  # 添加 name="bradford" 且 score=2 的景点。
tracker.add("branford", 3)  # 添加 name="branford" 且 score=3 的景点。
tracker.get()  # 从好带坏的景点为：branford ，bradford 。
# 注意到 branford 比 bradford 好，因为它的 评分更高 (3 > 2) 。
# 这是第 1 次调用 get() ，所以返回最好的景点："branford" 。
tracker.add("alps", 2)  # 添加 name="alps" 且 score=2 的景点。
tracker.get()  # 从好到坏的景点为：branford, alps, bradford 。
# 注意 alps 比 bradford 好，虽然它们评分相同，都为 2 。
# 这是因为 "alps" 字典序 比 "bradford" 小。
# 返回第 2 好的地点 "alps" ，因为当前为第 2 次调用 get() 。
tracker.add("orland", 2)  # 添加 name="orland" 且 score=2 的景点。
tracker.get()  # 从好到坏的景点为：branford, alps, bradford, orland 。
# 返回 "bradford" ，因为当前为第 3 次调用 get() 。
tracker.add("orlando", 3)  # 添加 name="orlando" 且 score=3 的景点。
tracker.get()  # 从好到坏的景点为：branford, orlando, alps, bradford, orland 。
# 返回 "bradford".
tracker.add("alpine", 2)  # 添加 name="alpine" 且 score=2 的景点。
tracker.get()  # 从好到坏的景点为：branford, orlando, alpine, alps, bradford, orland 。
# 返回 "bradford" 。
tracker.get()  # 从好到坏的景点为：branford, orlando, alpine, alps, bradford, orland 。
