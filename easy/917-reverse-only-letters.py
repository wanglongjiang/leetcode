'''
仅仅反转字母
给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。

 

示例 1：

输入："ab-cd"
输出："dc-ba"
示例 2：

输入："a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"
示例 3：

输入："Test1ng-Leet=code-Q!"
输出："Qedo1ct-eeLg=ntse-T!"
 

提示：

S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S 中不包含 \\or "

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-only-letters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：双指针
设置left,right指针，初始指向字符串2端。
然后2个指针分别向内移动，遇到第1个字母停止
交换2个指针指向的字母
持续上面过程，指针2个指针相遇

时间复杂度：O(n)
空间复杂度：O(n)，python中str为不可变对象，需要O(n)空间，换成c语言这种可变的，需要O(1)
'''


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        arr = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not arr[left].isalpha():
                left += 1
            while left < right and not arr[right].isalpha():
                right -= 1
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        return ''.join(arr)


s = Solution()
print(s.reverseOnlyLetters("a-bC-dEf-ghIj"))
