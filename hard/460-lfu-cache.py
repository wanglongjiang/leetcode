'''
LFU 缓存
请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。

实现 LFUCache 类：

LFUCache(int capacity) - 用数据结构的容量 capacity 初始化对象
int get(int key) - 如果键存在于缓存中，则获取键的值，否则返回 -1。
void put(int key, int value) - 如果键已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量时，则应该在插入新项之前，
使最不经常使用的项无效。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除 最久未使用 的键。
注意「项的使用次数」就是自插入该项以来对其调用 get 和 put 函数的次数之和。使用次数会在对应项被移除后置为 0 。

为了确定最不常使用的键，可以为缓存中的每个键维护一个 使用计数器 。使用计数最小的键是最久未使用的键。

当一个键首次插入到缓存中时，它的使用计数器被设置为 1 (由于 put 操作)。对缓存中的键执行 get 或 put 操作，使用计数器的值将会递增。
'''
'''
思路：哈希+双重链表
第1重链表为使用频率，每种使用频率为1个节点，value为第2重链表
第2重链表为按照lru组成的队列，最旧的在头部，最新的在尾部
时间复杂度：get,put都是O(1)
空间复杂度：O(n)
TODO
'''


# 频率链表节点
class RateNode:
    def __init__(self, rate=None):
        self.rate = rate
        import collections
        self.lru = collections.OrderedDict()  # 频率链表内部维护一个lru缓存
        self.prev = None
        self.next = None


class DataNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.rateNode = None


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = RateNode()
        self.tail = self.head
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.map:
            # 在缓存中存在，需要将其频率队列+1
            dataNode = self.map[key]
            rateNode = dataNode.rateNode
            prev = rateNode.prev
            if prev.rate != rateNode.rate + 1:  # 如果上一个频率不是当前频率+1，需要创建新的频率节点
                newRateNode = RateNode(rateNode.rate + 1)
                newRateNode.prev = prev
                newRateNode.next = rateNode
                prev.next = newRateNode
                rateNode.prev = newRateNode
                prev = newRateNode
            dataNode.rateNode = prev  # 更改所处的频率节点
            rateNode.lru.pop(key)  # 从原lru中删除
            prev.lru[key] = dataNode  # 添加到新lru中
            if len(rateNode.lru) == 0:  # 如果原lru为空，需要删除改频率队列
                prev.next = rateNode.next
                rateNode.prev = prev
            return dataNode.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            # 在缓存中存在，需要将其频率队列+1
            dataNode = self.map[key]
            rateNode = dataNode.rateNode
            prev = rateNode.prev
            if prev.rate != rateNode.rate + 1:  # 如果上一个频率不是当前频率+1，需要创建新的频率节点
                newRateNode = RateNode(rateNode.rate + 1)
                newRateNode.prev = prev
                newRateNode.next = rateNode
                prev.next = newRateNode
                rateNode.prev = newRateNode
                prev = newRateNode
            dataNode.rateNode = prev  # 更改所处的频率节点
            rateNode.lru.pop(key)  # 从原lru中删除
            prev.lru[key] = dataNode  # 添加到新lru中
            if len(rateNode.lru) == 0:  # 如果原lru为空，需要删除改频率队列
                prev.next = rateNode.next
                rateNode.prev = prev
        else:  # 在缓存中不存在，需要添加到频率为1 的队列中
            pass
