#일반적으로 최대공약수를 구하는 알고리즘
def sol1(a,b):
    i = min(a,b) #a와b중 작은 값
    while True:
        if a%i == 0 and b%i ==0: #만약 a,b 둘다 나누어 떨어지는 값이면 return
            return i
        i -= 1#아니면 1 감소

#유클리드 방식을 이용한 알고리즘
def sol2(a,b):
    if b==0:
        return a
    return sol2(b,a%b) #재귀호출 하다가 a%b가 0이 되면 b가 최대공약수가 된다.

print(sol1(32,144))
print(sol2(32,144))
