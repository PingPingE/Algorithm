#시도 중
import re
from collections import defaultdict

def solution(word, pages):
    answer = 0
    word = word.lower()
    # url을 index에 매핑
    page_dic = {}  # key: url, value: index

    # 자기 지신에게 링크를 건 링크 idx set
    link_dic = defaultdict(set)  # key: url, value: 링크(idx) set
    extern_score = [0 for _ in range(len(pages))]
    basic_score = [0 for _ in range(len(pages))]

    for idx, page in enumerate(pages):
        page = page.lower()
        tmp = page.split('</head>')
        target = tmp[0].split('content=')[-1].split('/>')[0]
        page_dic[target] = idx
        a_tag = re.findall('<a href=.*</a>', tmp[-1])

        # 외부 링크 수
        extern_score[idx] = len(a_tag)

        body_tag = tmp[-1].split('</body>')[0].split('<body>')[-1].strip()
        for a in a_tag:
            body_tag = re.sub(a, '', body_tag).strip()
            link = a.split('href=')[-1].split('>')[0]
            # link를 링크로 건 현재 url의 idx를 set에 저장
            link_dic[link].add(idx)

        body_tag = re.sub('[^a-z]', ' ', body_tag)

        # 기본 점수
        for w in body_tag.split():
            if w == word:
                basic_score[idx] += 1

    ans = [0, 100]  # 점수, index

    # 링크 점수, 매칭 점수 구하기
    for k, v in page_dic.items():
        link_score = 0
        # 링크 점수 계산
        for idx in link_dic[k]:
            if link not in page_dic:
                continue
            try:
                link_score += basic_score[idx] / extern_score[idx]
            except:
                continue
        # 매치 점수 계산
        match_score = basic_score[v] + link_score
        if match_score > ans[0]:
            ans[0], ans[1] = match_score, v

        elif match_score == ans[0]:
            ans[1] = min(ans[1], v)
    return ans[1]