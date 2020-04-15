num = list(map(int, input().split()))
A = input().split()
B = input().split()
G = input().split()
cntA = 0
cntB = 0
for i in G:
    if i in A:
        cntA += 1
    elif i in B:
        cntB += 1

if cntA>cntB:
    print("A")
elif cntA<cntB:
    print("B")
else:
    print("TIE")
        
        
