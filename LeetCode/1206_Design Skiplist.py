class Link:
    def __init__(self,element=None, next_element=None ):
        self.element = element
        self.next_element = next_element

class Skiplist:
    def __init__(self):
        self.sorted_list = [Link()]
        self.count = 0
    def search(self, target: int) -> bool:
        current = self.sorted_list[0]
        while current.next_element or current.element != target:
            current = current.next_element
        return True if current.element==target else False

    def add(self, num: int) -> None:
        stat = False
        for ind in range(0, len(self.sorted_list))
            current = self.sorted_list[ind]
            while current.next_element:
                if current.next_element <num:
                    current = current.next_element
                else:
                    break
            if current.next_element:
                tmp = current.next_element
                current.next_element = Link(num,tmp)     
        

    def erase(self, num: int) -> bool:
        


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)