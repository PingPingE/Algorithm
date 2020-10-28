'''
You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, 
and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). 
Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].

It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

Example 1:

Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]

Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3
'''
#632 ms	 19.3MB	
class RecentCounter:

    def __init__(self):
        self.counter = []

    def ping(self, t: int) -> int:
        self.counter.append(t)
        l,r = 0, len(self.counter)-1
        minn,maxx = t-3000, t
        target = [-1,-1]
        while l<=r:
            m = (l+r)//2
            if self.counter[m] >= minn:
                r=m-1
                target[0] = m
            else:
                l=m+1
                
        l2,r2 = 0,len(self.counter)-1
        while l2<=r2:
            m2 = (l2+r2)//2
            if self.counter[m2] <= maxx:
                l2 = m2+1
                target[1] = m2
            else:
                r2=m2-1
                
        if minn<= self.counter[target[0]] and maxx >= self.counter[target[1]]:
            return target[1]-target[0]+1
        return 0
            


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)