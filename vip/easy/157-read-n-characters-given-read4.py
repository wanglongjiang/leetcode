'''
157. 用 Read4 读取 N 个字符
给你一个文件，并且该文件只能通过给定的 read4 方法来读取，请实现一个方法使其能够读取 n 个字符。

read4 方法：

API read4 可以从文件中读取 4 个连续的字符，并且将它们写入缓存数组 buf 中。

返回值为实际读取的字符个数。

注意 read4() 自身拥有文件指针，很类似于 C 语言中的 FILE *fp 。

read4 的定义：

参数类型: char[] buf4
返回类型: int

注意: buf4[] 是目标缓存区不是源缓存区，read4 的返回结果将会复制到 buf4[] 当中。
下列是一些使用 read4 的例子：



File file("abcde"); // 文件名为 "abcde"， 初始文件指针 (fp) 指向 'a'
char[] buf4 = new char[4]; // 创建一个缓存区使其能容纳足够的字符
read4(buf4); // read4 返回 4。现在 buf4 = "abcd"，fp 指向 'e'
read4(buf4); // read4 返回 1。现在 buf4 = "e"，fp 指向文件末尾
read4(buf4); // read4 返回 0。现在 buf = ""，fp 指向文件末尾
read 方法：

通过使用 read4 方法，实现 read 方法。该方法可以从文件中读取 n 个字符并将其存储到缓存数组 buf 中。您 不能 直接操作文件。

返回值为实际读取的字符。

read 的定义：

参数类型:   char[] buf, int n
返回类型:   int

注意: buf[] 是目标缓存区不是源缓存区，你需要将结果写入 buf[] 中。


示例 1：

输入： file = "abc", n = 4
输出： 3
解释： 当执行你的 read 方法后，buf 需要包含 "abc"。 文件一共 3 个字符，因此返回 3。 注意 "abc" 是文件的内容，不是 buf 的内容，
buf 是你需要写入结果的目标缓存区。
示例 2：

输入： file = "abcde", n = 5
输出： 5
解释： 当执行你的 read 方法后，buf 需要包含 "abcde"。文件共 5 个字符，因此返回 5。
示例 3:

输入： file = "abcdABCD1234", n = 12
输出： 12
解释： 当执行你的 read 方法后，buf 需要包含 "abcdABCD1234"。文件一共 12 个字符，因此返回 12。
示例 4:

输入： file = "leetcode", n = 5
输出： 5
解释： 当执行你的 read 方法后，buf 需要包含 "leetc"。文件中一共 5 个字符，因此返回 5。


提示：

你 不能 直接操作该文件，文件只能通过 read4 获取而 不能 通过 read。
read  函数只在每个测试用例调用一次。
你可以假定目标缓存数组 buf 保证有足够的空间存下 n 个字符。
'''
"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
'''
思路：设计 交互
设变量count为已读取到的字符数，同时也是buf的指针
当count<n时，调用read4，读取readCharCount个字符，将writeCharCount=min(n-count,readCharCount)个字符写入到buf中，
并将count+=min(n-count,x)，如果x<4，中断后续读取过程
'''


def read4(buf4) -> int:
    pass


class Solution:
    def read(self, buf, n):
        count = 0
        buf4 = [0, 0, 0, 0]
        while count < n:
            readCharCount = read4(buf4)
            writeCharCount = min(n - count, readCharCount)
            for i in range(writeCharCount):
                buf[count + i] = buf4[i]
            count += writeCharCount
            if readCharCount < 4:
                break
        return count
