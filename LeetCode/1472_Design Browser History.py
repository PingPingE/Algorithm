'''
You have a browser of one tab where you start on the homepage and you can visit another url, 
get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

- BrowserHistory(string homepage) Initializes the object with the homepage of the browser.

- void visit(string url) Visits url from the current page. It clears up all the forward history.

- string back(int steps) Move steps back in history. 
If you can only return x steps in the history and steps > x, you will return only x steps. 
Return the current url after moving back in history at most steps.

- string forward(int steps) Move steps forward in history. 
If you can only forward x steps in the history and steps > x, you will forward only x steps. 
Return the current url after forwarding in history at most steps.
'''
#sol1: 328 ms	16.6 MB
from collections import deque
class BrowserHistory:
    def __init__(self, homepage: str):
        self.back_list = [homepage]
        self.forward_list = deque()
        
    def visit(self, url: str) -> None:
        self.back_list.append(url)
        self.forward_list.clear() #forward_list 비우기
        
    def back(self, steps: int) -> str:
        # print("steps:",steps, "cur back: ",self.back_list)
        while steps:
            steps -= 1
            if len(self.back_list)<=1: break
            self.forward_list.appendleft(self.back_list.pop()) #back_list pop, forward_list push
        return self.back_list[-1]
    
    def forward(self, steps: int) -> str:
        # print("steps:",steps, "cur forward: ",self.forward_list)
        while steps:
            steps -= 1
            if len(self.forward_list)==0: break
            self.back_list.append(self.forward_list.popleft()) #forward_list popleft, back_list push
        return self.back_list[-1]

#sol2: 216 ms	16.5 MB -> list를 하나만, 인덱스를 저장하는 변수 두개만 쓰기
from collections import deque
class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.total_cnt = 0 #가장 마지막 index
        self.index=0 #현재 페이지의 index
        
    def visit(self, url: str) -> None:
        self.history = self.history[:self.index+1]
        self.history.append(url)
        self.index+=1
        self.total_cnt = self.index
        
    def back(self, steps: int) -> str:
        self.index = max(0, self.index-steps)
        return self.history[self.index]
    
    def forward(self, steps: int) -> str:
        self.index=min(self.total_cnt, self.index+steps)
        return self.history[self.index]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)