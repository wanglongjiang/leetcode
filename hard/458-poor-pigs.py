'''
458. 可怜的小猪
有 buckets 桶液体，其中 正好 有一桶含有毒药，其余装的都是水。它们从外观看起来都一样。为了弄清楚哪只水桶含有毒药，
你可以喂一些猪喝，通过观察猪是否会死进行判断。不幸的是，你只有 minutesToTest 分钟时间来确定哪桶液体是有毒的。

喂猪的规则如下：

选择若干活猪进行喂养
可以允许小猪同时饮用任意数量的桶中的水，并且该过程不需要时间。
小猪喝完水后，必须有 minutesToDie 分钟的冷却时间。在这段时间里，你只能观察，而不允许继续喂猪。
过了 minutesToDie 分钟后，所有喝到毒药的猪都会死去，其他所有猪都会活下来。
重复这一过程，直到时间用完。
给你桶的数目 buckets ，minutesToDie 和 minutesToTest ，返回在规定时间内判断哪个桶有毒所需的 最小 猪数。



示例 1：

输入：buckets = 1000, minutesToDie = 15, minutesToTest = 60
输出：5
示例 2：

输入：buckets = 4, minutesToDie = 15, minutesToTest = 15
输出：2
示例 3：

输入：buckets = 4, minutesToDie = 15, minutesToTest = 30
输出：2


提示：

1 <= buckets <= 1000
1 <= minutesToDie <= minutesToTest <= 100
'''
'''
思路：信息熵

测试案例中最简单的情况，4个桶，毒药生效时间是15分钟，一共给了15分钟。
每个猪有2种状态：第15分钟死去，第15分钟活着。
4个桶可以用2只猪来表示这个信息，具体操作：
2个猪编号是：0，1，4个桶编号是：0，1，2，3
第0个猪喝掉0，2桶，第1个猪喝掉1，2桶，第3桶没有猪喝。
如果2个猪都死掉，就是第2桶有毒；如果单独某一个猪死掉，那么就是第0或1有毒；如果都活着，就是第3桶有毒。

推论，如果有1000桶水，毒药生效时间是15分钟，一共给了60分钟。
那么一个猪可能有5种状态：15分钟死，30分钟死，45分钟死，60分钟死，60分钟活。
如果想要找到1000桶水中的毒药，需要的状态至少是5头猪，5^5=3125>1000。

上面的思路来源于看过的知乎的一篇关于信息熵的文章：
https://www.zhihu.com/question/60227816/answer/1274071217

时间复杂度：O(logn)
空间复杂度：O(1)
'''


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if buckets == 1:  # 特别处理，如果只有1桶水，肯定有毒
            return 0
        n = minutesToTest // minutesToDie + 1
        s, ans = n, 1
        while s < buckets:
            s *= n
            ans += 1
        return ans


s = Solution()
print(s.poorPigs(1, 1, 1))
print(s.poorPigs(buckets=1000, minutesToDie=15, minutesToTest=60))
print(s.poorPigs(buckets=4, minutesToDie=15, minutesToTest=15))
print(s.poorPigs(buckets=4, minutesToDie=15, minutesToTest=30))
