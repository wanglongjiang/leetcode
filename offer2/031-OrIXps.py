'''
剑指 Offer II 031. 最近最少使用缓存
运用所掌握的数据结构，设计和实现一个  LRU (Least Recently Used，最近最少使用) 缓存机制 。

实现 LRUCache 类：

LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
 

示例：

输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
 

提示：

1 <= capacity <= 3000
0 <= key <= 10000
0 <= value <= 10^5
最多调用 2 * 10^5 次 get 和 put
 

进阶：是否可以在 O(1) 时间复杂度内完成这两种操作？

 

注意：本题与主站 146 题相同：https://leetcode-cn.com/problems/lru-cache/ 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/OrIXps
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：利用hashmap和双向链表，实现get、put都是O(1)时间复杂度
'''


class DNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = DNode()
        self.tail = self.head
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            self.moveToHead(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            node.prev.next = node.next
            node.next.prev = node.prev
            self.moveToHead(node)
        else:
            if self.capacity <= len(self.map):
                last = self.tail.prev
                self.map.pop(last.key)
                last.prev.next = self.tail
                self.tail.prev = last.prev
            node = DNode(key, value)
            self.moveToHead(node)
            self.map[key] = node

    def moveToHead(self, node: DNode):
        node.prev = self.head
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
