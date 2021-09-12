#시도 중
import re
from collections import defaultdict

def solution(word, pages):
    answer = 0
    word = word.lower()
    # url을 index에 매핑
    page_dic = {}  # key: url, value: index

    # 링크 점수
    link_score = [0 for _ in range(len(pages))]

    # 자기 자신(key)이 외부로 링크를 건 링크 url set(value)
    extern_dic = defaultdict(set)  # key: idx, value: url set
    basic_score = [0 for _ in range(len(pages))]

    for idx, page in enumerate(pages):
        page = page.lower()

        # 태그로 구분하지말고 일단 url만 추출하기
        links = re.findall('''\"https://.*\"''', page)

        # 맨 첫 url은 대상 링크(target) 나머진 외부 링크
        target = links[0]
        page_dic[target] = idx

        # 외부 링크 set
        extern_dic[idx].update(list(links[i] for i in range(1, len(links))))

        # body부분만 자르고 a태그 기준 나누기
        body_tag = page.split('<body>')[1].split('</body>')[0].split('<a')
        body_candi = []
        if len(body_tag) == 1:
            body_candi = body_tag[0]
        else:
            for body in body_tag:
                tmp = body.split('</a>')
                body_candi.append(tmp[-1])

        body_candi = ''.join(body_candi)
        # 문자만 남기기
        body_candi = re.sub('[^a-z]', ' ', body_candi).strip()

        # 기본 점수
        for w in body_candi.split():
            if w == word:
                basic_score[idx] += 1

    ans = [0, 100]  # 점수, index

    # 링크 점수, 매칭 점수 구하기
    for k, v in page_dic.items():
        link_score = 0
        # 링크 점수 계산
        for k2, v2 in extern_dic.items():
            try:
                if k in v2:
                    link_score += basic_score[k2] / len(extern_dic[k2])
            except:
                continue

        # 매치 점수 계산
        match_score = basic_score[v] + link_score
        if match_score > ans[0]:
            ans[0], ans[1] = match_score, v

        elif match_score == ans[0]:
            ans[1] = min(ans[1], v)

    return ans[1]

'''
정확성  테스트
테스트 1 〉	통과 (0.64ms, 10.4MB)
테스트 2 〉	통과 (0.53ms, 10.3MB)
테스트 3 〉	통과 (0.49ms, 10.3MB)
테스트 4 〉	실패 (0.55ms, 10.2MB)
테스트 5 〉	통과 (0.61ms, 10.3MB)
테스트 6 〉	실패 (0.61ms, 10.4MB)
테스트 7 〉	통과 (0.58ms, 10.3MB)
테스트 8 〉	실패 (0.59ms, 10.2MB)
테스트 9 〉	실패 (0.59ms, 10.3MB)
테스트 10 〉	실패 (0.53ms, 10.3MB)
테스트 11 〉	통과 (0.45ms, 10.2MB)
테스트 12 〉	통과 (0.42ms, 10.3MB)
테스트 13 〉	통과 (0.42ms, 10.3MB)
테스트 14 〉	통과 (0.49ms, 10.3MB)
테스트 15 〉	통과 (0.43ms, 10.3MB)
테스트 16 〉	통과 (0.21ms, 10.2MB)
테스트 17 〉	실패 (0.37ms, 10.3MB)
테스트 18 〉	통과 (0.17ms, 10.3MB)
테스트 19 〉	통과 (0.23ms, 10.3MB)
테스트 20 〉	통과 (0.48ms, 10.3MB)

채점 결과
정확성: 70.0
합계: 70.0 / 100.0
'''
