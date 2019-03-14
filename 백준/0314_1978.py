'''
1978번) 소수찾기
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
'''
#입력:첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
N = int(input())
a = list(map(int, input().split()))
cnt =0
for i in a:
    status = 0 #소수인지 아닌지 분별
    if i==2: #2는 소수
        cnt+=1
        continue
    elif i==1:#1은 소수가 아님
        continue
    
    for j in range(2,18):#17까지 검사한 이유는 1000 이하의 숫자에 17*17까지가
                         #걸러내야할 숫자가 있으므로(289는 소수가 아님)
        if i!=j and i%j == 0: #자기 자신이 아니고 나머지가 0인 숫자가 있으면
            status = 1#소수가 아니면 status 를 1로
            break
    #status가 0이면 
    if status == 0:
        cnt+=1

print(cnt)
