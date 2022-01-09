'''
문제
성화는 악독하기로 유명한 편의점 사장이다. 그의 편의점에는 특이한 임금 체계를 가지고 있다.

각 날마다 일의 차이때문에 일마다 급여가 정해져 있다.
돈은 당일에 주지 않고 퇴직을 할 때 한번에 준다.
성화는 욕심쟁이라서 해당 일을 한 동안 중 가장 일급이 작을 때를 기준으로 급여를 지급한다.
일급이 다른 것을 들키지 않기 위하여 한번이라도 퇴직한 자를 다시 취직 시키지 않는다. (만약 취직을 한다면, 일을 시작 한 날부터 끝날 때까지 하루도 빠지면 안 된다.)
준수는 n+1일 후에 001에 월세를 내야 해서 성화가 사장으로 있는 편의점에 취직하려 한다. 다행히 주변 퇴직자들의 얘기로 급여에 관련해 파악했다.
또한 퇴직자들의 급여 통계를 통해 당장 n일 후까지 일급 정보를 알아냈다. 최대로 많이 일했을 때가 최대 이익이 아닐 수 있다.

어제까지 과제를 제출하고 지금도 001에서 자고 있는 준수를 위해 코딩 잘하는 여러분이 일을 해서 벌 수 있는 최대 이익을 준수에게 알려주도록 하자.

입력
일을 할 수 있는 날의 수 (0 < n ≤ 100000) 가 주어진다.

그 다음 줄 에는 1일부터 n일 까지 일급 Ti 가 순서대로 주어진다. (0 < Ti ≤ 1,000,000)

출력
준수가 일을 해서 벌 수 있는 최대 이익을 출력한다.
'''
#풀이 참고: https://www.acmicpc.net/blog/view/12

n = int(input())
daily_pay = list(map(int, input().split()))
st = []
ans = 0

for i in range(n):
    #현재 index(i)에 있는 원소가 스택의 top 값을 인덱스로하는 원소보다 더 작으면 계산 ㄲ
    while st and daily_pay[st[-1]] > daily_pay[i]:
        height = daily_pay[st[-1]]
        st.pop()
        width = i-(-1 if not st else st[-1])-1
        ans = max(ans, height*width)
    st.append(i)

i=n
while st:
    height = daily_pay[st[-1]]
    st.pop()
    width = i - (-1 if not st else st[-1]) - 1
    ans = max(ans, height * width)
st.append(i)


print(ans)
