N,K = list(map(int, input().split()))
Ni = list(map(int, input().split()))
cnt = []
for i in Ni:
    for j in range(N):        
        if Ni[j]!=i and i+Ni[j]==K:
            if Ni[j] not in cnt:
                cnt.append(i)
                cnt.append(Ni[j])
print(int(len(cnt)/2))
            
