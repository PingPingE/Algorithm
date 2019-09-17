#기타줄 N개 사기위해 필요한 돈의 최솟값
#M개의 브랜드
N, M =map(int, input().split())

arr = []
Set = -1
EA = -1
result = -1
for i in range(M):
    # 6줄 패키지, 낱개가격 입력받기
    arr.append(list(map(int, input().split())))
    if N%6 == 0:
        tmpSet = (N//6)*arr[i][0]
    else:
        tmpSet=((N//6)+1)*arr[i][0]

    tmpEA = N*arr[i][1]

    #패키지구매, 낱개구매 중 더 싼 가격 tmp에 저장
    if tmpSet > tmpEA :
        tmp =  tmpEA
    else:
        tmp = tmpSet

    #result와 비교 후 저장
    if result == -1 or result > tmp:
        result = tmp

    #패키지, 낱개 최저 가격 각각 저장
    if Set == -1 or Set > arr[i][0]:
        Set = arr[i][0]
    if EA == -1 or EA > arr[i][1]:
        EA = arr[i][1]

#패키지 + 낱개
if N > 6 and N%6 != 0:
    SE = Set*(N//6) + EA*(N%6)
    if SE < result:
        result = SE
print(result)

