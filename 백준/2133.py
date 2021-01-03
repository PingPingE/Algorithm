'''
타일을 직접 몇번 그려보고 계산해봐야
규칙이 조금 보인다
참고)
https://suri78.tistory.com/103
https://hjp845.tistory.com/28
'''
#타일채우기
#120784kb	120ms
N = int(input())
memo = [0 for _ in range(N+1)]
memo[0] = 1
if N%2 == 1: print(0)
else:
    memo[2] = 3
    for i in range(4,N+1,2):
        memo[i] = memo[i-2]*3 #이전 타일 + 3*2타일(3가지)
        for j in range(i-4, -1,-2):
            memo[i] += memo[j]*2
    print(memo[N])
