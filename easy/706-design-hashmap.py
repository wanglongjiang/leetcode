'''
不使用任何内建的哈希表库设计一个哈希映射（HashMap）。

实现 MyHashMap 类：

MyHashMap() 用空映射初始化对象
void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key 已经存在于映射中，则更新其对应的值 value 。
int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。
void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。

'''


class MyHashMap:
    def __init__(self):
        self.factor = 0.75  # 装载系数
        self.bucketSize = 32
        self.bucket = [[] for i in range(self.bucketSize)]
        self.count = 0

    def hash(self, key: int) -> int:
        return key % self.bucketSize

    def resize(self):
        newBucketSize = self.bucketSize * 2  # 桶的数量变为原先的2倍
        self.bucketSize = newBucketSize
        newBucket = [[] for i in range(newBucketSize)]
        # 将旧容器里面的元素复制到新容器
        for li in self.bucket:
            for node in li:
                newBucket[self.hash(node[0])].append(node)
        self.bucket = newBucket

    def put(self, key: int, value: int) -> None:
        if (self.count / self.bucketSize) >= self.factor:  # 如果已有的元素数超过了装载系数，扩展容器
            self.resize()
        li = self.bucket[self.hash(key)]
        for node in li:
            if node[0] == key:
                node[1] = value
                return
        self.bucket[self.hash(key)].append([key, value])
        self.count += 1

    def get(self, key: int) -> int:
        li = self.bucket[self.hash(key)]
        for node in li:
            if node[0] == key:
                return node[1]
        return -1

    def remove(self, key: int) -> None:
        li = self.bucket[self.hash(key)]
        for i in range(len(li)):
            if li[i][0] == key:
                del li[i]
                self.count -= 1
                return


myHashMap = MyHashMap()
myHashMap.put(1, 1)
myHashMap.put(2, 2)
print(myHashMap.get(1))
print(myHashMap.get(3))
myHashMap.put(2, 1)
print(myHashMap.get(2))
myHashMap.remove(2)
print(myHashMap.get(2))
