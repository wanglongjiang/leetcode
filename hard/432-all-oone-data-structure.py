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
思路：哈希表 双向链表
哈希表维护key->valueNode的映射；
valueNode根据value大小串联成双向链表。

执行inc时：
> 如果kv中找不到valueNode，找大小为1的valueNode(从head节点开始查找)，在kv中添加key->valueNode
> 如果kv中找到valueNode，查看下一个节点值是否为value+1，如果不是，插入一个新的valueNode，key指向它。如果是，key指向下一个节点。
>> key指向的原节点引用keys减一，如果引用keys为0，删除valueNode

执行dec时：
> 如果kv中找不到valueNode，不做任何事情
> 如果找到valueNode，且val为1，删除kv中的key。节点引用keys减一。
> 如果找到valueNode，且val>1，指向上一个valueNode（上一个valueNode如果不存在，需要插入新的）。原节点引用keys减一。
>> 节点引用keys如果变成0，需要删除valueNode

执行getMaxKey:
从tail节点向上追溯的第1个非head节点，从keys中找到任意一个返回

指向getMinKey:
从头head节点向前追溯的第1个非tail节点，从keys中找到任意一个返回

4个操作时间复杂度均为O(1)

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
        self.head, self.tail = ValueNode(float('-inf')), ValueNode(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        if key not in self.kv:  # 在kv中不存在
            if self.head.next.val == 1:  # 第1个节点就是1，只需要修改第1个节点的引用
                self.head.next.keys.add(key)
                self.kv[key] = self.head.next
            else:  # 第1个节点不是1，需要插入1个值为1的节点
                node = ValueNode(1)
                node.keys.add(key)
                self.kv[key] = node
                node.next = self.head.next
                node.next.prev = node
                self.head.next = node
                node.prev = self.head
        else:
            oldNode = self.kv[key]
            oldNode.keys.remove(key)
            if oldNode.next.val == oldNode.val + 1:  # 下一个节点恰好是当前value+1，只需要修改引用
                oldNode.next.keys.add(key)
                self.kv[key] = oldNode.next
            else:  # 需要插入下一个节点
                node = ValueNode(oldNode.val + 1)
                node.keys.add(key)
                self.kv[key] = node
                node.next = oldNode.next
                node.next.prev = node
                oldNode.next = node
                node.prev = oldNode
            if not oldNode.keys:  # 原节点已经没有key指向，需要删除原节点
                oldNode.prev.next = oldNode.next
                oldNode.next.prev = oldNode.prev

    def dec(self, key: str) -> None:
        if key not in self.kv:
            return
        oldNode = self.kv[key]
        oldNode.keys.remove(key)
        if oldNode.val == 1:
            del self.kv[key]
        else:
            if oldNode.prev.val == oldNode.val - 1:
                oldNode.prev.keys.add(key)
                self.kv[key] = oldNode.prev
            else:
                node = ValueNode(oldNode.val - 1)
                node.keys.add(key)
                self.kv[key] = node
                node.next = oldNode
                node.prev = oldNode.prev
                node.prev.next = node
                node.next.prev = node
        if not oldNode.keys:
            oldNode.prev.next = oldNode.next
            oldNode.next.prev = oldNode.prev

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ''
        node = self.tail.prev
        key = node.keys.pop()
        node.keys.add(key)
        return key

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ''
        node = self.head.next
        key = node.keys.pop()
        node.keys.add(key)
        return key
