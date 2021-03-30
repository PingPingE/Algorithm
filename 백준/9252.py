#LCS 참고:https://twinw.tistory.com/126
str1,str2=input(), input()
ans=''
memo=[[0]*(len(str2)+1) for _ in range(len(str1)+1 )]
#LCS 길이 구하기
for i in range(1,len(str2)+1):
    for j in range(1,len(str1)+1):
        if str1[j-1] == str2[i-1]:
            memo[i][j]=memo[i-1][j-1]+1 #현재 값을 보기 전인 왼쪽 위 값 + 1
        else:
            memo[i][j]=max(memo[i-1][j], memo[i][j-1])#위나 왼쪽 원소 중 더 큰 값

#LCS 구하기
maxx=0
ans=[]
for i in range(len(str2)+1):#열부터 봐야한다.
    for j in range(min(len(str1),len(str2))+1):
        if memo[j][i]>maxx:
            maxx=memo[j][i]
            ans.append(str1[i-1])
            break

print(len(ans))
if len(ans)>0:
    print(''.join(ans))