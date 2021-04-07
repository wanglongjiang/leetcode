'''
从英文中重建数字
给定一个非空字符串，其中包含字母顺序打乱的英文单词表示的数字0-9。按升序输出原始的数字。

注意:

输入只包含小写英文字母。
输入保证合法并可以转换为原始的数字，这意味着像 "abc" 或 "zerone" 的输入是不允许的。
输入字符串的长度小于 50,000。
'''
'''
思路：字母计数+筛选法。
10个数字的英文单词是：zero,one,two,three,four,five,six,seven,eight,nine
可以看出有独有字母的是：zero:z,two:w,four:u,six:x,eight:g
如果从字符串中将上述单词都筛选掉，含有f的肯定是five，含有s的肯定是seven,含有t的肯定是three,含有o的肯定是one，剩下的都是nine
算法如下：
1、遍历字符串s，将每个字母进行计数，统计到表格中
2、从表格中筛选掉含有独有字母的单词
3、从表格中筛选掉第2轮变得独有得单词
4、统计表格中的i，即为9的数量
时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def originalDigits(self, s: str) -> str:
        count = {}
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        union = [('z', 'zero', 0), ('w', 'two', 2), ('u', 'four', 4), ('x', 'six', 6), ('g', 'eight', 8), ('f', 'five', 5), ('s', 'seven', 7),
                 ('t', 'three', 3), ('o', 'one', 1), ('n', 'nine', 9)]
        ncount = [0] * 10
        for n in union:
            while n[0] in count:
                ncount[n[2]] += 1
                for c in n[1]:
                    count[c] -= 1
                    if count[c] == 0:
                        count.pop(c)
            if len(count) == 0:
                break
        ans = []
        for i in range(10):
            for j in range(ncount[i]):
                ans.append(str(i))
        return ''.join(ans)


s = Solution()
print(s.originalDigits('owoztneoer'))
print(s.originalDigits('fviefuro'))
