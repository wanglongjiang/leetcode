'''
面试题 16.20. T9键盘
在老式手机上，用户通过数字键盘输入，手机将提供与这些数字相匹配的单词列表。每个数字映射到0至4个字母。给定一个数字序列，实现一个算法来返回匹配单词的列表。
你会得到一张含有有效单词的列表。映射如下图所示：



示例 1:

输入: num = "8733", words = ["tree", "used"]
输出: ["tree", "used"]
示例 2:

输入: num = "2", words = ["a", "b", "c", "d"]
输出: ["a", "b", "c"]
提示：

num.length <= 1000
words.length <= 500
words[i].length == num.length
num中不会出现 0, 1 这两个数字
'''
from typing import List
'''
思路：数组遍历
遍历words中每个word，将word转换为数字，然后对比数字与num是否一致。

时间复杂度：O(mn),m=num.length,n=words.length
空间复杂度：O(1)
'''


class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        # 26个字母映射为数字
        charToNum = ['2', '2', '2', '3', '3', '3', '4', '4', '4', '5', '5', '5', '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '9', '9', '9', '9']
        base = ord('a')
        n = len(num)
        ans = []
        for word in words:
            for i in range(n):
                if charToNum[ord(word[i]) - base] != num[i]:  # 如果数字对不上，该单词不会加入结果
                    break
            else:
                ans.append(word)
        return ans


s = Solution()
print(s.getValidT9Words(num="8733", words=["tree", "used"]))
print(s.getValidT9Words(num="2", words=["a", "b", "c", "d"]))
