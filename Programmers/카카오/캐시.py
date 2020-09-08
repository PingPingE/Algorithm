from collections import deque
def solution(cacheSize, cities):
    answer = 0
    que = deque()
    if cacheSize == 0:
        return len(cities) * 5
    for city in cities:
        city = city.upper()
        if city in que:
            answer += 1
            que.remove(city)
            que.append(city)
        else:
            answer += 5
            if len(que) == cacheSize:
                que.popleft()
                que.append(city)
            else:
                que.append(city)

    return answer

'''
from collections import deque
def solution(cacheSize, cities):
    answer = 0
    que = deque(maxlen=cacheSize) #크기 제한을 할 수 있었다!!! 큐가 찬 상태에서 아이템을 넣으면 첫 아이템 자동 삭제
    if cacheSize == 0:
        return len(cities) * 5
    for city in cities:
        city = city.upper()
        if city in que:
            answer += 1
            que.remove(city)
            que.append(city)
        else:
            answer += 5
            que.append(city)
    return answer

'''

