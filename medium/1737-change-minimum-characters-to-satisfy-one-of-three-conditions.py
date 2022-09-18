'''
1737. 满足三条件之一需改变的最少字符数
给你两个字符串 a 和 b ，二者均由小写字母组成。一步操作中，你可以将 a 或 b 中的 任一字符 改变为 任一小写字母 。

操作的最终目标是满足下列三个条件 之一 ：

a 中的 每个字母 在字母表中 严格小于 b 中的 每个字母 。
b 中的 每个字母 在字母表中 严格小于 a 中的 每个字母 。
a 和 b 都 由 同一个 字母组成。
返回达成目标所需的 最少 操作数。

 

示例 1：

输入：a = "aba", b = "caa"
输出：2
解释：满足每个条件的最佳方案分别是：
1) 将 b 变为 "ccc"，2 次操作，满足 a 中的每个字母都小于 b 中的每个字母；
2) 将 a 变为 "bbb" 并将 b 变为 "aaa"，3 次操作，满足 b 中的每个字母都小于 a 中的每个字母；
3) 将 a 变为 "aaa" 并将 b 变为 "aaa"，2 次操作，满足 a 和 b 由同一个字母组成。
最佳的方案只需要 2 次操作（满足条件 1 或者条件 3）。
示例 2：

输入：a = "dabadd", b = "cda"
输出：3
解释：满足条件 1 的最佳方案是将 b 变为 "eee" 。
 

提示：

1 <= a.length, b.length <= 105
a 和 b 只由小写字母组成
'''
'''
思路：计数
首先，分别统计2个字符串中字符的个数。
然后，用一个二重循环，a设置为从字符'a'-'z'，b设置为'a'-'z'，计算需要进行的改动数，找到最小的那个。

时间复杂度：O(n+C^3)，C为字符集大小
空间复杂度：O(1)，最多有26个字符，数组大小固定
'''


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        counta, countb = [0] * 26, [0] * 26
        for ch in a:
            counta[ord(ch) - ord('a')] += 1
        for ch in b:
            countb[ord(ch) - ord('a')] += 1
        ans = float('inf')
        for i in range(26):
            changeAlei = sum(counta[i + 1:])  # a变化为<=i的变化次数
            changeBgti = sum(countb[:i + 1]) if i < 25 else float('inf')  # b变化为>i的变化次数
            changeAgei = sum(counta[:i])  # a变化为>=i的变化次数
            changeBlti = sum(countb[i:]) if i > 0 else float('inf')  # b变化为<i的变化次数
            changeAeqi = sum(counta) - counta[i]  # a变化为全为i的变化次数
            changeBeqi = sum(countb) - countb[i]  # b变化为全为i的变化次数
            ans = min(ans, changeAlei + changeBgti, changeAgei + changeBlti, changeAeqi + changeBeqi)
        return ans


s = Solution()
print(s.minCharacters(a="aba", b="caa"))
print(s.minCharacters(a="dabadd", b="cda"))
