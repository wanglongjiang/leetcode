'''
Pony.ai-002. 车辆安排
目前小马智行已经获得了加州 RoboTaxi 服务的许可，意味着小马智行已经可以在加州向所有的公众提供服务。
于是在未来的某一天，小马智行在加州已经拥有了 N 辆自动驾驶车辆可以面向公众服务，这些车总共有 26 种颜色，颜色分别为小写字母 a 到 z。现在已知在 Pony 的服务系统 PonyPilot 中，总共有 M 个乘客正在排队，其中每个乘客也有各自的车辆颜色偏好,颜色范围也是 a 到 z。
现在运营小 P 突然有了一个奇怪的想法：小 P 想知道总共有多少个位置连续的子队列，能够满足现有的所有车辆可以在同一时刻把子队列中的乘客同时接上乘客喜爱的颜色的车。注意每个车辆只能接一个乘客，且车的颜色要恰好是乘客喜欢的颜色。

输入描述:
第一行输入两个数字 N，M。N 代表车辆数，M 代表乘客人数。

第二行输入一个字符串 A，长度为 N，表示每辆车的颜色。

第三行输入一个字符串 B，长度为 M，表示当前排队的乘客分别喜欢的车的颜色。

其中，1<=N<=1000000，1<=M<=1000000。

输出描述:
输出一个数，即总共满足要求的子队列数。

示例 1:


输入
4 6
pony
pponyy

输出
12

说明
满足的子队列分别为（[]内为子队列对应的下标区间）：
p, [0, 0]
p, [1, 1]
o, [2, 2]
po, [1, 2]
n, [3, 3]
on, [2, 3]
pon, [1, 3]
y, [4, 4]
ny, [3, 4]
ony, [2, 4]
pony, [1, 4]
y, [5, 5]
示例 2：


输入
2 2
ab
ba

输出
3

说明
满足的子队列分别为（[]内为子队列对应的下标区间）：
b, [0, 0]
ba, [0, 1]
a, [1, 1]
注意：本题需要自行编写「标准输入」和「标准输出」逻辑，以及自行 import/include 需要的 library。了解书写规则
'''
from collections import Counter
'''
思路：滑动窗口

一、首先读取输入，carColor为所有车辆颜色的计数，likeColor为用户的用车队列

二、然后用滑动窗口使窗口内的元素不超过carColor的数量，对窗口的队列计算子队列个数
设left,right指针，初始指向乘客队列的索引0
1. 向右移动right指针，如果指向的的颜色在carColor中存在且窗口内的个数不超过carColor中的数量，
   计算以right指针为结尾的队列中的子队列个数，然后继续读入下一个；否则执行2
2. 向右移动left指针，直至窗口中的颜色均在carColor中，且窗口内的个数不超过carColor中的数量
3. 重复上面1.2，直至right移动到likeColor的末尾

三、输出结果

时间复杂度：O(m)
'''

# 从终端读取收入
n, m = map(int, input().split())
carColor = Counter(input())
likeColor = input()
ans = 0

# 滑动窗口累计子队列个数
left, right = 0, 0
windowCount = Counter()
while right < m:
    if right < m and likeColor[right] in carColor and windowCount[likeColor[right]] < carColor[likeColor[right]]:
        windowCount[likeColor[right]] += 1
        right += 1
        ans += right - left  # 累计以right结尾的队列数
    elif right < m:
        if likeColor[right] not in carColor:  # 队列中的颜色不在车队中，需要跳过该用户
            right += 1
            left = right
        else:
            while left < right and windowCount[likeColor[right]] == carColor[likeColor[right]]:
                windowCount[likeColor[left]] -= 1
                left += 1
# 输出结果
print(ans)
