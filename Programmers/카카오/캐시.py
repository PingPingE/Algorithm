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