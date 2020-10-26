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

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)