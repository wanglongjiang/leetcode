'''
重构字符串

给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。

若可行，输出任意可行的结果。若不可行，返回空字符串。

示例 1:

输入: S = "aab"
输出: "aba"
示例 2:

输入: S = "aaab"
输出: ""
注意:

S 只包含小写字母并且长度在[1, 500]区间内。
'''
'''
思路：计数+排序
首先对所有字母进行计数，如果最多的字符超过1半，肯定无法重新排布。
如果最多的字符不超过一半，可以进行排布，排布方法是
按照字符的个数进行排序，然后依次输出到数组中，
最后从前一半、后一半依次取字符，插入到结果数组

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def reorganizeString(self, s: str) -> str:
        import collections
        counter = collections.Counter(s)
        tops = counter.most_common()
        n = len(s)
        half = n // 2 + n % 2
        if tops[0][1] > half:  # 第1个字符超过1半，肯定不可行
            return ''
        arr = []
        for char, count in tops:
            for i in range(count):
                arr.append(char)
        arr1, arr2 = arr[:half], arr[half:]
        # 交替输出所有字符
        ans = []
        for i in range(half):
            ans.append(arr1[i])
            if i < len(arr2):
                ans.append(arr2[i])
        return ''.join(ans)


s = Solution()
print(s.reorganizeString("aab"))
print(s.reorganizeString("aaab"))
