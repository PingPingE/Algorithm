import string
class Node():
    def __init__(self, data, next_n, ind):
        self.data = data
        self.next_n = []
        if next_n:
            self.next_n.append(next_n)
        self.ind = ind

class Trie():
    def __init__(self):
        self.node = Node('',None,-1)
        for e,alph in enumerate(string.ascii_uppercase,1):
            self.node.next_n.append(Node(alph, None, e))
        self.ind = 27
        
    def search(self, total_data):
        result = []
        s=0
        while s<len(total_data):
            cur = self.node
            data= total_data[s]
            for current in cur.next_n:
                if current.data == data:
                    stat= True
                    e=2
                    target_ind = current.ind
                    while stat and s+e<=len(total_data):
                        next_data = total_data[s:s+e]
                        for k in current.next_n:
                            if next_data == k.data:
                                target_ind = k.ind
                                e+=1
                                break
                        else:
                            current.next_n.append(Node(next_data, None, self.ind))
                            self.ind+=1
                            stat=False
                    
                    result.append(target_ind)
                    s= s+e-1
                    break
                else: continue
        return result
               
def solution(msg):
    trie = Trie()
    return trie.search(msg)

'''
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.4MB)
테스트 2 〉	통과 (0.05ms, 10.3MB)
테스트 3 〉	통과 (0.04ms, 10.5MB)
테스트 4 〉	통과 (0.62ms, 10.4MB)
테스트 5 〉	통과 (0.10ms, 10.4MB)
테스트 6 〉	통과 (0.73ms, 10.4MB)
테스트 7 〉	통과 (1.07ms, 10.5MB)
테스트 8 〉	통과 (0.84ms, 10.4MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.71ms, 10.4MB)
테스트 11 〉	통과 (0.63ms, 10.3MB)
테스트 12 〉	통과 (1.20ms, 10.3MB)
테스트 13 〉	통과 (1.97ms, 10.4MB)
테스트 14 〉	통과 (1.51ms, 10.5MB)
테스트 15 〉	통과 (1.46ms, 10.4MB)
테스트 16 〉	통과 (1.13ms, 10.3MB)
테스트 17 〉	통과 (0.72ms, 10.3MB)
테스트 18 〉	통과 (0.34ms, 10.4MB)
테스트 19 〉	통과 (0.36ms, 10.4MB)
테스트 20 〉	통과 (0.71ms, 10.3MB)
'''