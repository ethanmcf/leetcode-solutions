class Twitter:

    def __init__(self):
        self.following = {}
        self.userTweets = {}
        self.tweetTime = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.userTweets:
            self.userTweets[userId] = []
        self.userTweets[userId].append(tweetId)
        self.tweetTime[tweetId] = self.time
        self.time += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        self.follow(userId, userId)
        tempHeap = []
        for followee in self.following[userId]:
            if followee not in self.userTweets:
                continue
            tweets = self.userTweets[followee]
            for i in range(min(10, len(tweets))):
                tweet = tweets[len(tweets) - 1 - i]
                heapq.heappush(tempHeap, [-self.tweetTime[tweet], tweet])
        top10 = []
        for i in range(min(10, len(tempHeap))):
            top10.append(heapq.heappop(tempHeap)[1])
        return top10

    def follow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            if followeeId in self.following[followerId]:
                self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
