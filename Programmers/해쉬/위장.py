'''
문제 설명

스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.
예를 들어 스파이가 가진 옷이 아래와 같고 오늘 스파이가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야 합니다.
종류	이름
얼굴	동그란 안경, 검정 선글라스
상의	파란색 티셔츠
하의	청바지
겉옷	긴 코트
스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
같은 이름을 가진 의상은 존재하지 않습니다.
clothes의 모든 원소는 문자열로 이루어져 있습니다.
모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
스파이는 하루에 최소 한 개의 의상은 입습니다.

'''
from collections import defaultdict
def solution(clothes):
    clothes_dict = defaultdict(int)
    for c_name, c_type in clothes:
        clothes_dict[c_type] += 1
    answer = 1
    for v in clothes_dict.values():
        # 해당 종류의 옷 입는 경우의 수 + 안입는다
        answer *= (v + 1)
    return answer - 1  # 아무것도 안입는 경우의 수 빼주기


#테스트 케이스 1개 시간초과난 코드
#정확성: 96.4 합계: 96.4 / 100.0
from itertools import combinations
from functools import reduce
from collections import defaultdict
def solution_bef(clothes):
    def multi(a, b):
        return a * b

    clothes_dict = defaultdict(int)
    for c_name, c_type in clothes:
        clothes_dict[c_type] += 1
    N_type = len(clothes_dict)
    answer = 0

    # 몇개의 의상
    for n in range(1, N_type + 1):
        for comb in combinations(clothes_dict.values(), n):
            answer += reduce(multi, comb, 1)
    return answer
