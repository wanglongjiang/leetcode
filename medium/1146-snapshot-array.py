'''
快照数组
实现支持下列接口的「快照数组」- SnapshotArray：

SnapshotArray(int length) - 初始化一个与指定长度相等的 类数组 的数据结构。初始时，每个元素都等于 0。
void set(index, val) - 会将指定索引 index 处的元素设置为 val。
int snap() - 获取该数组的快照，并返回快照的编号 snap_id（快照号是调用 snap() 的总次数减去 1）。
int get(index, snap_id) - 根据指定的 snap_id 选择快照，并返回该快照指定索引 index 的值。
 

示例：

输入：["SnapshotArray","set","snap","set","get"]
     [[3],[0,5],[],[0,6],[0,0]]
输出：[null,null,0,null,5]
解释：
SnapshotArray snapshotArr = new SnapshotArray(3) # 初始化一个长度为 3 的快照数组
snapshotArr.set(0,5)  # 令 array[0] = 5
snapshotArr.snap()  # 获取快照，返回 snap_id = 0
snapshotArr.set(0,6)
snapshotArr.get(0,0)  # 获取 snap_id = 0 的快照中 array[0] 的值，返回 5
 

提示：

1 <= length <= 50000
题目最多进行50000 次set，snap，和 get的调用 。
0 <= index < length
0 <= snap_id < 我们调用 snap() 的总次数
0 <= val <= 10^9

来源：力扣（LeetCode）
链接：https:#leetcode-cn.com/problems/snapshot-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from sortedcontainers import SortedDict
'''
思路：有序集合
设一个长度为length的数组nums，它的每个元素都是有序集合SortedDict，dict的key为snap_id，val为set设置的值
1. set会通过nums下标找到SortedDict，然后key=snap_id，添加元素
时间复杂度：O(logn)

2. snap将snapid+1
时间复杂度：O(1)

3. get会通过nums下标找到SortedDict，然后key=snap_id，找到值
时间复杂度：O(logn)

'''


class SnapshotArray:
    def __init__(self, length: int):
        self.snapid = 0
        self.nums = [SortedDict() for _ in range(length)]
        for i in range(length):
            self.set(i, 0)

    def set(self, index: int, val: int) -> None:
        self.nums[index][self.snapid] = val

    def snap(self) -> int:
        snapid = self.snapid
        self.snapid += 1
        return snapid

    def get(self, index: int, snap_id: int) -> int:
        sd = self.nums[index]
        i = sd.bisect_right(snap_id)
        return sd[sd.keys()[i - 1]]


snapshotArr = SnapshotArray(4)  # 初始化一个长度为 4 的快照数组
snapshotArr.snap()  # 获取快照，返回 snap_id = 0
snapshotArr.snap()  # 获取快照，返回 snap_id = 0
print(snapshotArr.get(3, 1))
snapshotArr.set(2, 4)
snapshotArr.snap()
print(snapshotArr.get(1, 4))  # 获取 snap_id = 0 的快照中 array[0] 的值，返回 5

snapshotArr = SnapshotArray(3)  # 初始化一个长度为 3 的快照数组
snapshotArr.set(0, 5)  # 令 array[0] = 5
snapshotArr.snap()  # 获取快照，返回 snap_id = 0
snapshotArr.set(0, 6)
print(snapshotArr.get(0, 0))  # 获取 snap_id = 0 的快照中 array[0] 的值，返回 5
