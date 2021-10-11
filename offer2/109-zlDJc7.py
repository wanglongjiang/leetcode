'''
剑指 Offer II 109. 开密码锁
一个密码锁由 4 个环形拨轮组成，每个拨轮都有 10 个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。

锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。

列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。

字符串 target 代表可以解锁的数字，请给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 -1 。

 

示例 1:

输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
输出：6
解释：
可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，因为当拨动到 "0102" 时这个锁就会被锁定。
示例 2:

输入: deadends = ["8888"], target = "0009"
输出：1
解释：
把最后一位反向旋转一次即可 "0000" -> "0009"。
示例 3:

输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
输出：-1
解释：
无法旋转到目标数字且不被锁定。
示例 4:

输入: deadends = ["0000"], target = "8888"
输出：-1
 

提示：

1 <= deadends.length <= 500
deadends[i].length == 4
target.length == 4
target 不在 deadends 之中
target 和 deadends[i] 仅由若干位数字组成
 

注意：本题与主站 752 题相同： https://leetcode-cn.com/problems/open-the-lock/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zlDJc7
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：BFS
每个数字可以前进的路径是每位数字上+1或-1，使用BFS从0000开始，尝试前进到target，中间不能经过deadends中的路径。
如果能找到路径，返回最短路径的长度。
官方有启发式算法A*，值得学习

时间复杂度：O(80000)
空间复杂度：O(10000)
'''


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deads = set(map(lambda x: int(x), deadends))  # 转化为整数并加入set
        target = int(target)  # 转化为整数
        if 0 in deads:  # 起始坐标就在deadends中，直接返回-1
            return -1
        visited = [False] * 10000

        # 获取从坐标node开始，能到达的坐标list
        def getNextNodes(node):
            nexts = []
            for i in range(4):  # 对于4位数字中的每一位，尝试+1或-1，变动后的新坐标用addNodeId尝试加入list
                m, d = 10**(i + 1), 10**i
                n = (node % m) // d
                if n == 9:
                    addNodeId(node - 9 * d, nexts)
                    addNodeId(node - d, nexts)
                elif n == 0:
                    addNodeId(node + 9 * d, nexts)
                    addNodeId(node + d, nexts)
                else:
                    addNodeId(node - d, nexts)
                    addNodeId(node + d, nexts)
            return nexts

        def addNodeId(nextid, nexts):
            if nextid not in deads and not visited[nextid]:
                nexts.append(nextid)
                visited[nextid] = True

        # 用bfs遍历从0开始到target的路径
        q, nextq = [], []
        q.append(0)
        visited[0] = True
        d = 0
        while q:
            node = q.pop()
            if node == target:
                return d
            nextq.extend(getNextNodes(node))
            if not q:
                q, nextq = nextq, q
                d += 1
        return -1
