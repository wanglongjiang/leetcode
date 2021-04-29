'''
根据身高重建队列

假设有打乱顺序的一群人站成一个队列，数组 people 表示队列中一些人的属性（不一定按顺序）。每个 people[i] = [hi, ki] 表示第 i 个人的身高为 hi ，
前面 正好 有 ki 个身高大于或等于 hi 的人。

请你重新构造并返回输入数组 people 所表示的队列。返回的队列应该格式化为数组 queue ，其中 queue[j] = [hj, kj] 是队列中第 j 个人的属性（queue[0] 是排在队列前面的人）。

提示：

1 <= people.length <= 2000
0 <= hi <= 10^6
0 <= ki < people.length
题目数据确保队列可以被重建
'''
from typing import List
'''
思路：排序+回溯
建立一个二维数组sortedItems，下标表示前面有几个人，值为list，具有相同k值的人在同一个list
重建队列queue时，从sortedItems[0..len(queue)]中查找满足条件item.h>queue = item.k的元素，
找到一个后，尝试加入队列，如果回溯成功，则返回，否则尝试下一个
时间复杂度：O(n^2)
空间复杂度：O(n)
'''


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        sortedItems = [[] for _ in range(n)]
        for item in people:
            sortedItems[item[1]].append(item)
        for items in sortedItems:
            items.sort(key=lambda item: item[0], reverse=True)  # 按照身高逆序，便于pop()操作
        queue = []

        def backtrack():
            maxK = len(queue)
            for i in range(maxK + 1):
                if sortedItems[i]:
                    item = sortedItems[i][-1]  # 取出该队列中身高最低的人
                    count = 0
                    for other in queue:
                        if other[0] >= item[0]:
                            count += 1
                            if count > i:  # 如果前面高于当前人的人数多于指定的，退出循环
                                break
                    if count == i:  # 如果身高人数匹配，加入队列
                        queue.append(sortedItems[i].pop())
                        if len(queue) == n:
                            return True
                        if backtrack():
                            return True
                        else:
                            sortedItems[i].append(queue.pop())
            return False

        backtrack()
        return queue


s = Solution()
print(s.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]) == [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]])
print(s.reconstructQueue([[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]) == [[4, 0], [5, 0], [2, 2], [3, 2], [1, 4], [6, 0]])
