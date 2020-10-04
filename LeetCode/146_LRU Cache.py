'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. 
Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

Follow up:
Could you do get and put in O(1) time complexity?
 
'''
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.recent = {}#언제 방문했는지 체크용
        self.time =0

    def get(self, key: int) -> int:
        if key in self.cache:
            self.recent[key] = self.time
            self.time+=1
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            self.cache[key] = value
            self.recent[key] = self.time
        else:
            if len(self.cache)>=self.capacity:
                target=  sorted(self.recent, key = lambda x: self.recent[x])[0] #가장 오랫동안 방문되지 않은 key 추출
                self.cache.pop(target)
                self.recent.pop(target)
            self.cache[key] = value
            self.recent[key] = self.time  
        self.time+=1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)