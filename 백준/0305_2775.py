#2775번) 부녀회장이 될테야
'''
평소 반상회에 참석하는 것을 좋아하는 주희는 이번 기회에 부녀회장이 되고 싶어
각 층의 사람들을 불러 모아 반상회를 주최하려고 한다.
이 아파트에 거주를 하려면 조건이 있는데,
“a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼
사람들을 데려와 살아야 한다” 는 계약 조항을 꼭 지키고 들어와야 한다.
아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때,
주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라.
단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.

'''
#입력 : 첫 번째 줄에 Test case의 수 T가 주어진다. 그리고 각각의 케이스마다 입력으로
#첫 번째 줄에 정수 k, 두 번째 줄에 정수 n이 주어진다. (1 <= k <= 14, 1 <= n <= 14)

def cal(k,n): #층, 호수를 매개변수로 받는다.
    r = [] #아래층의 사람들 수를 담을 배열
    for j in range(1,n+1):#먼저 0층 사람들로 배열 초기화
        r.append(j)

    for i in range(k):#층수 만큼 반복
        for j in range(n):#호수 만큼 반복

            if j > 0: #0보다 크면(즉 1호가 아니면)
                r[j]= r[j-1]+r[j] #자기 자신과 전 호수를 더한 값으로 갱신

            else:#0이면(1호면)
                r[j] = 1 #1로 갱신
                
    return r[n-1]#사람 수 리턴
    
T = int(input())
for i in range(T):
    k = int(input()) #층 
    n = int(input()) #호
    if n==1: #1이면 바로 1 출력
        print(1)
        continue
    elif n==2: #2면 바로 층+2 출력
        print(k+2)
        continue
    else:
        res = cal(k,n)
        print(res)
        continue

#출력 : 각각의 Test case에 대해서 해당 집에 거주민 수를 출력하라.
