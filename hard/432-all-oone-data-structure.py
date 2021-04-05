'''
全 O(1) 的数据结构
请你实现一个数据结构支持以下操作：

Inc(key) - 插入一个新的值为 1 的 key。或者使一个存在的 key 增加一，保证 key 不为空字符串。
Dec(key) - 如果这个 key 的值是 1，那么把他从数据结构中移除掉。否则使一个存在的 key 值减一。
如果这个 key 不存在，这个函数不做任何事情。key 保证不为空字符串。
GetMaxKey() - 返回 key 中值最大的任意一个。如果没有元素存在，返回一个空字符串"" 。
GetMinKey() - 返回 key 中值最小的任意一个。如果没有元素存在，返回一个空字符串""。
 

挑战：

你能够以 O(1) 的时间复杂度实现所有操作吗？
'''
'''
思路：哈希表。
第1个哈希表维护key->value的映射
第2个哈希表维护value->key set 的映射
还需要维护value 列表
TODO
'''


class ValueNode:
    def __init__(self, val):
        self.val = val
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:
    def __init__(self):
        self.kv = {}
        self.vk = {}

    def inc(self, key: str) -> None:
        newVal = 1
        if key in self.kv:
            valueNode = self.kv[key]
            newVal = valueNode.val + 1
            valueNode.keys.remove(key)
        newValNode = None
        if newVal in self.vk:
            newValNode = self.vk[newVal]
        else:
            newValNode = ValueNode(newVal)
            self.vk[newVal] = newValNode
        newValNode.keys.add(key)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
