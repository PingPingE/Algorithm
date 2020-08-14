#두개의 스택으로 큐 구현(pop, push)
class queue:
    def __init__(self):
        self.st1=[]
        self.st2=[]#pop할때 담을 stack

    def pop(self):
        if len(self.st2) == 0:
            if len(self.st1) == 0:
                print("No data in stack")
                return

            for i in range(len(self.st1)-1,-1,-1):
                self.st2.append(self.st1[i])
            self.st1 = []
        print(self.st2[-1])
        del(self.st2[-1])

    def push(self,x):
        self.st1.append(x)


q = queue()
for n in range(5):
    q.push(n)

for _ in range(6):
    q.pop()

'''
출력)
0
1
2
3
4
No data in stack
'''