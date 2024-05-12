'''
문제 설명
A와 B가 n개의 주사위를 가지고 승부를 합니다. 주사위의 6개 면에 각각 하나의 수가 쓰여 있으며, 주사위를 던졌을 때 각 면이 나올 확률은 동일합니다.
 각 주사위는 1 ~ n의 번호를 가지고 있으며, 주사위에 쓰인 수의 구성은 모두 다릅니다.
A가 먼저 n / 2개의 주사위를 가져가면 B가 남은 n / 2개의 주사위를 가져갑니다. 각각 가져간 주사위를 모두 굴린 뒤,
나온 수들을 모두 합해 점수를 계산합니다. 점수가 더 큰 쪽이 승리하며, 점수가 같다면 무승부입니다.
A는 자신이 승리할 확률이 가장 높아지도록 주사위를 가져가려 합니다.

주사위에 쓰인 수의 구성을 담은 2차원 정수 배열 dice가 매개변수로 주어집니다.
이때, 자신이 승리할 확률이 가장 높아지기 위해 A가 골라야 하는 주사위 번호를 오름차순으로 1차원 정수 배열에 담아 return 하도록 solution 함수를 완성해 주세요. 승리할 확률이 가장 높은 주사위 조합이 유일한 경우만 주어집니다.

제한사항
2 ≤ dice의 길이 = n ≤ 10
n은 2의 배수입니다.
dice[i]는 i+1번 주사위에 쓰인 6개의 수를 담고 있습니다.
dice[i]의 길이 = 6
1 ≤ dice[i]의 원소 ≤ 100

'''
from itertools import combinations, product
#메모이제이션 / 바이너리서치로 해보기
def simulation(A,B):
    a_wins = 0
    for result in product(*(A+B)):
        result = list(result)
        N = len(result)//2
        a_sum = sum(result[:N])
        b_sum = sum(result[N:])
        if a_sum > b_sum:
            a_wins+=1
    return a_wins

def solution(dice):
    answer_wins = 0
    answer = []
    N = len(dice)
    set_N = set(range(N))
    for comb in combinations(range(N),N//2):
        comb = set(comb)
        a, b= list(dice[i] for i in comb), list(dice[i] for i in set_N-comb)
        a_wins = simulation(a,b)
        if a_wins > answer_wins:
            answer_wins = a_wins
            answer = sorted(c+1 for c in comb)
    return answer