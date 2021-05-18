'''
前K个高频单词

给一非空的单词列表，返回前 k 个出现次数最多的单词。

返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。

示例 1：

输入: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
输出: ["i", "love"]
解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
    注意，按字母顺序 "i" 在 "love" 之前。


示例 2：

输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
输出: ["the", "is", "sunny", "day"]
解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
    出现次数依次为 4, 3, 2 和 1 次。
 

注意：

假定 k 总为有效值， 1 ≤ k ≤ 集合元素数。
输入的单词均由小写字母组成。
 

扩展练习：

尝试以 O(n log k) 时间复杂度和 O(n) 空间复杂度解决。
'''
from typing import List
from collections import defaultdict
import heapq
'''
思路：堆+哈希
看到 O(n log k) 的时间复杂度，就想到了堆，建一个k大小的堆，遍历每个单词的出行频率，最后堆中剩下的单词即为top k
具体算法：
1. 用哈希统计每个单词的出现频率
2. 遍历所有单词的(单词,频率)对，将其加入大小为k的最小堆中
3. 输出堆中所有单词，逆序

复杂性分析
> 时间复杂度：O(nlogk)。第1步哈希需要O(n*l)l为单词平均长度，第2步建堆为O(nlogk)
> 空间复杂度：O(n)，哈希表最坏情况下需要O(n)空间
'''


# 定义了一个打包类，重载了>、<等比较运算符，便于给堆运算使用
class Pair:
    def __init__(self, word, count):
        self.word = word
        self.count = count

    def __lt__(self, value):
        return self.count < value.count or (self.count == value.count and self.word > value.word)

    def __le__(self, value):
        return self.count <= value.count or (self.count == value.count and self.word >= value.word)

    def __gt__(self, value):
        return self.count > value.count or (self.count == value.count and self.word < value.word)

    def __ge__(self, value):
        return self.count >= value.count or (self.count == value.count and self.word <= value.word)

    def __eq__(self, value):
        return self.count == value.count or (self.count == value.count and self.word == value.word)


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # 统计所有单词的出现频率
        counter = defaultdict(int)
        for word in words:
            counter[word] += 1
        # 将单词及出现频率打包
        wds = [Pair(word, cnt) for word, cnt in counter.items()]
        heap = []
        # 将单词加入堆中
        for wd in wds:
            if len(heap) < k:
                heapq.heappush(heap, wd)
            else:
                if wd > heap[0]:
                    heapq.heapreplace(heap, wd)
        ans = []
        while heap:
            ans.append(heapq.heappop(heap).word)
        ans.reverse()
        return ans


s = Solution()
print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], k=2))
print(s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k=4))
