'''
LCP 19. 秋叶收藏集
小扣出去秋游，途中收集了一些红叶和黄叶，他利用这些叶子初步整理了一份秋叶收藏集 leaves， 字符串 leaves 仅包含小写字符 r 和 y， 其中字符 r 表示一片红叶，字符 y 表示一片黄叶。
出于美观整齐的考虑，小扣想要将收藏集中树叶的排列调整成「红、黄、红」三部分。每部分树叶数量可以不相等，但均需大于等于 1。
每次调整操作，小扣可以将一片红叶替换成黄叶或者将一片黄叶替换成红叶。请问小扣最少需要多少次调整操作才能将秋叶收藏集调整完毕。

示例 1：

输入：leaves = "rrryyyrryyyrr"

输出：2

解释：调整两次，将中间的两片红叶替换成黄叶，得到 "rrryyyyyyyyrr"

示例 2：

输入：leaves = "ryr"

输出：0

解释：已符合要求，不需要额外操作

提示：

3 <= leaves.length <= 10^5
leaves 中只包含字符 'r' 和字符 'y'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/UlBDOe
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：模拟+双指针
设left指针初始指向下标1，向右移动直至遇到leaves[left]==y，停止移动
设right指针初始指向下标n-2，向左移动直至遇到leaves[right]==y，停止移动

经过上述操作后，字符串被2个指针切分成左边r部分，中间'r''y'混合部分，右边r部分。
中间的ry混合部分需要对'r''y'分别计数，得到rcount和ycount
如果将所有的r替换成y，成本是rcount
如果保留一个y，剩余的y替换成r，成本是ycount-1
那么ans=min(rcount,ycount-1)

最后：
如果leaves[0]=='y'，这个字符必须必须替换,ans+1
如果leaves[n-1]=='y'，这个字符必须替换,ans+1

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def minimumOperations(self, leaves: str) -> int:
        n = len(leaves)
        left, right = 1, n - 2
        while left < right and leaves[left] == 'r':  # 跳过左侧所有的r
            left += 1
        while right > left and leaves[right] == 'r':  # 跳过右侧所有的r
            right -= 1
        rcount, ycount = 0, 0
        for c in leaves[left:right + 1]:  # 对left,right中间的字符进行计数
            if c == 'r':
                rcount += 1
            else:
                ycount += 1
        ans = min(rcount, ycount - 1) if ycount > 0 else 1  # 当y的个数>0时取min(rcount, ycount - 1)；当y的个数为0时，最多只需要替换1个'r'为'y'
        ans += 1 if leaves[0] == 'y' else 0
        ans += 1 if leaves[n - 1] == 'y' else 0
        return ans


s = Solution()
print(s.minimumOperations('rrrrr') == 1)
print(s.minimumOperations('rrryyyrryyyrr') == 2)
print(s.minimumOperations('ryr') == 0)
print(s.minimumOperations('yyyr') == 1)
print(s.minimumOperations('ryyyy') == 1)
print(s.minimumOperations('yyyyy') == 2)
print(s.minimumOperations('rrryyyryyyyryyyrr') == 2)
print(s.minimumOperations('rrryyyrrrrrrrrryyyrr') == 5)
