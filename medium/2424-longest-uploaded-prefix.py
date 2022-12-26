'''
2424. 最长上传前缀
给你一个 n 个视频的上传序列，每个视频编号为 1 到 n 之间的 不同 数字，你需要依次将这些视频上传到服务器。请你实现一个数据结构，在上传的过程中计算 最长上传前缀 。

如果 闭区间 1 到 i 之间的视频全部都已经被上传到服务器，那么我们称 i 是上传前缀。最长上传前缀指的是符合定义的 i 中的 最大值 。

请你实现 LUPrefix 类：

LUPrefix(int n) 初始化一个 n 个视频的流对象。
void upload(int video) 上传 video 到服务器。
int longest() 返回上述定义的 最长上传前缀 的长度。
 

示例 1：

输入：
["LUPrefix", "upload", "longest", "upload", "longest", "upload", "longest"]
[[4], [3], [], [1], [], [2], []]
输出：
[null, null, 0, null, 1, null, 3]

解释：
LUPrefix server = new LUPrefix(4);   // 初始化 4个视频的上传流
server.upload(3);                    // 上传视频 3 。
server.longest();                    // 由于视频 1 还没有被上传，最长上传前缀是 0 。
server.upload(1);                    // 上传视频 1 。
server.longest();                    // 前缀 [1] 是最长上传前缀，所以我们返回 1 。
server.upload(2);                    // 上传视频 2 。
server.longest();                    // 前缀 [1,2,3] 是最长上传前缀，所以我们返回 3 。
 

提示：

1 <= n <= 105
1 <= video <= 105
video 中所有值 互不相同 。
upload 和 longest 总调用 次数至多不超过 2 * 105 次。
至少会调用 longest 一次。
'''
'''
思路：并查集
设一个并查集，初始各节点（video)互不相连。
每次执行upload，将video的根节点设置为下一个节点（如果存在）的根节点，将video的上一个节点的根节点设置为本节点的根节点。这样操作后，将前后节点连结起来。
每次执行longest，返回节点1的根节点。

upload时间复杂度：O(1)
longest时间复杂度：O(1)
'''


class LUPrefix:
    def __init__(self, n: int):
        self.parent = list(range(n + 1))  # 并查集的父节点
        self.uploaded = set()  # 集合，记录某个视频是否已经上传

    def upload(self, video: int) -> None:
        self.uploaded.add(video)
        if video + 1 in self.uploaded:
            self.parent[video] = self.find(video + 1)  # 将当前节点的根节点设置为下一节点的根
        if video - 1 in self.uploaded:
            self.parent[video - 1] = self.parent[video]  # 将上一节点的根设置为当前节点的根

    def find(self, video):
        if self.parent[video] != video:
            self.parent[video] = self.find(self.parent[video])
        return self.parent[video]

    def longest(self) -> int:
        if 1 not in self.uploaded:
            return 0
        return self.find(1)
