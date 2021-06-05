'''
任务调度器
给你一个用字符数组 tasks 表示的 CPU 需要执行的任务列表。其中每个字母表示一种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。
在任何一个单位时间，CPU 可以完成一个任务，或者处于待命状态。

然而，两个 相同种类 的任务之间必须有长度为整数 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

你需要计算完成所有任务所需要的 最短时间 。

提示：

1 <= task.length <= 10^4
tasks[i] 是大写英文字母
n 的取值范围为 [0, 100]
'''
from typing import List
'''
思路：哈希+链表计数
任务执行窗口大小为n，每次从待办任务中拿出任务数最多的n个任务依次执行。
可以用哈希+链表实现每n个周期从待办任务中取出次数最多的n个任务。这里偷个懒用collections.counter
时间复杂度：O(m*n)
空间复杂度：O(m)
'''


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        import collections
        counter = collections.Counter(tasks)
        empty = collections.Counter()
        times = 0
        while len(counter) > 0:
            topTasks = counter.most_common(n + 1)
            counter.subtract(map(lambda t: t[0], topTasks))
            counter = counter - empty  # 去掉为0的任务
            if len(counter) > 0:
                times += n + 1
            else:
                times += len(topTasks)
        return times


s = Solution()
print(s.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=2))
print(s.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=0))
print(s.leastInterval(tasks=["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n=2))
