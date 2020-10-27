'''
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed.
Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed.
Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.

Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);
'''

#84 ms	19.5 MB
from collections import defaultdict,deque
class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.followers = defaultdict(list) #key: user, values:[follwers]
        self.followees = defaultdict(list)#key: user, values:[followees]
        self.newspeed = defaultdict(list) #key:user, values:[posts]
        self.time =0 #posts 형식:(-time, post) 
    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.newspeed[userId].append((-self.time, tweetId)) #포스팅 시간을 넣음
        self.time +=1 #시간 증가

    def getNewsFeed(self, userId: int):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        candi = list()
        for target in self.followees[userId]:
            candi.extend(self.newspeed[target][-1:max(-10,-len(self.newspeed[target]))-1:-1] ) #user가 follow하는 사람들의 최근 10개의 posts 넣기
        candi.extend(self.newspeed[userId][-1:max(-10,-len(self.newspeed[userId]))-1:-1]) #user의 최근 10개의 posts넣기
        candi.sort()
        res = []
        for _ in range(min(10, len(candi))):
            res.append(candi[_][1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.followees[followerId] or followeeId == followerId:
            return
        self.followees[followerId].append(followeeId)
        self.followers[followeeId].append(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId not in self.followees[followerId]:
            return
        self.followees[followerId].remove(followeeId)
        self.followers[followeeId].remove(followerId)
