'''
重新排列句子中的单词
「句子」是一个用空格分隔单词的字符串。给你一个满足下述格式的句子 text :

句子的首字母大写
text 中的每个单词都用单个空格分隔。
请你重新排列 text 中的单词，使所有单词按其长度的升序排列。如果两个单词的长度相同，则保留其在原句子中的相对顺序。

请同样按上述格式返回新的句子。

 

示例 1：

输入：text = "Leetcode is cool"
输出："Is cool leetcode"
解释：句子中共有 3 个单词，长度为 8 的 "Leetcode" ，长度为 2 的 "is" 以及长度为 4 的 "cool" 。
输出需要按单词的长度升序排列，新句子中的第一个单词首字母需要大写。
示例 2：

输入：text = "Keep calm and code on"
输出："On and keep calm code"
解释：输出的排序情况如下：
"On" 2 个字母。
"and" 3 个字母。
"keep" 4 个字母，因为存在长度相同的其他单词，所以它们之间需要保留在原句子中的相对顺序。
"calm" 4 个字母。
"code" 4 个字母。
示例 3：

输入：text = "To be or not to be"
输出："To be or to be not"
 

提示：

text 以大写字母开头，然后包含若干小写字母以及单词间的单个空格。
1 <= text.length <= 10^5
'''
'''
思路：归并排序
按照单词长度排序，因为要保持原顺序，需要使用稳定的排序，又最大长度为10^5，所以使用冒泡、选择等排序可能会超时，使用归并
时间复杂度：O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split(' ')
        words[0] = words[0][:1].lower() + words[0][1:]

        def sort(left, right):
            if right - left > 1:
                mid = (right + left) // 2
                sort(left, mid)
                sort(mid, right)
                larr = words[left:mid]
                rarr = words[mid:right]
                i, j = 0, 0
                lsize, rsize = mid - left, right - mid
                while i < lsize or j < rsize:
                    if (i < lsize and j < rsize and len(larr[i]) <= len(rarr[j])) or j == rsize:
                        words[left] = larr[i]
                        i += 1
                    else:
                        words[left] = rarr[j]
                        j += 1
                    left += 1

        sort(0, len(words))
        words[0] = words[0][:1].upper() + words[0][1:]
        return ' '.join(words)


s = Solution()
print(s.arrangeWords("Leetcode is cool"))
print(s.arrangeWords("Keep calm and code on"))
print(s.arrangeWords("To be or not to be"))
