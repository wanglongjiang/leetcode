'''
854. 相似度为 K 的字符串
对于某些非负整数 k ，如果交换 s1 中两个字母的位置恰好 k 次，能够使结果字符串等于 s2 ，则认为字符串 s1 和 s2 的 相似度为 k 。

给你两个字母异位词 s1 和 s2 ，返回 s1 和 s2 的相似度 k 的最小值。

 

示例 1：

输入：s1 = "ab", s2 = "ba"
输出：1
示例 2：

输入：s1 = "abc", s2 = "bca"
输出：2
 

提示：

1 <= s1.length <= 20
s2.length == s1.length
s1 和 s2  只包含集合 {'a', 'b', 'c', 'd', 'e', 'f'} 中的小写字母
s2 是 s1 的一个字母异位词
'''
'''
思路：BFS 状态压缩
字符串s1每次交换2个不同位置的字符，形成新的字符串s1i，他与s1有一条路径。
按照BFS的思路将其加入队列，每遍历一次队列中的一个字符串，找到其所有一次交换后的变形加入队列，直至找到s2。
因为6个字符可以压缩到3bit，20个字符可以用60bit表示，为加快速度，进行了状态压缩

时间复杂度：O(5^n)
空间复杂度：O(5^n)
'''


class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0
        ans, n = 0, len(s1)
        # 下面的代码段是状态压缩
        bitmap = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}
        int1, int2 = 0, 0
        for i in range(n):
            int1 |= bitmap[s1[i]] << (3 * i)
            int2 |= bitmap[s2[i]] << (3 * i)
        # 下面开始bfs遍历
        q, nextq = [int1], []
        marked = set()
        marked.add(int1)
        while q:
            curint = q.pop()
            for i in range(n - 1):
                if (curint >> (i * 3)) & 7 != (int2 >> (i * 3)) & 7:  # 找到2个字符串第1个不相同的字符，此时开始才需要进行交换
                    break
            for j in range(i + 1, n):
                if (curint >> (j * 3)) & 7 != (int2 >> (i * 3)) & 7:  # 如果该字符串第j个字符，与目标字符串第i个不同，交换没有意义，需要跳过
                    continue
                if (curint >> (i * 3)) & 7 == (curint >> (j * 3)) & 7:  # 如果2个字符串需要交换的字符相同，也没有意义，需要跳过
                    continue
                newint = (curint & ~((7 << (j * 3)) | (7 << (i * 3)))) | (((curint >> (i * 3)) & 7) << (j * 3)) | (((curint >> (j * 3)) & 7) <<
                                                                                                                   (i * 3))  # 交换2个位置的字符
                if newint == int2:
                    return ans + 1
                if newint in marked:  # 已遍历过的状态跳过
                    continue
                marked.add(newint)
                nextq.append(newint)
            if not q:
                q, nextq = nextq, q
                ans += 1
        return ans


curint = Solution()
print(curint.kSimilarity('abcdeabcdeabcdeabcde', 'aaaabbbbccccddddeeee'))
print(curint.kSimilarity('ab', 'ba'))
print(curint.kSimilarity('abc', 'bca'))
print(curint.kSimilarity('abcdeabcde', 'aabbccddee'))
print(curint.kSimilarity('abcdeabcdeabcde', 'aaabbbcccdddeee'))
