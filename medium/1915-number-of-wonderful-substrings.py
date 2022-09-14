'''
1915. 最美子字符串的数目
如果某个字符串中 至多一个 字母出现 奇数 次，则称其为 最美 字符串。

例如，"ccjjc" 和 "abab" 都是最美字符串，但 "ab" 不是。
给你一个字符串 word ，该字符串由前十个小写英文字母组成（'a' 到 'j'）。请你返回 word 中 最美非空子字符串 的数目。如果同样的子字符串在 word 中出现多次，那么应当对 每次出现 分别计数。

子字符串 是字符串中的一个连续字符序列。

 

示例 1：

输入：word = "aba"
输出：4
解释：4 个最美子字符串如下所示：
- "aba" -> "a"
- "aba" -> "b"
- "aba" -> "a"
- "aba" -> "aba"
示例 2：

输入：word = "aabb"
输出：9
解释：9 个最美子字符串如下所示：
- "aabb" -> "a"
- "aabb" -> "aa"
- "aabb" -> "aab"
- "aabb" -> "aabb"
- "aabb" -> "a"
- "aabb" -> "abb"
- "aabb" -> "b"
- "aabb" -> "bb"
- "aabb" -> "b"
示例 3：

输入：word = "he"
输出：2
解释：2 个最美子字符串如下所示：
- "he" -> "h"
- "he" -> "e"
 

提示：

1 <= word.length <= 105
word 由从 'a' 到 'j' 的小写英文字母组成
'''
from collections import defaultdict
'''
思路：位运算
将一个字符串中字符是否偶数用一个整数bitmap表示，bitmap第0位表示'a'的出现次数是否奇数次，第1位表示'b'，依次类推。
设一个哈希表bitmapSet，用于保存bitmap。
遍历所有从0开始字符串的bitmap，
1. 当下标i的bitmap出现在哈希表，说明之前有若干下标能与当前下标构成完美字符串，因为2个相同的bitmap相减后，字符都是偶数个。
2. 然后从0遍历到9，依次将bitmap的每一位取反，如果在哈希表中存在，也能构成完美字符串，因为只有1bit不同，也就是字符有1个是奇数个。
上述1.2.处理完成后，将当前的bitmap加入哈希表。

时间复杂度：O(n)，遍历一次word，每个字符处理10次
空间复杂度：O(2^10)，一共10种字符，最多有2^10个bitmap
'''


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        bitmapSet = defaultdict(int)
        bitmapSet[0] = 1
        bitmap, ans = 0, 0
        for char in word:
            bitmap ^= 1 << (ord(char) - ord('a'))  # 计算截止当前的字符的bitmap
            ans += bitmapSet[bitmap]  # 累计全部是偶数字符的子串
            for i in range(10):
                ans += bitmapSet[bitmap ^ (1 << i)]  # 累计只有1个奇数字符的子串
            bitmapSet[bitmap] += 1
        return ans


s = Solution()
print(s.wonderfulSubstrings("aba"))
print(s.wonderfulSubstrings("aabb"))
print(s.wonderfulSubstrings("he"))
