'''
379. 电话目录管理系统
设计一个电话目录管理系统，让它支持以下功能：

get: 分配给用户一个未被使用的电话号码，获取失败请返回 -1
check: 检查指定的电话号码是否被使用
release: 释放掉一个电话号码，使其能够重新被分配


示例：

// 初始化电话目录，包括 3 个电话号码：0，1 和 2。
PhoneDirectory directory = new PhoneDirectory(3);

// 可以返回任意未分配的号码，这里我们假设它返回 0。
directory.get();

// 假设，函数返回 1。
directory.get();

// 号码 2 未分配，所以返回为 true。
directory.check(2);

// 返回 2，分配后，只剩一个号码未被分配。
directory.get();

// 此时，号码 2 已经被分配，所以返回 false。
directory.check(2);

// 释放号码 2，将该号码变回未分配状态。
directory.release(2);

// 号码 2 现在是未分配状态，所以返回 true。
directory.check(2);


提示：

1 <= maxNumbers <= 10^4
0 <= number < maxNumbers
调用方法的总数处于区间 [0 - 20000] 之内
'''
'''
思路：设计 哈希
设一个变量number，保存下一个待分配的最大电话号码。
设一个哈希表released，保存已释放的号码。

get：如果number<maxNumbers,分配一个未曾分配过的号码；否则从哈希表released中随机挑选一个分配。
check：如果号码>=number或者在released中不存在，未被分配。
release：号码加入哈希表

时间复杂度：3个函数都是O(1)
'''


class PhoneDirectory:
    def __init__(self, maxNumbers: int):
        self.maxNumbers = maxNumbers
        self.number = 0
        self.relased = set()

    def get(self) -> int:
        ans = -1
        if self.number < self.maxNumbers:
            ans = self.number
            self.number += 1
        elif self.relased:
            ans = self.relased.pop()
        return ans

    def check(self, number: int) -> bool:
        return number < self.maxNumbers or number not in self.relased

    def release(self, number: int) -> None:
        self.relased.add(number)
