def solution(n, results):
    if n<3:
        return n
    dic = {r:[set(),set()] for r in range(1,n+1)}
    ans = 0
    for w, l in results:
        dic[w][0].add(l)
        dic[l][1].add(w)

    for k,v in dic.items():
        for win in v[0]: 
            dic[win][1].update(v[1])
            dic[win][1].add(k)

        for lose in v[1]:
            dic[lose][0].update(v[0])
            dic[lose][0].add(k)
            
    return len(list(filter(lambda x: len(x[0]) + len(x[1]) == n-1, dic.values())))

정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.8MB)
테스트 2 〉	통과 (0.06ms, 10.7MB)
테스트 3 〉	통과 (0.08ms, 10.8MB)
테스트 4 〉	통과 (0.07ms, 10.7MB)
테스트 5 〉	통과 (0.48ms, 10.9MB)
테스트 6 〉	통과 (0.76ms, 10.9MB)
테스트 7 〉	통과 (2.54ms, 11.4MB)
테스트 8 〉	통과 (5.03ms, 13.8MB)
테스트 9 〉	통과 (6.74ms, 16.3MB)
테스트 10 〉	통과 (7.56ms, 17.6MB)

#다른 사람 코드를 참고한 코드로, 훨씬 빠르다...
sol2는 dic.items()를 돌면서 자기자신(해당 key)의 value만 갱신했지 연관된 다른 key들은 갱신하지 않았다.
이 코드는 dic.items()를 돌면서 자기자신이 아닌 연관된 다른 key들을 모두 갱신한다. 
