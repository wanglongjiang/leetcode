'''
TinyURL 的加密与解密
TinyURL是一种URL简化服务， 比如：当你输入一个URL https://leetcode.com/problems/design-tinyurl 时，
它将返回一个简化的URL http://tinyurl.com/4e9iAk.

要求：设计一个 TinyURL 的加密 encode 和解密 decode 的方法。你的加密和解密算法如何设计和运作是没有限制的，
你只需要保证一个URL可以被加密成一个TinyURL，并且这个TinyURL可以用解密方法恢复成原本的URL。

'''
import random
'''
思路：哈希+随机
随机生成1个6位的字符串，将其与输入的url进行绑定。
encode的算法：
1. 生成6位随机字符串randStr，判断哈希表中是否存在，如果存在则重新生成，直至生成1个不存在的随机字符串
2. 将randStr与longUrl进行绑定，写入哈希表中
3. 返回'http://tinyurl.com/'+randStr

decode的算法：
1. 取得'http://tinyurl.com/'后面的randStr
2. 检查randStr在哈希表中是否存在，如果存在返回该字符串
'''


class Codec:
    def __init__(self):
        self.data = {}
        self.chars = []
        for ch in range(ord('a'), ord('z') + 1):
            self.chars.append(chr(ch))
        for ch in range(ord('A'), ord('Z') + 1):
            self.chars.append(chr(ch))
        for ch in range(ord('0'), ord('9') + 1):
            self.chars.append(chr(ch))

    def randomStr(self):
        s = []
        for i in range(6):
            s.append(self.chars[random.randint(0, len(self.chars) - 1)])
        return ''.join(s)

    def encode(self, longUrl: str) -> str:
        randStr = self.randomStr()
        while randStr in self.data:  # 创建一个未使用的随机字符串
            randStr = self.randomStr()
        self.data[randStr] = longUrl
        return 'http://tinyurl.com/' + randStr

    def decode(self, shortUrl: str) -> str:
        randStr = shortUrl[len('http://tinyurl.com/'):]
        if randStr in self.data:
            return self.data[randStr]
