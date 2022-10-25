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
回溯字模的全排列，相同的字模需要排除，用哈希集合排重
时间复杂度：O(n!)
空间复杂度：O(n)
'''


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        hashset = set()
        chars = list(tiles)

        def backtrack(i):
            if i == n:
                return
            hashset.add(''.join(chars[:i + 1]))
            for j in range(i + 1, n):
                if chars[i] != chars[j]:
                    chars[i], chars[j] = chars[j], chars[i]
                    hashset.add(''.join(chars[:i + 1]))
                    backtrack(i + 1)
                    chars[i], chars[j] = chars[j], chars[i]
            backtrack(i + 1)

        backtrack(0)
        return len(hashset)


s = Solution()
print(s.numTilePossibilities('AAB'))
print(s.numTilePossibilities('AA'))
print(s.numTilePossibilities("AAABBC"))
print(s.numTilePossibilities('v'))
