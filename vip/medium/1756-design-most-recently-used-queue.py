'''
1756. 设计最近使用（MRU）队列
设计一种类似队列的数据结构，该数据结构将最近使用的元素移到队列尾部。

实现 MRUQueue 类：

MRUQueue(int n)  使用 n 个元素： [1,2,3,...,n] 构造 MRUQueue 。
fetch(int k) 将第 k 个元素（从 1 开始索引）移到队尾，并返回该元素。


示例 1：

输入：
["MRUQueue", "fetch", "fetch", "fetch", "fetch"]
[[8], [3], [5], [2], [8]]
输出：
[null, 3, 6, 2, 2]

解释：
MRUQueue mRUQueue = new MRUQueue(8); // 初始化队列为 [1,2,3,4,5,6,7,8]。
mRUQueue.fetch(3); // 将第 3 个元素 (3) 移到队尾，使队列变为 [1,2,4,5,6,7,8,3] 并返回该元素。
mRUQueue.fetch(5); // 将第 5 个元素 (6) 移到队尾，使队列变为 [1,2,4,5,7,8,3,6] 并返回该元素。
mRUQueue.fetch(2); // 将第 2 个元素 (2) 移到队尾，使队列变为 [1,4,5,7,8,3,6,2] 并返回该元素。
mRUQueue.fetch(8); // 第 8 个元素 (2) 已经在队列尾部了，所以直接返回该元素即可。


提示：

1 <= n <= 2000
1 <= k <= n
最多调用 2000 次 fetch


进阶：找到每次 fetch 的复杂度为 O(n) 的算法比较简单。你可以找到每次 fetch 的复杂度更佳的算法吗？
'''
from sortedcontainers import SortedList
'''
思路：设计 有序集合 O(logn)
将所有整数和其索引形成的序对p(index, num)加入有序集合。
此时有序集合中的元素会以索引进行排序
每次执行fetch(i)，找到集合中第i个元素，将其从集合中删除，然后将(最大索引+1，num)再加入有序集合，经过这样操作后，元素会移动到有序集合末尾

时间复杂度：O(logn)
'''


class MRUQueue:
    def __init__(self, n: int):
        self.maxIdx = n
        self.slist = SortedList(zip(range(n), range(1, n + 1)))

    def fetch(self, k: int) -> int:
        idx, num = self.slist.pop(k - 1)  # 找到集合中第k个元素并删除
        self.slist.add((self.maxIdx, num))  # 索引改为最大索引后再加入集合
        self.maxIdx += 1
        return num


mRUQueue = MRUQueue(8)
print(mRUQueue.fetch(3))
print(mRUQueue.fetch(5))
print(mRUQueue.fetch(2))
print(mRUQueue.fetch(8))
