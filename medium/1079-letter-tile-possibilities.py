'''
活字印刷

你有一套活字字模 tiles，其中每个字模上都刻有一个字母 tiles[i]。返回你可以印出的非空字母序列的数目。

注意：本题中，每个活字字模只能使用一次。

 

示例 1：

输入："AAB"
输出：8
解释：可能的序列为 "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"。
示例 2：

输入："AAABBC"
输出：188
 

提示：

1 <= tiles.length <= 7
tiles 由大写英文字母组成
'''
'''
思路：回溯
回溯字模的全排列，相同的字模需要排除，跳过相同组合
时间复杂度：O(n!)
空间复杂度：O(n)
TODO
'''


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        chars = list(tiles)
        chars.sort()
        ans = 0

        def bt():
            nonlocal ans
            for i in range(len(chars)):
                if i > 0 and chars[i - 1] == chars[i]:
                    continue
                if i == len(chars) - 1:
                    continue
                chars[i], chars[-1] = chars[-1], chars[i]
                item = chars.pop()
                backtrack(0)
                if chars:
                    bt()
                chars.append(item)
                chars[i], chars[-1] = chars[-1], chars[i]

        def backtrack(i):
            nonlocal ans
            ans += 1
            for j in range(i + 1, len(chars)):
                if chars[i] != chars[j]:
                    chars[i], chars[j] = chars[j], chars[i]
                    if j < n - 1:
                        ans += 1
                        backtrack(j)
                    chars[i], chars[j] = chars[j], chars[i]

        backtrack(0)
        bt()
        return ans


s = Solution()
print(s.numTilePossibilities('AA'))
print(s.numTilePossibilities('AAB'))
print(s.numTilePossibilities("AAABBC"))
