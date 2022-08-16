'''
271. 字符串的编码与解码
请你设计一个算法，可以将一个 字符串列表 编码成为一个 字符串。这个编码后的字符串是可以通过网络进行高效传送的，
并且可以在接收端被解码回原来的字符串列表。

1 号机（发送方）有如下函数：

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
2 号机（接收方）有如下函数：

vector<string> decode(string s) {
  //... your code
  return strs;
}
1 号机（发送方）执行：

string encoded_string = encode(strs);
2 号机（接收方）执行：

vector<string> strs2 = decode(encoded_string);
此时，2 号机（接收方）的 strs2 需要和 1 号机（发送方）的 strs 相同。

请你来实现这个 encode 和 decode 方法。

注意：

因为字符串可能会包含 256 个合法 ascii 字符中的任何字符，所以您的算法必须要能够处理任何可能会出现的字符。
请勿使用 “类成员”、“全局变量” 或 “静态变量” 来存储这些状态，您的编码和解码算法应该是非状态依赖的。
请不要依赖任何方法库，例如 eval 又或者是 serialize 之类的方法。本题的宗旨是需要您自己实现 “编码” 和 “解码” 算法。

'''
'''
思路：字符串
编码：
以\n作为特殊字符，作为字符串的间隔。
因原字符串有可能有'\'，所以遇到'\'需要进行转义，两个连续的'\\'为'\'。
解码：
上面编码的逆过程。

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Codec:
    def encode(self, strs: [str]) -> str:
        ans = []
        for s in strs:
            for char in s:
                if char == '\\':
                    ans.append('\\\\')
                else:
                    ans.append(char)
            ans.append('\\n')
        if ans:
            del ans[-1]
        return ''.join(ans)

    def decode(self, s: str) -> [str]:
        ans = []
        curStr = []
        i, n = 0, len(s)
        while i < n:
            if s[i] == '\\':
                if i + 1 < n:
                    if s[i + 1] == '\\':
                        curStr.append('\\')
                    else:
                        ans.append(''.join(curStr))
                        curStr = []
                    i += 1
                else:
                    curStr.append(s[i])
            else:
                curStr.append(s[i])
            i += 1
        if curStr:
            ans.append(''.join(curStr))
        return ans


s = Codec()
print(s.decode(s.encode(['abc', 'cde\\', 'abc\n', 'hig'])))
