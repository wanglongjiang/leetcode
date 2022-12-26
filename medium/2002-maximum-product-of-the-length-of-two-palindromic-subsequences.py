'''
2002. 两个回文子序列长度的最大乘积
给你一个字符串 s ，请你找到 s 中两个 不相交回文子序列 ，使得它们长度的 乘积最大 。两个子序列在原字符串中如果没有任何相同下标的字符，则它们是 不相交 的。

请你返回两个回文子序列长度可以达到的 最大乘积 。

子序列 指的是从原字符串中删除若干个字符（可以一个也不删除）后，剩余字符不改变顺序而得到的结果。如果一个字符串从前往后读和从后往前读一模一样，那么这个字符串是一个 回文字符串 。

 

示例 1：

example-1

输入：s = "leetcodecom"
输出：9
解释：最优方案是选择 "ete" 作为第一个子序列，"cdc" 作为第二个子序列。
它们的乘积为 3 * 3 = 9 。
示例 2：

输入：s = "bb"
输出：1
解释：最优方案为选择 "b" （第一个字符）作为第一个子序列，"b" （第二个字符）作为第二个子序列。
它们的乘积为 1 * 1 = 1 。
示例 3：

输入：s = "accbcaxxcxx"
输出：25
解释：最优方案为选择 "accca" 作为第一个子序列，"xxcxx" 作为第二个子序列。
它们的乘积为 5 * 5 = 25 。
 

提示：

2 <= s.length <= 12
s 只含有小写英文字母。
'''
'''
思路：枚举 位运算
字符串最大长度为12，可以枚举1..2^12的数字，每一位代表该索引的字符被选中，枚举到一个数字后，检查数字映射的字符串是否为回文串。
如果是回文串，将其数字加入数组。
最后遍历所有的回文串，将与其不相交的回文串长度相乘，找出最大乘积。

时间复杂度：O(2^2n)
空间复杂度：O(2^n)
'''


class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        palins = []  # 哈希表，保存所有的回文数字
        for num in range(1, 2**n):
            arr = []
            for j in range(n):
                if num & (1 << j):
                    arr.append(s[j])
            # 检查数字映射的序列是否为回文序列，如果是，将其加入数组
            isPalin = True
            for j in range(len(arr) // 2):
                if arr[j] != arr[-j - 1]:
                    isPalin = False
                    break
            if isPalin:
                palins.append(num)
        # 下面开始找到长度乘积最大的不相交回文串
        ans = 0
        for i in range(len(palins)):
            for j in range(i + 1, len(palins)):
                if palins[i] & palins[j] == 0:
                    ans = max(ans, palins[i].bit_count() * palins[j].bit_count())
        return ans


s = Solution()
assert s.maxProduct("jee") == 2
assert s.maxProduct('bb') == 1
assert s.maxProduct("leetcodecom") == 9
assert s.maxProduct("accbcaxxcxx") == 25
