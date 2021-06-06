'''
设计推特
设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近十条推文。
你的设计需要支持以下的几个功能：

postTweet(userId, tweetId): 创建一条新的推文
getNewsFeed(userId): 检索最近的十条推文。每个推文都必须是由此用户关注的人或者是用户自己发出的。推文必须按照时间顺序由最近的开始排序。
follow(followerId, followeeId): 关注一个用户
unfollow(followerId, followeeId): 取消关注一个用户
示例:

Twitter twitter = new Twitter();

// 用户1发送了一条新推文 (用户id = 1, 推文id = 5).
twitter.postTweet(1, 5);

// 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
twitter.getNewsFeed(1);

// 用户1关注了用户2.
twitter.follow(1, 2);

// 用户2发送了一个新推文 (推文id = 6).
twitter.postTweet(2, 6);

// 用户1的获取推文应当返回一个列表，其中包含两个推文，id分别为 -> [6, 5].
// 推文id6应当在推文id5之前，因为它是在5之后发送的.
twitter.getNewsFeed(1);

// 用户1取消关注了用户2.
twitter.unfollow(1, 2);

// 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
// 因为用户1已经不再关注用户2.
twitter.getNewsFeed(1);
'''
from collections import defaultdict
from typing import List
import heapq
'''
思路：哈希+数组+堆
现实时间中推文的数量及其多，故取所有关注的人的10条推文，遍历所有推文并用作者是否关注的人来过滤时间复杂度比较高。
而每个人关注的人数通常是一个较小的数量级，可以从关注的所有人（含自身）每个人都抓取最新的10条数据，然后从这些数据中选择最新的10条即可。

时间复杂度：
postTweet:O(1)
follow:O(1)
unfollow:O(1)
getNewsFeed:O(m)，m为平均每个人关注的用户数量
'''


class Twitter:
    def __init__(self):
        self.follows = defaultdict(set)  # key为用户id,value为set,存放每个人所关注的所有人
        self.tweets = defaultdict(list)  # key为用户id，value为list,存放每个人的所有推文
        self.time = 0  # 时间戳

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))  # 将推文以(时间戳，推文id)的方式存储，便于按照时间戳排序
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        ans = None
        if len(self.tweets[userId]) > 10:
            ans = self.tweets[userId][-10:]
        else:
            ans = self.tweets[userId].copy()
        heapq.heapify(ans)  # 用堆进行排序，因为堆默认是最小堆，时间戳最旧的在最前面
        # 遍历用户的所有关注
        for otherUserId in self.follows[userId]:
            # 提取该用户最新的10条推文，加入堆
            tweets = self.tweets[otherUserId]
            start = 0 if len(tweets) <= 10 else len(tweets) - 10
            for i in range(len(tweets) - 1, start - 1, -1):
                if len(ans) < 10:
                    heapq.heappush(ans, tweets[i])
                elif tweets[i][0] > ans[0][0]:
                    heapq.heapreplace(ans, tweets[i])
                else:  # 该关注用户的最新推文已经晚于堆中最旧的，剩下的不需要继续遍历
                    break
        return list(map(lambda t: t[1], sorted(ans, reverse=True)))

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)


twitter = Twitter()
twitter.postTweet(1, 4)
twitter.postTweet(2, 5)
twitter.unfollow(1, 2)
twitter.getNewsFeed(1)

twitter = Twitter()
twitter.postTweet(1, 1)
twitter.getNewsFeed(1)
twitter.follow(2, 1)
twitter.getNewsFeed(2)
twitter.unfollow(2, 1)
twitter.getNewsFeed(2)

twitter = Twitter()
twitter.postTweet(1, 5)
twitter.getNewsFeed(1)
twitter.follow(1, 2)
twitter.postTweet(2, 6)
twitter.getNewsFeed(1)
twitter.unfollow(1, 2)
twitter.getNewsFeed(1)
