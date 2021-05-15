'''
推多米诺
一行中有 N 张多米诺骨牌，我们将每张多米诺骨牌垂直竖立。

在开始时，我们同时把一些多米诺骨牌向左或向右推。



每过一秒，倒向左边的多米诺骨牌会推动其左侧相邻的多米诺骨牌。

同样地，倒向右边的多米诺骨牌也会推动竖立在其右侧的相邻多米诺骨牌。

如果同时有多米诺骨牌落在一张垂直竖立的多米诺骨牌的两边，由于受力平衡， 该骨牌仍然保持不变。

就这个问题而言，我们会认为正在下降的多米诺骨牌不会对其它正在下降或已经下降的多米诺骨牌施加额外的力。

给定表示初始状态的字符串 "S" 。如果第 i 张多米诺骨牌被推向左边，则 S[i] = 'L'；如果第 i 张多米诺骨牌被推向右边，则 S[i] = 'R'；如果第 i 张多米诺骨牌没有被推动，则 S[i] = '.'。

返回表示最终状态的字符串。

示例 1：

输入：".L.R...LR..L.."
输出："LL.RR.LLRRLL.."
示例 2：

输入："RR.L"
输出："RR.L"
说明：第一张多米诺骨牌没有给第二张施加额外的力。
提示：

0 <= N <= 10^5
表示多米诺骨牌状态的字符串只含有 'L'，'R'; 以及 '.';
'''
'''
思路：双指针
设当前指针i
> 1. i向右遍历，直至遇到L或R，
>>    1.1 如果遇到L，将L左部的.全部改成L
>>    1.2 如果遇到R,当前位置i记录到left指针内，继续向右遍历直至遇到L或R或结束
>> >     如果遇到R或结束，将left到i的所有.改成R, 回到1.2继续执行
>> >     如果遇到L，将当前位置i记录到right指针内，同时移动left,right指针：left指针向右，遇到的每个.改成R，right指针向左，遇到的每个.改成L，直至2个指针相遇。将i+1后回到1.
> 2. 重复上面的过程直至遍历完成

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        ans = ['.'] * n
        i, left, right = 0, 0, 0
        while i < n:
            left = i
            while i < n and dominoes[i] == '.':
                i += 1
            if i < n:
                if dominoes[i] == 'L':
                    for j in range(left, i + 1):
                        ans[j] = 'L'
                    i += 1
                elif dominoes[i] == 'R':
                    left = i
                    i += 1
                    while i < n and dominoes[i] == '.':
                        i += 1
                    if i == n or dominoes[i] == 'R':
                        for j in range(left, i):
                            ans[j] = 'R'
                    else:
                        right = i
                        i += 1
                        while left < right:
                            ans[left] = 'R'
                            ans[right] = 'L'
                            left += 1
                            right -= 1
        return ''.join(ans)


s = Solution()
print(s.pushDominoes("RR.L") == "RR.L")
print(s.pushDominoes(".L.R...LR..L..") == "LL.RR.LLRRLL..")
