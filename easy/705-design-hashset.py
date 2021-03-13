'''
设计哈希集合
不使用任何内建的哈希表库设计一个哈希集合（HashSet）。

实现 MyHashSet 类：

void add(key) 向哈希集合中插入值 key 。
bool contains(key) 返回哈希集合中是否存在这个值 key 。
void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。
 
'''


class MyHashSet:
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
            for key in li:
                newBucket[self.hash(key)].append(key)
        self.bucket = newBucket

    def add(self, key: int) -> None:
        if (self.count / self.bucketSize) >= self.factor:  # 如果已有的元素数超过了装载系数，扩展容器
            self.resize()
        li = self.bucket[self.hash(key)]
        for k in li:
            if k == key:
                return
        self.bucket[self.hash(key)].append(key)
        self.count += 1

    def remove(self, key: int) -> None:
        li = self.bucket[self.hash(key)]
        for i in range(len(li)):
            if li[i] == key:
                del li[i]
                self.count -= 1
                return

    def contains(self, key: int) -> bool:
        li = self.bucket[self.hash(key)]
        for k in li:
            if k == key:
                return True
        return False


myHashSet = MyHashSet()
myHashSet.add(1)
myHashSet.add(2)
print(myHashSet.contains(1))
print(myHashSet.contains(3))
myHashSet.add(2)
print(myHashSet.contains(2))
myHashSet.remove(2)
print(myHashSet.contains(2))
