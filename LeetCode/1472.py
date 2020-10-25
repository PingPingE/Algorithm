class Linked_List:
    def __init__(self, cur = None,prev_url=None, next_url=None):
        self.cur = cur
        self.prev_url = prev_url
        self.next_url = next_url
class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = Linked_List(cur = homepage)
        
    def visit(self, url: str) -> None:
        self.history.next_url = Linked_List(cur= url, prev_url = self.history.cur)
        
    def back(self, steps: int) -> str:
        step = steps
        current = self.history
        while step:
            step -=1
            if current.prev_url is None:
                return current.cur
            current = current.prev_url
        return current.cur
    
    def forward(self, steps: int) -> str:
        step = steps
        current = self.history
        while step:
            step -=1
            if current.next_url is None:
                return current.cur
            current = current.next_url
        return current.cur

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)