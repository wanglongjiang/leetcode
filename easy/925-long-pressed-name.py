'''
长按键入
你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。

你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。

 

示例 1：

输入：name = "alex", typed = "aaleex"
输出：true
解释：'alex' 中的 'a' 和 'e' 被长按。
示例 2：

输入：name = "saeed", typed = "ssaaedd"
输出：false
解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。
示例 3：

输入：name = "leelee", typed = "lleeelee"
输出：true
示例 4：

输入：name = "laiden", typed = "laiden"
输出：true
解释：长按名字中的字符并不是必要的。
 

提示：

name.length <= 1000
typed.length <= 1000
name 和 typed 的字符都是小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/long-pressed-name
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：双指针
设2指针pn,pt分别指向name,typed，初始值都是0
> 如果pn,pt指向的字符相同，指针分别向前移动一步
> 如果pn,pt指向的字符不同，
>> 如果pt指向的字符与pn-1指向的字符相同，pt向前移动
>> 如果不满足上述条件，返回false
> 重复上述过程直至某个指针到了末尾

如果pn,pt都指向末尾，2个字符是匹配的,返回true
如果pt到了末尾，pn未到，name里有未匹配的，返回false
如果pn到了末尾，pt~n之间的字符与name最后一个字符相同

时间复杂度：O(m+n)，m=len(name),n=len(typed)
空间复杂度：O(1)
'''


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        m, n = len(name), len(typed)
        pn, pt = 0, 0
        while pn < m and pt < n:
            if name[pn] == typed[pt]:
                pn += 1
                pt += 1
            else:
                if pn > 0 and name[pn - 1] == typed[pt]:
                    pt += 1
                else:
                    return False
        if pn == m and pt == n:
            return True
        if pt == n:
            return False
        for i in range(pt, n):
            if typed[i] != name[-1]:
                return False
        return True
