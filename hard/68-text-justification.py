'''
文本左右对齐
给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

'''
from typing import List
'''
思路：滑动窗口
一次读入m个单词使得sum(len(word))+m-1<=maxWidth
'''


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)

        def justify(start: int, end: int, wordLen: int):
            if end == n:  # 最后一行，左对齐
                return ' '.join(words[start:end]).ljust(maxWidth)
            elif end - start == 1:  # 只有1个单词，左对齐
                return words[start].ljust(maxWidth)
            else:  # 空格需要平均分配，如果不能完全平均分配，需要左边多于右边
                wordNum = end - start
                spaceNum = maxWidth - wordLen
                intervalNum, remainder = divmod(spaceNum, wordNum - 1)
                s = ''
                for i in range(start, end - 1):
                    s += words[i]
                    for j in range(intervalNum):
                        s += ' '
                    if remainder > 0:
                        s += ' '
                        remainder -= 1
                return s + words[end - 1]

        left = 0
        sumLen = 0
        ans = []
        for i in range(n):
            if sumLen + len(words[i]) + i - left > maxWidth:
                ans.append(justify(left, i, sumLen))
                left = i
                sumLen = len(words[i])
            else:
                sumLen += len(words[i])
        ans.append(justify(left, n, sumLen))
        return ans


s = Solution()
print(
    s.fullJustify(
        ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"],
        20))
print(s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
print(s.fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16))
