N = int(input())
check = [0 for _ in range(N+2)]
prime = []
prime_ap = prime.append
tmp_sum=0
s,e = 0,0
cnt =0
if N <2:
    print(0)
else:
    #소수 구하기
    #소수 구하면서 중간중간에도 연산하면 222552kb	720ms
    #그냥 소수 다 구하고 연산하면 	222424kb	616ms
    for i in range(2, N+1):
        if check[i]:
            continue
        prime_ap(i)
        # if s>e:
        #     break
        # if tmp_sum > N:
        #     tmp_sum -= prime[s]
        #     s+=1
        # else:
        #     tmp_sum += prime[e]
        #     e+=1
        # if tmp_sum == N:
        #     cnt += 1

        for j in range(i*i,N+1,i):
            check[j] = 1
    while s<=e:
        if tmp_sum > N:
            tmp_sum -= prime[s]
            s+=1
        elif e == len(prime):
            break
        else:
            tmp_sum += prime[e]
            e+=1
        if tmp_sum == N:
            cnt += 1
    print(cnt)